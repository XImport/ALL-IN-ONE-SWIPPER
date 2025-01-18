import { createApp } from 'vue'
import App from './App.vue'

// Vuetify
import 'vuetify/styles'
import { createVuetify } from 'vuetify'
import * as components from 'vuetify/components'
import * as directives from 'vuetify/directives'
import '@mdi/font/css/materialdesignicons.css'
import Axios from "./Axios"
import Router from "./router"
import Store from './Store'
import 'animate.css';
import CORS from "cors"
import PrimeVue from 'primevue/config';

import "primevue/resources/themes/saga-blue/theme.css"; //theme
import "primevue/resources/primevue.min.css"; //core CSS
import "primeicons/primeicons.css"; //icons



const vuetify = createVuetify({
  components,
  directives
})




const app = createApp(App)

app.use(Axios)
app.use(Store)
app.use(PrimeVue)




app.use(CORS)
app.use(Router)
app.use(vuetify)
app.mount('#app')