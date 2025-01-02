import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AuthView from '../views/AuthView.vue'
import Temp from '../views/Temp.vue'
import ProtectedView from '../views/Protected.vue'


import OvertimeEmployee from '../components/OvertimeEmployee.vue'
import OvertimeOwner from '../components/OvertimeOwner.vue'
import Profile from '../components/Profile.vue'
import ReadSlip from '../components/ReadSlip.vue'
// import SiteNavigation from '../components/SiteNavigation.vue'
import Statistics from '../components/Statistics.vue'
import UserManagement from '../components/UserManagement.vue'
import ForbiddenView from '../components/ForbiddenView.vue'

import Cookies from 'js-cookie'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/login',
      name: 'login',
      component: AuthView
    },
    {
      path: '/register',
      name: 'register',
      component: Temp
    },
    {
      name: "Manage Users",
      path: "/UserManagement",
      component: UserManagement,
      meta: { requiresAuth: true, roles: ['owner'] },
    },
    {
      name: "Payroll Slip",
      path: "/ReadSlip",
      component: ReadSlip,
      meta: { requiresAuth: true },
    },
    {
      name: "Overtime Owner",
      path: "/OvertimeOwner",
      component: OvertimeOwner,
      meta: { requiresAuth: true, roles: ['owner', 'finance'] },
    },
    {
      name: "Overtime Employee",
      path: "/OvertimeEmployee",
      component: OvertimeEmployee,
      meta: { requiresAuth: true, roles: ['employee'] },
    },
    {
      name: "Statistics",
      path: "/Statistics",
      component: Statistics,
      meta: { requiresAuth: true, roles: ['owner', 'finance'] },
    },
    {
      name: "Profile",
      path: "/Profile",
      component: Profile,
      meta: { requiresAuth: true },
    },
    {
      name: "Protected",
      path: "/protected",
      component: ProtectedView,
      meta: { requiresAuth: true },
    },
    {
      path: '/403',
      name: 'forbidden',
      component: ForbiddenView,
    },
  ]
})

function isAuthenticated() {
  const token = Cookies.get('csrf_access_token')
  return !!token
}

function getUserRoles() {
  const token = Cookies.get('role');
  return token
}

router.beforeEach((to, from, next) => {
  const isAuth = isAuthenticated();
  const userRoles = getUserRoles();

  if (to.meta.requiresAuth && !isAuth) {
    return next({ name: 'login' });
  }

  if (to.meta.roles && !to.meta.roles.some(role => userRoles.includes(role))) {
    return next({ name: 'forbidden' });
  }
  next();
});

export default router;