import axios from 'axios'
import { getErrorMessage } from '@/utils/error'

export default {
  state: {
    status: '',
    token: localStorage.getItem('token') || '',
    user: {}
  },
  mutations: {
    auth_success (state, token) {
      state.token = token
    },
    logout (state) {
      state.token = ''
    }
  },
  actions: {
    login ({ commit }, user) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://18.220.255.127/api/auth/token/login/', data: user, method: 'POST' })
          .then(resp => {
            const token = 'Token ' + resp.data.auth_token
            localStorage.setItem('token', token)
            axios.defaults.headers.common.Authorization = token
            commit('auth_success', token)
            commit('clearError')
            resolve(resp)
          })
          .catch(err => {
            commit('setError', getErrorMessage(err.response.data))
            localStorage.removeItem('token')
          })
      })
    },
    getUserInfo ({ commit }) {
      return new Promise((resolve, reject) => {

      })
    },
    register ({ commit }, user) {
      return new Promise((resolve, reject) => {
        axios({ url: 'http://18.220.255.127/api/user/registration/', data: user, method: 'POST' })
          .catch(err => {
            commit('setError', getErrorMessage(err.response.data))
          })
      })
    },
    logout ({ commit }) {
      return new Promise((resolve, reject) => {
        commit('logout')
        axios({ url: 'http://18.220.255.127/api/auth/token/logout/', method: 'POST' })
        localStorage.removeItem('token')
        delete axios.defaults.headers.common.Authorization
        resolve()
      })
    }
  },
  getters: {
    isLoggedIn: state => !!state.token,
    authStatus: state => state.status
  }
}
