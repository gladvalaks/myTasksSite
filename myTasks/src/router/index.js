import { createRouter, createWebHistory } from 'vue-router'
import MainPageContent from '../pages/MainPageContent.vue'
import LoginPage from '../pages/LoginPage.vue'
import RegisterPage from '../pages/RegisterPage.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/tasks',
      component: MainPageContent
    },
    {
      path: '/login',
      component: LoginPage
    },
    {
      path: '/register',
      component:RegisterPage
    }
  ]
})

export default router
