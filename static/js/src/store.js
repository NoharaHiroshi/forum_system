import Vuex from "vuex";
import Vue from 'vue'

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    user: null,
    isLogin: false
  },
  mutations: {
    setUser(state, userObj) {
      state.user = userObj;
    },
    setLoginStatus(state, status) {
      state.isLogin = status;
    }
  }
});

export default store;