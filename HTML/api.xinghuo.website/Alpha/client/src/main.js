import { createApp } from 'vue';
import App from './App.vue';
import router from './router/index'; // Ensure you have a router configuration

// If you are using Vuex for state management, import your store here
// import store from './store';

const app = createApp(App);

// If using Vuex, apply your store here
// app.use(store);

app.use(router);
app.mount('#app');
