import Vue from 'vue'
import Router from 'vue-router'
import App from '@/App'
import Layout from '@/components/common/Layout'
import Index from '@/components/Index'
import Register from '@/components/common/Register'
import Login from '@/components/common/Login'
import Forum from "@/components/content/Forum"
import AddPost from "@/components/content/AddPost"
import store from '@/store'

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
              component: Index,
              meta: {
                needLogin: false
              }
            },{
              path: "register",
              name: "register",
              component: Register,
              meta: {
                needLogin: false
              }
            }, {
              path: "login",
              name: "login",
              component: Login,
              meta: {
                needLogin: false
              }
            }, {
              path: "forum/:sub_forum_id",
              name: "forum",
              component: Forum,
              meta: {
                needLogin: false
              }
            }, {
              path: "forum/:sub_forum_id/add_post",
              name: "add_post",
              component: AddPost,
              meta: {
                needLogin: true
              }
            }
          ]
        }
      ]
    }
  ]
});

router.beforeEach((to, from, next) => {
  let isLogin = localStorage.getItem("isLogin");
  let user = localStorage.getItem("user");
  if (isLogin === "1") {
    store.state.isLogin = "1";
    store.state.user = JSON.parse(user);
    if (to.name === "login" || to.name === "register") {
      next({
        name: "index"
      })
    }else {
      next();
    }
  }else {
    if (to.meta.needLogin) {
      next({
        name: "login"
      })
    } else {
        next();
    }
  }
});

export default router
