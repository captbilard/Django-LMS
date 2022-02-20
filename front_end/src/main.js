import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'
//axios global configuration
axios.defaults.baseURL = "https://bilard.pythonanywhere.com"

createApp(App).use(store).use(router, axios).mount('#app')
