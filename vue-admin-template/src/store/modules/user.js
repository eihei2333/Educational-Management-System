import { login, logout, getInfo, getTerm, getCollege, changePassword } from '@/api/user'
import { getToken, setToken, removeToken } from '@/utils/auth'
import { resetRouter } from '@/router'
import { setSx } from '@/api/admin'

const getDefaultState = () => {
  return {
    token: getToken(),
    name: '',
    avatar: ''
  }
}

const state = getDefaultState()

const mutations = {
  RESET_STATE: (state) => {
    Object.assign(state, getDefaultState())
  },
  SET_TOKEN: (state, token) => {
    state.token = token
  },
  SET_NAME: (state, name) => {
    state.name = name
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar
  }
}

const actions = {
  changePassword({ state }, pass) {
    const usr = state.token
    const pwd = pass.pass
    console.log('pass', pass)
    return new Promise((resolve, reject) => {
      changePassword({ usr: usr, pwd: pwd }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  // user login
  login({ commit }, userInfo) {
    console.log('userInfo', userInfo)
    const { identification, username, password } = userInfo
    return new Promise((resolve, reject) => {
      login({ identification: identification, username: username.trim(), password: password, identification1: 'sss' }).then(response => {
        const { data } = response
        console.log('data', data, response)
        commit('SET_TOKEN', data.token)
        setToken(data.token)
        resolve()
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },

  getTerm({ state }) {
    return new Promise((resolve, reject) => {
      getTerm(state.token).then(response => {
        console.log('data')
        const { data } = response
        console.log(data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  getCollege({ state }) {
    return new Promise((resolve, reject) => {
      getCollege(state.token).then(response => {
        console.log('data')
        const { data } = response
        console.log(data)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // get user info
  getInfo({ commit, state }) {
    return new Promise((resolve, reject) => {
      getInfo(state.token).then(response => {
        console.log('data')
        const { data } = response

        if (!data) {
          reject('Verification failed, please Login again.')
        }

        const { name, avatar } = data
        commit('SET_NAME', name)
        commit('SET_AVATAR', avatar)
        resolve(data)
      }).catch(error => {
        reject(error)
      })
    })
  },

  // user logout
  logout({ commit, state }) {
    return new Promise((resolve, reject) => {
      logout(state.token).then(() => {
        removeToken() // must remove  token  first
        resetRouter()
        commit('RESET_STATE')
        resolve()
      }).catch(error => {
        reject(error)
      })
    })
  },

  // remove token
  resetToken({ commit }) {
    return new Promise(resolve => {
      removeToken() // must remove  token  first
      commit('RESET_STATE')
      resolve()
    })
  },
  setSx({ commit }, creditSetting) {
    console.log('setSx', creditSetting)
    return new Promise((resolve, reject) => {
      setSx({ term: creditSetting.term, xy: creditSetting.yxh, xf: creditSetting.credit }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}

