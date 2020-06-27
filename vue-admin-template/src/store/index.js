import Vue from 'vue'
import Vuex from 'vuex'
import getters from './getters'
import app from './modules/app'
import settings from './modules/settings'
import user from './modules/user'
import admin from './modules/admin'
import student from './modules/student'
import teacher from './modules/teacher'
Vue.use(Vuex)

const store = new Vuex.Store({
  modules: {
    app,
    settings,
    user,
    admin,
    student,
    teacher
  },
  getters
})

export default store
