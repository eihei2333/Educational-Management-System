import request from '@/utils/request'

export function login(data) {
  return request({
    url: 'http://127.0.0.1:5000/login ',
    method: 'POST',
    data
  })
}
export function updateScore(data) {
  return request({
    url: 'http://127.0.0.1:5000/teacher/updateScore ',
    method: 'POST',
    data
  })
}
export function getStudent(data) {
  return request({
    url: 'http://127.0.0.1:5000/teacher/getStudent ',
    method: 'POST',
    data
  })
}
export function getClass(data) {
  return request({
    url: 'http://127.0.0.1:5000/teacher/getClass ',
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

export function getInfo(token) {
  return request({
    url: 'http://127.0.0.1:5000/getInfo',
    method: 'GET',
    params: { token }
  })
}
