import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

/* Layout */
import Layout from '@/layout'

/**
 * Note: sub-menu only appear when route children.length >= 1
 * Detail see: https://panjiachen.github.io/vue-element-admin-site/guide/essentials/router-and-nav.html
 *
 * hidden: true                   if set true, item will not show in the sidebar(default is false)
 * alwaysShow: true               if set true, will always show the root menu
 *                                if not set alwaysShow, when item has more than one children route,
 *                                it will becomes nested mode, otherwise not show the root menu
 * redirect: noRedirect           if set noRedirect will no redirect in the breadcrumb
 * name:'router-name'             the name is used by <keep-alive> (must set!!!)
 * meta : {
    roles: ['admin','editor']    control the page roles (you can set multiple roles)
    title: 'title'               the name show in sidebar and breadcrumb (recommend set)
    icon: 'svg-name'             the icon show in the sidebar
    breadcrumb: false            if set false, the item will hidden in breadcrumb(default is true)
    activeMenu: '/example/list'  if set path, the sidebar will highlight the path you set
  }
 */

/**
 * constantRoutes
 * a base page that does not have permission requirements
 * all roles can be accessed
 */
export const constantRoutes = [
  {
    path: '/login',
    component: () => import('@/views/login/index'),
    hidden: true
  },

  {
    path: '/404',
    component: () => import('@/views/404'),
    hidden: true
  },

  {
    path: '/',
    component: Layout,
    redirect: '/personalInfo',
    children: [{
      path: 'personalInfo',
      name: '个人信息',
      component: () => import('@/views/personalInfo/index'),
      meta: { title: '个人信息管理', icon: 'dashboard' }
    }]
  }

  // {
  //   path: '/',
  //   component: Layout,
  //   redirect: '/dashboard',
  //   children: [{
  //     path: 'dashboard',
  //     name: 'Dashboard',
  //     component: () => import('@/views/dashboard/index'),
  //     meta: { title: 'Dashboard', icon: 'dashboard' }
  //   }]
  // }

  // {
  //   path: '/example',
  //   component: Layout,
  //   redirect: '/example/table',
  //   name: 'Example',
  //   meta: { title: 'Example', icon: 'example' },
  //   children: [
  //     {
  //       path: 'table',
  //       name: 'Table',
  //       component: () => import('@/views/table/index'),
  //       meta: { title: 'Table', icon: 'table' }
  //     },
  //     {
  //       path: 'tree',
  //       name: 'Tree',
  //       component: () => import('@/views/tree/index'),
  //       meta: { title: 'Tree', icon: 'tree' }
  //     }
  //   ]
  // },
  //
  // {
  //   path: '/form',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'index',
  //       name: 'Form',
  //       component: () => import('@/views/form/index'),
  //       meta: { title: 'Form', icon: 'form' }
  //     }
  //   ]
  // }
  //
  // {
  //   path: '/form',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'index',
  //       name: 'Form',
  //       component: () => import('@/views/form/index'),
  //       meta: { title: 'Form', icon: 'form' }
  //     }
  //   ]
  // },
  //
  // {
  //   path: '/nested',
  //   component: Layout,
  //   redirect: '/nested/menu1',
  //   name: 'Nested',
  //   meta: {
  //     title: 'Nested',
  //     icon: 'nested'
  //   },
  //   children: [
  //     {
  //       path: 'menu1',
  //       component: () => import('@/views/nested/menu1/index'), // Parent router-view
  //       name: 'Menu1',
  //       meta: { title: 'Menu1' },
  //       children: [
  //         {
  //           path: 'menu1-1',
  //           component: () => import('@/views/nested/menu1/menu1-1'),
  //           name: 'Menu1-1',
  //           meta: { title: 'Menu1-1' }
  //         },
  //         {
  //           path: 'menu1-2',
  //           component: () => import('@/views/nested/menu1/menu1-2'),
  //           name: 'Menu1-2',
  //           meta: { title: 'Menu1-2' },
  //           children: [
  //             {
  //               path: 'menu1-2-1',
  //               component: () => import('@/views/nested/menu1/menu1-2/menu1-2-1'),
  //               name: 'Menu1-2-1',
  //               meta: { title: 'Menu1-2-1' }
  //             },
  //             {
  //               path: 'menu1-2-2',
  //               component: () => import('@/views/nested/menu1/menu1-2/menu1-2-2'),
  //               name: 'Menu1-2-2',
  //               meta: { title: 'Menu1-2-2' }
  //             }
  //           ]
  //         },
  //         {
  //           path: 'menu1-3',
  //           component: () => import('@/views/nested/menu1/menu1-3'),
  //           name: 'Menu1-3',
  //           meta: { title: 'Menu1-3' }
  //         }
  //       ]
  //     },
  //     {
  //       path: 'menu2',
  //       component: () => import('@/views/nested/menu2/index'),
  //       meta: { title: 'menu2' }
  //     }
  //   ]
  // },
  // {
  //   path: 'external-link',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'https://panjiachen.github.io/vue-element-admin-site/#/',
  //       meta: { title: 'External Link', icon: 'link' }
  //     }
  //   ]
  // }
]

