import { defineConfig } from 'vite'

// Contorna erro do minificador de CSS (lightningcss) com o CSS de blocos de código do Slidev
export default defineConfig({
  build: { cssMinify: false },
})
