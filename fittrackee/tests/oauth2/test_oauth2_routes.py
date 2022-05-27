import json
from typing import List, Union
from unittest.mock import patch
from urllib.parse import parse_qs

import pytest
from flask import Flask
from urllib3.util import parse_url
from werkzeug.test import TestResponse

from fittrackee.oauth2.models import OAuth2Client, OAuth2Token
from fittrackee.users.models import User

from ..mixins import ApiTestCaseMixin
from ..utils import TEST_OAUTH_CLIENT_METADATA


class TestOAuthClientCreation(ApiTestCaseMixin):
    route = '/api/oauth/apps'

    def test_it_returns_error_when_no_user_authenticated(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )

        response = client.post(
            self.route,
            data=json.dumps(TEST_OAUTH_CLIENT_METADATA),
            content_type='application/json',
        )

        self.assert_401(response)

    def test_it_returns_error_when_no_metadata_provided(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )

        response = client.post(
            self.route,
            data=json.dumps(dict()),
            content_type='application/json',
            headers=dict(Authorization=f'Bearer {auth_token}'),
        )

        self.assert_400(
            response, error_message='OAuth client metadata missing'
        )

    @pytest.mark.parametrize(
        'missing_key',
        [
            'client_name',
            'client_uri',
            'redirect_uris',
            'scope',
        ],
    )
    def test_it_returns_error_when_metadata_key_is_missing(
        self, app: Flask, user_1: User, missing_key: str
    ) -> None:
        metadata = TEST_OAUTH_CLIENT_METADATA.copy()
        del metadata[missing_key]
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )

        response = client.post(
            self.route,
            data=json.dumps(metadata),
            content_type='application/json',
            headers=dict(Authorization=f'Bearer {auth_token}'),
        )

        self.assert_400(
            response,
            error_message=f'OAuth client metadata missing keys: {missing_key}',
        )

    def test_it_creates_oauth_client(self, app: Flask, user_1: User) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )

        response = client.post(
            self.route,
            data=json.dumps(TEST_OAUTH_CLIENT_METADATA),
            content_type='application/json',
            headers=dict(Authorization=f'Bearer {auth_token}'),
        )

        assert response.status_code == 201
        oauth_client = OAuth2Client.query.first()
        assert oauth_client is not None

    def test_it_returns_serialized_oauth_client(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        client_id = self.random_string()
        client_secret = self.random_string()
        with patch(
            'fittrackee.oauth2.client.gen_salt',
            side_effect=[client_id, client_secret],
        ):

            response = client.post(
                self.route,
                data=json.dumps(TEST_OAUTH_CLIENT_METADATA),
                content_type='application/json',
                headers=dict(Authorization=f'Bearer {auth_token}'),
            )

        data = json.loads(response.data.decode())
        assert data['data']['client']['client_id'] == client_id
        assert data['data']['client']['client_secret'] == client_secret
        assert (
            data['data']['client']['name']
            == TEST_OAUTH_CLIENT_METADATA['client_name']
        )
        assert (
            data['data']['client']['redirect_uris']
            == TEST_OAUTH_CLIENT_METADATA['redirect_uris']
        )
        assert (
            data['data']['client']['website']
            == TEST_OAUTH_CLIENT_METADATA['client_uri']
        )

    @pytest.mark.parametrize(
        'input_key,expected_value',
        [
            ('grant_types', ['authorization_code', 'refresh_token']),
            ('response_types', ['code']),
            ('token_endpoint_auth_method', 'client_secret_post'),
        ],
    )
    def test_it_always_creates_oauth_client_with_authorization_grant(
        self,
        app: Flask,
        user_1: User,
        input_key: str,
        expected_value: Union[List, str],
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )

        client.post(
            self.route,
            data=json.dumps(
                {**TEST_OAUTH_CLIENT_METADATA, input_key: self.random_string()}
            ),
            content_type='application/json',
            headers=dict(Authorization=f'Bearer {auth_token}'),
        )

        oauth_client = OAuth2Client.query.first()
        assert getattr(oauth_client, input_key) == expected_value


class TestOAuthClientAuthorization(ApiTestCaseMixin):
    route = '/api/oauth/authorize'

    def test_it_returns_error_not_authenticated(
        self, app: Flask, user_1: User
    ) -> None:
        oauth_client = self.create_oauth_client(user_1)
        client = app.test_client()

        response = client.post(
            self.route,
            data={
                'client_id': oauth_client.client_id,
                'response_type': 'code',
            },
            headers=dict(content_type='multipart/form-data'),
        )

        self.assert_401(response)

    def test_it_returns_error_when_client_id_is_missing(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )

        response = client.post(
            self.route,
            data={'response_type': 'code'},
            headers=dict(
                Authorization=f'Bearer {auth_token}',
                content_type='multipart/form-data',
            ),
        )

        self.assert_400(response, error_message='invalid payload')

    def test_it_returns_error_when_response_type_is_missing(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        oauth_client = self.create_oauth_client(user_1)

        response = client.post(
            self.route,
            data={'client_id': oauth_client.client_id},
            headers=dict(
                Authorization=f'Bearer {auth_token}',
                content_type='multipart/form-data',
            ),
        )

        self.assert_400(response, error_message='invalid payload')

    def test_it_returns_code_in_url(self, app: Flask, user_1: User) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        oauth_client = self.create_oauth_client(user_1)

        response = client.post(
            self.route,
            data={
                'client_id': oauth_client.client_id,
                'response_type': 'code',
            },
            headers=dict(
                Authorization=f'Bearer {auth_token}',
                content_type='multipart/form-data',
            ),
        )

        assert response.status_code == 302
        parsed_url = parse_url(response.location)
        assert parse_qs(parsed_url.query).get('code') is not None


class TestOAuthIssueToken(ApiTestCaseMixin):
    route = '/api/oauth/token'

    @staticmethod
    def assert_token_is_returned(response: TestResponse) -> None:
        assert response.status_code == 200
        data = json.loads(response.data.decode())
        assert data.get('access_token') is not None
        assert data.get('expires_in') is not None
        assert data.get('refresh_token') is not None
        assert data.get('token_type') == 'Bearer'

    def test_it_returns_error_when_form_is_empty(self, app: Flask) -> None:
        client = app.test_client()

        response = client.post(
            self.route,
            data=dict(data='{}'),
            headers=dict(content_type='multipart/form-data'),
        )

        self.assert_unsupported_grant_type(response)

    def test_it_returns_error_when_client_id_is_invalid(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        oauth_client = self.create_oauth_client(user_1)
        code = self.authorize_client(client, oauth_client, auth_token)

        response = client.post(
            self.route,
            data={
                'client_id': self.random_string(),
                'client_secret': oauth_client.client_secret,
                'grant_type': 'authorization_code',
                'code': code,
            },
            headers=dict(content_type='multipart/form-data'),
        )

        self.assert_invalid_client(response)

    def test_it_returns_error_when_client_secret_is_invalid(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        oauth_client = self.create_oauth_client(user_1)
        code = self.authorize_client(client, oauth_client, auth_token)

        response = client.post(
            self.route,
            data={
                'client_id': oauth_client.client_id,
                'client_secret': self.random_string(),
                'grant_type': 'authorization_code',
                'code': code,
            },
            headers=dict(content_type='multipart/form-data'),
        )

        self.assert_invalid_client(response)

    def test_it_returns_error_when_client_not_authorized(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        oauth_client = self.create_oauth_client(user_1)

        response = client.post(
            self.route,
            data={
                'client_id': oauth_client.client_id,
                'client_secret': oauth_client.client_secret,
                'grant_type': 'authorization_code',
                'code': self.random_string(),
            },
            headers=dict(content_type='multipart/form-data'),
        )

        self.assert_invalid_request(response)

    def test_it_returns_error_when_code_is_invalid(
        self, app: Flask, user_1: User
    ) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        oauth_client = self.create_oauth_client(user_1)
        self.authorize_client(client, oauth_client, auth_token)

        response = client.post(
            self.route,
            data={
                'client_id': oauth_client.client_id,
                'client_secret': oauth_client.client_secret,
                'grant_type': 'authorization_code',
                'code': self.random_string(),
            },
            headers=dict(content_type='multipart/form-data'),
        )

        self.assert_invalid_request(response)

    def test_it_returns_access_token(self, app: Flask, user_1: User) -> None:
        client, auth_token = self.get_test_client_and_auth_token(
            app, user_1.email
        )
        oauth_client = self.create_oauth_client(user_1)
        code = self.authorize_client(client, oauth_client, auth_token)

        response = client.post(
            self.route,
            data={
                'client_id': oauth_client.client_id,
                'client_secret': oauth_client.client_secret,
                'grant_type': 'authorization_code',
                'code': code,
            },
            headers=dict(content_type='multipart/form-data'),
        )

        self.assert_token_is_returned(response)


class TestOAuthTokenRevocation(ApiTestCaseMixin):
    route = '/api/oauth/revoke'

    def test_it_revokes_user_token(self, app: Flask, user_1: User) -> None:
        (
            client,
            oauth_client,
            access_token,
        ) = self.create_oauth_client_and_issue_token(app, user_1)

        response = client.post(
            self.route,
            data={
                'client_id': oauth_client.client_id,
                'client_secret': oauth_client.client_secret,
                'token': access_token,
            },
            headers=dict(content_type='multipart/form-data'),
        )

        assert response.status_code == 200
        token = OAuth2Token.query.filter_by(
            client_id=oauth_client.client_id
        ).first()
        assert token.access_token_revoked_at is not None
