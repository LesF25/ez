const { configure } = require('quasar/wrappers');

module.exports = configure(function (ctx) {
  return {
    boot: [
      'pinia'
    ],
    css: [
      'app.sass'
    ],
    extras: [
      'material-icons'
    ],

    store: true,

    framework: {
      config: {},
      plugins: [
        'Notify'
      ]
    },

    build: {
      target: {
        browser: ['es2019', 'edge88', 'firefox78', 'chrome87', 'safari13.1'],
      },
      vueRouterMode: 'hash',
    },

    devServer: {
      port: 9000,
      host: '0.0.0.0',
      open: false
    }
  }
});