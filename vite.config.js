import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import electron from 'vite-plugin-electron'
import path from 'path'

export default defineConfig({
  base: './',
  plugins: [
    vue(),
    electron([
      {
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
        format: 'es',  // Changed from 'cjs' to 'es'
        inlineDynamicImports: true
      }
    },
    target: 'esnext'
  },
  optimizeDeps: {
    esbuildOptions: {
      target: 'esnext'
    },
    include: ['jspdf', 'html2pdf.js']
  },
  resolve: {
    alias: {
      '@': path.resolve(__dirname, './src')
    }
  }
})