import { getTerm } from '@/api/user'
import { getToken } from '@/utils/auth'
import { getScore, getSelectedCourse, getCourse, select, delet } from '@/api/student'
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
  // user login
  delet({ state }, data) {
    return new Promise((resolve, reject) => {
      delet({ xh: state.token, xq: data.xq, gh: data.gh, kh: data.kh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  select({ state }, data) {
    return new Promise((resolve, reject) => {
      select({ xh: state.token, xq: data.xq, gh: data.gh, kh: data.kh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getScore({ state }, data) {
    return new Promise((resolve, reject) => {
      getScore({ xh: state.token, xq: data.xq }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getSelectedCourse({ state }, data) {
    return new Promise((resolve, reject) => {
      getSelectedCourse({ xh: state.token, xq: data.xq }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getCourse({ state }, data) {
    return new Promise((resolve, reject) => {
      getCourse({ xh: state.token, xq: data.xq, kh: data.kh, gh: data.gh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  setSx({ commit }, creditSetting) {
    // const { term, yxh, credit } = creditSetting
    console.log('setSx', creditSetting)
    // const xyh = credit.yxh
    // const xf = credit.credit
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
