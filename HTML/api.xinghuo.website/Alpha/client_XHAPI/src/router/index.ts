import { createRouter, createWebHistory } from 'vue-router'
import APIList from '../views/APIList/APIList.vue'
import IdCard from '../views/IdCard.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'index',
      component: APIList
    },
    {
      path: '/apilist',
      name: 'APIList',
      component: APIList
    },
    {
      path: '/doc/idcard',
      name: 'IdCard',
      component: IdCard
    }
  ]
})

export default router
