import fs from 'fs'
import { fileURLToPath } from 'url'
import { dirname, resolve } from 'path'

// Resolve __dirname in ES module scope
const __dirname = dirname(fileURLToPath(import.meta.url))

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',
  devtools: { enabled: true },
  server: {
    https: {
      key: fs.readFileSync(resolve(__dirname, 'pages/192.168.0.106-key.pem')),
      cert: fs.readFileSync(resolve(__dirname, 'pages/192.168.0.106-cert.pem')),
    },
    host: '0.0.0.0',
    port: 3000,
  }
})

