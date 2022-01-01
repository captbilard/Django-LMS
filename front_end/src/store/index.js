import { createStore } from "vuex";

export default createStore({
  state: {
    user: {
      token: null,
      isAuthenticated: false,
    },
  },
  mutations: {
    initializeStore: function (state) {
      if (localStorage.getItem("token")) {
        state.user.token = localStorage.getItem("token");
        state.user.isAuthenticated = true;
      } else {
        state.user.token = null;
        state.user.isAuthenticated = false;
      }
    },
    setToken: function (state, token) {
      state.user.token = token;
      state.user.isAuthenticated = true;
    },
    removeToken: function (state) {
      state.user.token = null;
      state.user.isAuthenticated = false;
    },
  },
  actions: {},
  modules: {},
});
