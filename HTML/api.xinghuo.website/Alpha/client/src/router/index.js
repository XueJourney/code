import { createRouter, createWebHistory } from 'vue-router';
import APIList from '@/components/APIList/APIList.vue';
import IdCard from '@/components/IdCard.vue';

const routes = [
    {
        path: '/',
        name: 'index',
        component: APIList,
    },
    {
        path: '/apilist',
        name: 'APIList',
        component: APIList,
    },
    {
        path: '/doc/idcard',
        name: 'IdCard',
        component: IdCard
    }
];

const router = createRouter({
    mode: 'hash',
    history: createWebHistory(),
    routes
});

export default router;
