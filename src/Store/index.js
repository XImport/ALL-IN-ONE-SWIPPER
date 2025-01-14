// src/store/index.js
import { createStore } from 'vuex'

export default createStore({
  state: {
   title : {debutDate : "",finDate : ""},
   Dialog : false,
   Drawer : true
  },
  
  getters: {
   getTtitleContent(state){
    return state.title
   },
   GetDialogState(state){
    return state.Dialog 
   },
   GetDrawerState(state){
    return state.Drawer
   }
   
  },
  
  mutations: {
    ChangeTitleContent(state,payload){
      state.title.debutDate = payload.DébutDate
      state.title.finDate = payload.FinDate
    },
    ChangeDialogState(state){
      state.Dialog = !state.Dialog
    },
    ChangeDrawerState(state){
      state.Drawer = !state.Drawer
    }
   
  },
  
  actions: {
   
  },
  
  modules: {
    // Your modules here
  }
})