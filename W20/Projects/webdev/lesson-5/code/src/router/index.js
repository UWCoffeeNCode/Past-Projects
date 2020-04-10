import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import Dashboard from '../components/Dashboard.vue'
import AddItem from '../components/AddItem.vue'
import Error from '../components/Error'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: Home },
        { path: '/dashboard', component: Dashboard },
        { path: '/add-item', component: AddItem },
        { path: '*', component: Error}
    ],
    linkActiveClass: 'is-active'  // needed because of Bulma
})