import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "MHYY.PY",
  description: "米哈云游（云·原神、云·星穹铁道）签到方法及其他方法的API封装",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '主页', link: '/' },
      { text: 'API 参考', link: '/api/interface/' }
    ],

    sidebar: [
      {
        text: 'MHYY.PY',
        items: [
          { text: '介绍', link: '/intro' }
        ]
      },
      {
        text: '使用',
        items: [
          { text: '快速开始', link: '/usage/quick_start' },
          { text: '多客户端支持', link: '/usage/multi_client_support' }
        ]
      },
      {
        text: '附录',
        items: [
          { text: '获取你的Headers', link: '/appendix/get_headers' }
        ]
      },
      {
        text: 'API 参考',
        items: [
          { text: '开发人员接口', link: '/api/interface' }
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/Mooneze/mhyy.py' }
    ]
  }
})
