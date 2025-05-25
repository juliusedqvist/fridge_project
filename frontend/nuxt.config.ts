import fs from 'fs'
import { fileURLToPath } from 'url'
import { dirname, resolve } from 'path'

// Resolve __dirname in ES module scope
const __dirname = dirname(fileURLToPath(import.meta.url))

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  server: {
    host: '0.0.0.0',
    port: 3000,
  },
  vite: {
    server: {
      host: '0.0.0.0',  // listen on all interfaces
      allowedHosts: ['fridge-project.com', 'localhost', '127.0.0.1'],
    },
  },
})

