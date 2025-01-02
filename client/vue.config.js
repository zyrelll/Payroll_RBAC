module.exports = {
    devServer: {
      proxy: {
        '^/register': {
          target: 'http://127.0.0.1:5001/',
          ws: true,
          changeOrigin: true
        },
      }
    }
  }