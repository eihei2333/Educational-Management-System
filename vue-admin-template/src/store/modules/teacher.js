import { getToken } from '@/utils/auth'
import { getClass, getStudent, updateScore } from '@/api/teacher'
import { setSx } from '@/api/admin'
import da from 'element-ui/src/locale/lang/da'

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
  updateScore({ state }, data) {
    return new Promise((resolve, reject) => {
      updateScore({ gh: state.token, xq: data.xq, kh: data.kh, xh: data.xh, pscj: data.pscj, kscj: data.kscj }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getStudent({ state }, data) {
    return new Promise((resolve, reject) => {
      getStudent({ gh: state.token, xq: data.xq, kh: data.kh, xh: data.xh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getClass({ state }, data) {
    return new Promise((resolve, reject) => {
      getClass({ gh: state.token, xq: data.xq, kh: data.kh }).then(response => {
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
