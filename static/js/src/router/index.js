import Vue from 'vue'
import Router from 'vue-router'
import App from '@/App'
import Layout from '@/components/common/Layout'
import Index from '@/components/Index'

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      component: App,
      children: [
        {
          path: '/',
          component: Layout,
          children: [
            {
              path: '/',
              name: 'index',
              component: Index
            }
          ]
        }
      ]
    }
  ]
});

export default router
