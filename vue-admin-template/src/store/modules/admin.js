import { getTerm } from '@/api/user'
import { setSx, getCourseByTerm, createCourse, getAllCourse, getClass, getStudent, deletCourse, deletClass, deletStudentFromClass, createStudentInClass, createClass, getAllStudent, getAllTeacher, creatStudent, creatTeacher, deleteStudent, deleteTeacher } from '@/api/admin'
import { getToken } from '@/utils/auth'

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
  },
  getCourseByTerm({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      getCourseByTerm({ term: data.xq, kh: data.kh, km: data.km }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getAllCourse({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      getAllCourse({ term: data.xq, kh: data.kh, km: data.km }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getAllStudent({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      getAllStudent({ xh: data.xh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getAllTeacher({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      getAllTeacher({ gh: data.gh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getClass({ commit }, data) {
    return new Promise((resolve, reject) => {
      getClass({ term: data.xq, kh: data.kh, gh: data.gh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  getStudent({ commit }, data) {
    return new Promise((resolve, reject) => {
      getStudent({ term: data.xq, kh: data.kh, gh: data.gh, xh: data.xh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  createCourse({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      createCourse({ term: data.xq, kh: data.kh, km: data.km, xf: data.xf, xs: data.xs, yx: data.yx }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  creatStudent({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      creatStudent({ xh: data.xh, xm: data.xm, yx: data.yxh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  creatTeacher({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      creatTeacher({ gh: data.gh, xm: data.xm, yx: data.yxh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  createStudentInClass({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      createStudentInClass({ xq: data.xq, kh: data.kh, xh: data.xh, gh: data.gh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  createClass({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      createClass({ xq: data.xq, kh: data.kh, gh: data.gh, sksj: data.sksj }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  deletCourse({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      deletCourse({ kh: data.kh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  deleteStudent({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      deleteStudent({ xh: data.xh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  deleteTeacher({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      deleteTeacher({ gh: data.gh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  deletClass({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      deletClass({ xq: data.xq, kh: data.kh, gh: data.gh, sksj: data.sksj, xs: data.xs, yx: data.yx }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
      }).catch(error => {
        console.log(error)
        reject(error)
      })
    })
  },
  deletStudentFromClass({ commit }, data) {
    console.log('data', data)
    return new Promise((resolve, reject) => {
      deletStudentFromClass({ xq: data.xq, kh: data.kh, gh: data.gh, xh: data.xh }).then(response => {
        const { data } = response
        console.log('data', data, response)
        resolve(data)
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
  }
}

export default {
  namespaced: true,
  state,
  mutations,
  actions
}
