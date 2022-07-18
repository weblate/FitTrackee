export enum AuthUserActions {
  CHECK_AUTH_USER = 'CHECK_AUTH_USER',
  CONFIRM_ACCOUNT = 'CONFIRM_ACCOUNT',
  CONFIRM_EMAIL = 'CONFIRM_EMAIL',
  DELETE_ACCOUNT = 'DELETE_ACCOUNT',
  DELETE_PICTURE = 'DELETE_PICTURE',
  GET_USER_PROFILE = 'GET_USER_PROFILE',
  LOGIN_OR_REGISTER = 'LOGIN_OR_REGISTER',
  LOGOUT = 'LOGOUT',
  SEND_PASSWORD_RESET_REQUEST = 'SEND_PASSWORD_RESET_REQUEST',
  RESEND_ACCOUNT_CONFIRMATION_EMAIL = 'RESEND_ACCOUNT_CONFIRMATION_EMAIL',
  RESET_USER_PASSWORD = 'RESET_USER_PASSWORD',
  RESET_USER_SPORT_PREFERENCES = 'RESET_USER_SPORT_PREFERENCES',
  UPDATE_USER_ACCOUNT = 'UPDATE_USER_ACCOUNT',
  UPDATE_USER_PICTURE = 'UPDATE_USER_PICTURE',
  UPDATE_USER_PROFILE = 'UPDATE_USER_PROFILE',
  UPDATE_USER_PREFERENCES = 'UPDATE_USER_PREFERENCES',
  UPDATE_USER_SPORT_PREFERENCES = 'UPDATE_USER_SPORT_PREFERENCES',
}

export enum AuthUserGetters {
  AUTH_TOKEN = 'AUTH_TOKEN',
  AUTH_USER_PROFILE = 'AUTH_USER_PROFILE',
  IS_ADMIN = 'IS_ADMIN',
  IS_AUTHENTICATED = 'IS_AUTHENTICATED',
  IS_SUCCESS = 'IS_SUCCESS',
  IS_REGISTRATION_SUCCESS = 'IS_REGISTRATION_SUCCESS',
  USER_LOADING = 'USER_LOADING',
}

export enum AuthUserMutations {
  CLEAR_AUTH_USER_TOKEN = 'CLEAR_AUTH_USER_TOKEN',
  UPDATE_AUTH_TOKEN = 'UPDATE_AUTH_TOKEN',
  UPDATE_AUTH_USER_PROFILE = 'UPDATE_AUTH_USER_PROFILE',
  UPDATE_IS_SUCCESS = 'UPDATE_USER_IS_SUCCESS',
  UPDATE_IS_REGISTRATION_SUCCESS = 'UPDATE_IS_REGISTRATION_SUCCESS',
  UPDATE_USER_LOADING = 'UPDATE_USER_LOADING',
}
