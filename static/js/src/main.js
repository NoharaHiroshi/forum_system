import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui';
import axios from 'axios'
import VueAxios from 'vue-axios'
import 'element-ui/lib/theme-chalk/index.css';
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { far } from '@fortawesome/free-regular-svg-icons'
import { fab } from '@fortawesome/free-brands-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import util from './util/util'
import api from './router/api'
import store from './store'
import config from "./config"
import VueQuillEditor from 'vue-quill-editor'
import 'quill/dist/quill.core.css'
import 'quill/dist/quill.snow.css'
import 'quill/dist/quill.bubble.css'

Vue.use(VueQuillEditor);


Vue.config.productionTip = false;
library.add(fas, far, fab);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(ElementUI);
Vue.use(VueAxios, axios);

Vue.prototype.$util = util;
Vue.prototype.$api = api;
Vue.prototype.$config = config;

new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
});