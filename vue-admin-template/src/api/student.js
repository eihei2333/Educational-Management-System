import request from '@/utils/request'

export function login(data) {
  return request({
    url: 'http://127.0.0.1:5000/login ',
    method: 'POST',
    data
  })
}

export function changePassword(data) {
  return request({
    url: 'http://127.0.0.1:5000/changePassword ',
    method: 'POST',
    data
  })
}
export function delet(data) {
  return request({
    url: 'http://127.0.0.1:5000/student/delete ',
    method: 'POST',
    data
  })
}
export function select(data) {
  return request({
    url: 'http://127.0.0.1:5000/student/select ',
    method: 'POST',
    data
  })
}
export function getScore(data) {
  return request({
    url: 'http://127.0.0.1:5000/student/getScore ',
    method: 'POST',
    data
  })
}
export function getSelectedCourse(data) {
  return request({
    url: 'http://127.0.0.1:5000/student/getSelectedCourse ',
    method: 'POST',
    data
  })
}
export function getCourse(data) {
  return request({
    url: 'http://127.0.0.1:5000/student/getCourse ',
    method: 'POST',
    data
  })
}
export function getInfo(token) {
  return request({
    url: 'http://127.0.0.1:5000/getInfo',
    method: 'GET',
    params: { token }
  })
}
