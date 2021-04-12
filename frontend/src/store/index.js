import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth.module'

Vue.use(Vuex)

export default new Vuex.Store({
  state () {
    return {
      error: null
    }
  },
  mutations: {
    setError (state, error) {
      state.error = error
    },
    clearError (state) {
      state.error = null
    }
  },
  getters: {
    error: s => s.error
  },
  modules: {
    auth
  }
})
