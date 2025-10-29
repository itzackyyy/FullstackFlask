import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': 'http://localhost:8080' // CAMBIAR EN CASO DE QUE NO SEA ESTE PUERTO
    }
  }
})

// HACER npm start

// INICIAR SERVIDOR cd client => npm run dev