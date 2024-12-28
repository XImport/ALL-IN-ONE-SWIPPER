import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-plugin-electron'
import path from 'path'

export default defineConfig({
  base: './',  // This is crucial for production builds
  plugins: [
    vue(),
    electron([
      {
        // Main process entry file
        entry: 'electron/main.js',
        onstart(options) {
          options.startup()
        },
      }
    ])
  ],
  build: {
    outDir: 'dist',
    assetsDir: '.',
    rollupOptions: {
      output: {
        format: 'cjs'
      }
    }
  }
})