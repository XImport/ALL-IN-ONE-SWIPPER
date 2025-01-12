import { createApp } from 'vue'
import { createStore } from 'vuex'

Vue.use(Vuex);

export default createStore({
  state: {
   
    count: 0,
    
  },
  mutations: {
    // Define methods to modify the state
    
  },
  actions: {
   
  },
  getters: {
    // Define getters to retrieve state values
    getCount(state) {
      return state.count;
    },
   
  }
});
