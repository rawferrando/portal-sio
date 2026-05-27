import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/portal-sio/', 
  plugins: [vue()],
  build: {
    outDir: 'docs', // <-- ¡Esto obliga a Vite a usar la carpeta de GitHub Pages!
    emptyOutDir: true // <-- Esto limpia la carpeta antes de construir para evitar basura vieja
  }
})