<template>
  <div>
    <button @click="startButton"> {{ show ? "Hide" : "Show" }} </button>
  </div>
  <div v-if="show">
    <h1>Streckkodsscanner</h1>
    <div class="scanner-container" ref="scannerContainer"
      style="width: 80%; max-width: 300px; height: 300px; border: 1px solid #ccc;"></div>
    <p>{{ resultText }}</p>
    <h2>Loggar</h2>
    <pre style="background: #f0f0f0; padding: 1em; height: 150px; overflow-y: auto;">{{ logs }}</pre>
  </div>
  <div>
    <p> {{ latestCode }} </p>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import Quagga from 'quagga'

const scannerContainer = ref(null);
const resultText = ref('Ingen streckkod scannad ännu');
const logs = ref('');

const show = ref(false);
const latestCode = ref('');

function startButton() {
  show.value = !show.value;

  if (show.value) {
    log('Komponenten monterad');
    nextTick(() => {
      startScanner(); // now scannerContainer is available
    });
  } else {
    Quagga.stop();
    log('Scanner stoppad');
  }
}

function log(msg) {
  logs.value += msg + '\n';
  console.log(msg);
}

function startScanner() {
  if (!scannerContainer.value) {
    log('Ingen scannerContainer ref hittad');
    return
  }

  Quagga.init({
    inputStream: {
      type: "LiveStream",
      constraints: {
        facingMode: "environment"
      },
      target: scannerContainer.value
    },
    decoder: {
      readers: ["code_128_reader", "ean_reader", "ean_8_reader"]
    }
  }, (err) => {
    if (err) {
      log(`Init error: ${err}`)
      return
    }
    Quagga.start()
    log('Scanner startad')
  })

  Quagga.onDetected((result) => {
    const code = result.codeResult.code
    latestCode = code
  })
}
//
// onMounted(() => {
//   startScanner()
// })

onBeforeUnmount(() => {
  Quagga.stop()
  log('Scanner stoppad')
})
</script>

<style scoped>
div[ref="scannerContainer"],
div[ref="scannerContainer"] video,
div[ref="scannerContainer"] canvas {
  width: 50% !important;
  height: 50% !important;
  object-fit: cover;
}
</style>
