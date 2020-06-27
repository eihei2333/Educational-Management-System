import request from '@/utils/request'

export function setSx(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/setSx ',
    method: 'POST',
    data
  })
}

export function getCourseByTerm(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/getCourseByTerm ',
    method: 'POST',
    data
  })
}

export function createCourse(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/createCourse ',
    method: 'POST',
    data
  })
}
export function creatStudent(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/creatStudent ',
    method: 'POST',
    data
  })
}
export function creatTeacher(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/creatTeacher ',
    method: 'POST',
    data
  })
}
export function createClass(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/createClass ',
    method: 'POST',
    data
  })
}
export function createStudentInClass(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/createStudentInClass ',
    method: 'POST',
    data
  })
}
export function getStudent(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/getStudent ',
    method: 'POST',
    data
  })
}
export function getClass(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/getClass ',
    method: 'POST',
    data
  })
}
export function deletCourse(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/deletCourse ',
    method: 'POST',
    data
  })
}
export function deletClass(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/deletClass ',
    method: 'POST',
    data
  })
}
deleteTeacher
export function deleteTeacher(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/deleteTeacher ',
    method: 'POST',
    data
  })
}
export function deleteStudent(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/deleteStudent ',
    method: 'POST',
    data
  })
}
export function deletStudentFromClass(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/deletStudentFromClass ',
    method: 'POST',
    data
  })
}
export function getAllCourse(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/getAllCourse ',
    method: 'POST',
    data
  })
}
export function getAllTeacher(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/getAllTeacher ',
    method: 'POST',
    data
  })
}
export function getAllStudent(data) {
  return request({
    url: 'http://127.0.0.1:5000/admin/getAllStudent ',
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
