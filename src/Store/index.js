// src/store/index.js
import { createStore } from 'vuex'

export default createStore({
  state: {
   title : {debutDate : "",finDate : ""},
   Dialog : false,
   Drawer : true,
   ClientDialog : false,
   OneClientData : {},
   Querys : {}
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
   },
   GetClientDialog(state){
    return state.ClientDialog
   },
   GetOneClientData(state){
    return state.OneClientData
   },
   GetQuerys(state){
    return state.Querys
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
    },
    ChangeClientDialog(state){
      state.ClientDialog = !state.ClientDialog
    },
    ChangeOneClientData(state,payload){
      state.OneClientData = payload
    },
    ChangeQuerysData(state,payload){
      state.Querys = payload
    }
   
  },
  
  actions: {
   
  },
  
  modules: {
    // Your modules here
  }
})