<template>
    <header class="top-header">
        <div class="logo">API</div>
        <div class="slogan">星火免费API - 公益项目，永不收费</div>
        <div class="right-hand">
			<button @click="toggleTheme" class="theme-toggle-button">切换主题</button>
            <img src="/img/email_icon.png" alt="email" class="email-icon" />
        </div>
    </header>
    <div class="api-list-container">
        <api-card
            v-for="api in apis"
            :key="api.id"
            :name="api.name"
            :description="api.description"
            :image-url="api.imageUrl"
            :tag="api.tag"
			:author="api.author"
			:url="api.url"
        />
    </div>
</template>

<script>
import ApiCard from './ApiCard.vue';

export default {
    components: {
        ApiCard
    },
    data() {
        return {
            // 来自第二份代码的数据
            apis: [
                {
                    id: 1,
                    name: '二要素实名认证',
                    description: '姓名、身份证二要素实名认证',
                    tag: '热门',
                    imageUrl: '/img/IDCard.png',
                    author: "官方",
					url:"/doc/IDCard"
                }
                // ...其他API对象
            ],
            // 来自第一份代码的数据
            darkMode: window.matchMedia('(prefers-color-scheme: dark)').matches
        };
    },
    methods: {
        // 来自第一份代码的方法
        toggleTheme() {
            this.darkMode = !this.darkMode;
            if (this.darkMode) {
                document.documentElement.style.setProperty('--background-color', 'var(--background-color-dark)');
                document.documentElement.style.setProperty('--text-color', 'var(--text-color-dark)');
            } else {
                document.documentElement.style.setProperty('--background-color', 'var(--background-color-light)');
                document.documentElement.style.setProperty('--text-color', 'var(--text-color-light)');
            }
        }
    },
    created() {
        // 来自第一份代码的 created 钩子
        window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
            this.darkMode = e.matches;
            this.toggleTheme();
        });
    }
};
</script>

<style>
.api-list-container {
    display: flex;
    flex-wrap: wrap;
    gap: 20px;
    justify-content: center;
    padding: 20px;
}

/* 全局样式 */
body {
    font-family: 'Arial', sans-serif;
    background-color: var(--background-color);
	color: var(--text-color);
    margin: 0;
}

.top-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px 20px;
    background-color: var(--background-color);
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.logo {
    font-size: 24px;
    font-weight: bold;
    color: #007bff;
}

.slogan {
    font-size: 14px;
	text-align: center;
    color: var(--text-color);
}

.right-hand {
    display: flex;
    align-items: center;
	gap:24px;
}

.email-icon {
    width: 36px; /* 或者其他尺寸，根据您的图标大小调整 */
    height: auto;
}

.theme-toggle-button {
	cursor: pointer;
	background-color: #fff;
	border: 1px solid #ccc;
	border-radius: 15px;
	padding: 5px 10px;
	margin-left: 10px;
	transition: background-color 0.3s;
}

.theme-toggle-button:hover {
	background-color: #e0e0e0;
}
</style>
