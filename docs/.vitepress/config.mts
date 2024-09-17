import {defineConfig} from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
    title: "mhyy.py",
    description: "Python 米哈云游（云·原神、云·星穹铁道）的 API 封装。",
    base: '/mhyy.py/',
    themeConfig: {
        // https://vitepress.dev/reference/default-theme-config
        nav: [
            {
                text: '主页',
                link: '/'
            },
            {
                text: '指南',
                link: '/guide/what-is-mhyy-py',
                activeMatch: '/guide/'
            },
            {
                text: 'API 参考',
                link: '/reference/interface'
            }
        ],

        sidebar: {
            '/guide/': [
                {
                    text: '简介',
                    items: [
                        {text: '关于 mhyy.py', link: '/guide/what-is-mhyy-py'},
                        {text: '快速入门', link: '/guide/quick-start'}
                    ]
                }
            ]
        },

        socialLinks: [
            {icon: 'github', link: 'https://github.com/Mooneze/mhyy.py'}
        ]
    }
})
