// src/store/index.js
import { createStore } from 'vuex'

export default createStore({
  state: {
   title : {debutDate : "",finDate : ""}
  },
  
  getters: {
   getTtitleContent(state){
    return state.title
   }
   
  },
  
  mutations: {
    ChangeTitleContent(state,payload){
      state.title.debutDate = payload.DébutDate
      state.title.finDate = payload.FinDate
    }
   
  },
  
  actions: {
   
  },
  
  modules: {
    // Your modules here
  }
})