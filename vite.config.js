import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/portal-sio/', // <-- ESTO ES CLAVE
  plugins: [vue()]
})