"use strict";(self["webpackChunkfittrackee_client"]=self["webpackChunkfittrackee_client"]||[]).push([[193],{9161:function(e,s,t){t.r(s),t.d(s,{default:function(){return A}});t(6699);var a=t(6252),r=t(2262),l=t(3577),o=t(3324),n=t(9996);const c={class:"chart-menu"},i={class:"chart-arrow"},u={class:"time-frames custom-checkboxes-group"},d={class:"time-frames-checkboxes custom-checkboxes"},p=["id","name","checked","onInput"],m={class:"chart-arrow"};var v=(0,a.aZ)({__name:"StatsMenu",emits:["arrowClick","timeFrameUpdate"],setup(e,{emit:s}){const t=(0,r.iH)("month"),o=["week","month","year"];function n(e){t.value=e,s("timeFrameUpdate",e)}return(e,r)=>((0,a.wg)(),(0,a.iD)("div",c,[(0,a._)("div",i,[(0,a._)("i",{class:"fa fa-chevron-left","aria-hidden":"true",onClick:r[0]||(r[0]=e=>s("arrowClick",!0))})]),(0,a._)("div",u,[(0,a._)("div",d,[((0,a.wg)(),(0,a.iD)(a.HY,null,(0,a.Ko)(o,(s=>(0,a._)("div",{class:"time-frame custom-checkbox",key:s},[(0,a._)("label",null,[(0,a._)("input",{type:"radio",id:s,name:s,checked:t.value===s,onInput:e=>n(s)},null,40,p),(0,a._)("span",null,(0,l.zw)(e.$t(`statistics.TIME_FRAMES.${s}`)),1)])]))),64))])]),(0,a._)("div",m,[(0,a._)("i",{class:"fa fa-chevron-right","aria-hidden":"true",onClick:r[1]||(r[1]=e=>s("arrowClick",!1))})])]))}}),k=t(3744);const _=(0,k.Z)(v,[["__scopeId","data-v-22d55de2"]]);var S=_,w=t(631);const f={class:"sports-menu"},h=["id","name","checked","onInput"],U={class:"sport-label"};var b=(0,a.aZ)({__name:"StatsSportsMenu",props:{userSports:null,selectedSportIds:{default:()=>[]}},emits:["selectedSportIdsUpdate"],setup(e,{emit:s}){const t=e,{t:n}=(0,o.QT)(),c=(0,a.f3)("sportColors"),{selectedSportIds:i}=(0,r.BK)(t),u=(0,a.Fl)((()=>(0,w.xH)(t.userSports,n)));function d(e){s("selectedSportIdsUpdate",e)}return(e,s)=>{const t=(0,a.up)("SportImage");return(0,a.wg)(),(0,a.iD)("div",f,[((0,a.wg)(!0),(0,a.iD)(a.HY,null,(0,a.Ko)((0,r.SU)(u),(e=>((0,a.wg)(),(0,a.iD)("label",{type:"checkbox",key:e.id,style:(0,l.j5)({color:e.color?e.color:(0,r.SU)(c)[e.label]})},[(0,a._)("input",{type:"checkbox",id:e.id,name:e.label,checked:(0,r.SU)(i).includes(e.id),onInput:s=>d(e.id)},null,40,h),(0,a.Wm)(t,{"sport-label":e.label,color:e.color},null,8,["sport-label","color"]),(0,a._)("span",U,(0,l.zw)(e.translatedLabel),1)],4)))),128))])}}});const I=b;var g=I,T=t(9318);const y={key:0,id:"user-statistics"};var C=(0,a.aZ)({__name:"index",props:{sports:null,user:null},setup(e){const s=e,{t:t}=(0,o.QT)(),{sports:l,user:c}=(0,r.BK)(s),i=(0,r.iH)("month"),u=(0,r.iH)(v(i.value)),d=(0,a.Fl)((()=>(0,w.xH)(s.sports,t))),p=(0,r.iH)(_(s.sports));function m(e){i.value=e,u.value=v(i.value)}function v(e){return(0,T.aZ)(new Date,e,s.user.weekm)}function k(e){u.value=(0,T.FN)(u.value,e,s.user.weekm)}function _(e){return e.map((e=>e.id))}function f(e){p.value.includes(e)?p.value=p.value.filter((s=>s!==e)):p.value.push(e)}return(0,a.YP)((()=>s.sports),(e=>{p.value=_(e)})),(e,s)=>(0,r.SU)(d)?((0,a.wg)(),(0,a.iD)("div",y,[(0,a.Wm)(S,{onTimeFrameUpdate:m,onArrowClick:k}),(0,a.Wm)(n.Z,{sports:(0,r.SU)(l),user:(0,r.SU)(c),chartParams:u.value,"displayed-sport-ids":p.value,fullStats:!0},null,8,["sports","user","chartParams","displayed-sport-ids"]),(0,a.Wm)(g,{"selected-sport-ids":p.value,"user-sports":(0,r.SU)(l),onSelectedSportIdsUpdate:f},null,8,["selected-sport-ids","user-sports"])])):(0,a.kq)("",!0)}});const F=(0,k.Z)(C,[["__scopeId","data-v-d693c7da"]]);var Z=F,x=t(5630),D=t(8602),H=t(9917);const E={id:"statistics",class:"view"},R={key:0,class:"container"};var W=(0,a.aZ)({__name:"StatisticsView",setup(e){const s=(0,H.o)(),t=(0,a.Fl)((()=>s.getters[D.YN.GETTERS.AUTH_USER_PROFILE])),o=(0,a.Fl)((()=>s.getters[D.O8.GETTERS.SPORTS].filter((e=>t.value.sports_list.includes(e.id)))));return(e,s)=>{const n=(0,a.up)("Card");return(0,a.wg)(),(0,a.iD)("div",E,[(0,r.SU)(t).username?((0,a.wg)(),(0,a.iD)("div",R,[(0,a.Wm)(n,null,{title:(0,a.w5)((()=>[(0,a.Uk)((0,l.zw)(e.$t("statistics.STATISTICS")),1)])),content:(0,a.w5)((()=>[(0,a.Wm)(Z,{class:(0,l.C_)({"stats-disabled":0===(0,r.SU)(t).nb_workouts}),user:(0,r.SU)(t),sports:(0,r.SU)(o)},null,8,["class","user","sports"])])),_:1}),0===(0,r.SU)(t).nb_workouts?((0,a.wg)(),(0,a.j4)(x.Z,{key:0})):(0,a.kq)("",!0)])):(0,a.kq)("",!0)])}}});const P=(0,k.Z)(W,[["__scopeId","data-v-2e341d4e"]]);var A=P}}]);
//# sourceMappingURL=statistics.1ad194e3.js.map