export const studentRoutes = [
  {
    path: '/student_class_choose',
    component: Layout,
    children: [
      {
        path: 'index',
        name: '选课',
        component: () => import('@/views/student_class_choose/index'),
        meta: { title: '选课', icon: 'form' }
      }
    ]
  },
  {
    path: '/student_class_delet',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'student_class_delet',
        component: () => import('@/views/student_class_delet/index'),
        meta: { title: '退课', icon: 'form' }
      }
    ]
  },
  // {
  //   path: '/student_class_view',
  //   component: Layout,
  //   children: [
  //     {
  //       path: 'index',
  //       name: 'student_class_view',
  //       component: () => import('@/views/student_class_view/index'),
  //       meta: { title: 'student_class_view', icon: 'form' }
  //     }
  //   ]
  // },
  {
    path: '/student_score',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'student_score',
        component: () => import('@/views/student_score/index'),
        meta: { title: '成绩查询', icon: 'form' }
      }
    ]
  },

  {
    path: 'external-link',
    component: Layout,
    children: [
      {
        path: 'https://github.com/2019ZSS/Educational-Management-System-/',
        meta: { title: '更多', icon: 'link' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

export const teacherRoutes = [
  {
    path: '/teacher_class',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'teacher_class',
        component: () => import('@/views/teacher_class/index'),
        meta: { title: '课程管理', icon: 'form' }
      }
    ]
  },
  {
    path: 'external-link',
    component: Layout,
    children: [
      {
        path: 'https://github.com/2019ZSS/Educational-Management-System-/',
        meta: { title: '更多', icon: 'link' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

export const adminRoutes = [
  {
    path: '/admin_xf',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'admin_xf',
        component: () => import('@/views/admin_xf/index'),
        meta: { title: '学分上限设置', icon: 'form' }
      }
    ]
  },
  {
    path: '/admin_course',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'admin_course',
        component: () => import('@/views/admin_course/index'),
        meta: { title: '课程管理', icon: 'form' }
      }
    ]
  },
  {
    path: '/admin_student',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'admin_student',
        component: () => import('@/views/admin_student/index'),
        meta: { title: '学生管理', icon: 'form' }
      }
    ]
  },
  {
    path: '/admin_teacher',
    component: Layout,
    children: [
      {
        path: 'index',
        name: 'admin_teacher',
        component: () => import('@/views/admin_teacher/index'),
        meta: { title: '教师管理', icon: 'form' }
      }
    ]
  },

  {
    path: 'external-link',
    component: Layout,
    children: [
      {
        path: 'https://github.com/2019ZSS/Educational-Management-System-/',
        meta: { title: '更多', icon: 'link' }
      }
    ]
  },
  // 404 page must be placed at the end !!!
  { path: '*', redirect: '/404', hidden: true }
]

const createRouter = () => new Router({
  // mode: 'history', // require service support
  scrollBehavior: () => ({ y: 0 }),
  routes: constantRoutes
})

const router = createRouter()

export function addRoutes(role) {
  console.log(router.options.routes)
  var a = []
  // router.options.routes = a.concat(constantRoutes, studentRoutes)
  // router.addRoutes(studentRoutes)
  if (role === 'student') {
    router.options.routes = a.concat(constantRoutes, studentRoutes)
    router.addRoutes(studentRoutes)
  }
  if (role === 'teacher') {
    router.options.routes = a.concat(constantRoutes, teacherRoutes)
    router.addRoutes(teacherRoutes)
  }
  if (role === 'admin') {
    router.options.routes = a.concat(constantRoutes, adminRoutes)
    router.addRoutes(adminRoutes)
  }
  console.log(router)
}

// Detail see: https://github.com/vuejs/vue-router/issues/1234#issuecomment-357941465
export function resetRouter() {
  const newRouter = createRouter()
  router.matcher = newRouter.matcher // reset router
}

export default router
