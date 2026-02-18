import { createApp } from 'vue'
import { createPinia } from 'pinia' // ИМПОРТ
import App from './App.vue'
import router from './router'

const app = createApp(App)
const pinia = createPinia() // СОЗДАНИЕ

app.use(pinia) // ПОДКЛЮЧЕНИЕ К APP
app.use(router)
app.mount('#q-app')