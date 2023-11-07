import { createRouter, createWebHistory } from 'vue-router'
import MainPageContent from '../pages/MainPageContent.vue'
import Login from '../pages/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/tasks',
      component: MainPageContent
    },
    {
      path: '/login',
      component: Login
    }
  ]
})

export default router
