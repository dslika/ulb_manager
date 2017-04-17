import Vue from 'vue'
import Router from 'vue-router'
import Base from '@/components/Base'
import Home from '@/components/Home'
import Doc from '@/components/Doc'
import Contact from '@/components/Contact'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Home',
      component: {
        extends: Base,
        components: {
          'main-page': Home
        }
      }
    },
    {
      path: '/doc',
      name: 'Doc',
      component: {
        extends: Base,
        components: {
          'main-page': Doc
        }
      }
    },
    {
      path: '/contact',
      name: 'Contact',
      component: {
        extends: Base,
        components: {
          'main-page': Contact
        }
      }
    }
  ]
})
