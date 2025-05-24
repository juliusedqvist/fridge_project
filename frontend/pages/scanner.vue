<template>
  <div>
  </div>
  <div>
    <ul class="navbar">
      <li class="nav-element" style="width: 80%;">Latest scanned code: {{ latestCode }}</li>
      <li class="nav-element" style="width: 20%;"><button @click="findProduct(latestCode)">Get product</button></li>
    </ul>
  </div>
  <div class="navbar2">
    <li class="nav2-element" style="width: 55%;">{{ product }}</li>
    <li class="nav2-element"><button @click="getWeight">scale</button></li>
    <li class="nav2-element">{{ weight }}</li>
  </div>
  <p class="whole-button">Add to database</p>
  <button @click="startButton"> {{ show ? "Hide" : "Show" }} </button>
  <div v-if="show">
    <div class="scanner-container" ref="scannerContainer"
      style="width: 80%; max-width: 300px; height: 300px; border: 1px solid #ccc;"></div>
    <p>{{ resultText }}</p>
    <h2>Loggar</h2>
    <pre style="background: #f0f0f0; padding: 1em; height: 150px; overflow-y: auto;">{{ logs }}</pre>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import Quagga from '@ericblade/quagga2'
import axios from 'axios'

const scannerContainer = ref(null);
const resultText = ref('Ingen streckkod scannad ännu');
const logs = ref('');

const show = ref(false);
const latestCode = ref('');
const product = ref('Produktnamn');
const weight = ref('N/A');

async function getWeight() {
  try {
    const response = await axios.get(`/api/weight`)
    weight.value = `${response.data.weight}`


  } catch (error) {
    console.log(`Fel vid API-förfrågan: ${error.message}`)
  }
}

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

async function findProduct(code) {
  try {
    const response = await axios.get(`https://world.openfoodfacts.org/api/v0/product/${code}.json`)
    const productData = response.data

    if (productData.status === 1) {
      show.value = !show.value
      log(`Produkt hittad: ${productData.product.product_name || 'Namn saknas'}`)
      product.value = `${productData.product.brands}: ${productData.product.product_name}`
    } else {
      log('Produkt hittades inte')
    }
  } catch (error) {
    log(`Fel vid API-förfrågan: ${error.message}`)
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
    resultText.value = `Scannad kod: ${code}`
    log(`Kod upptäckt: ${code}`)
    latestCode.value = code
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

.navbar {
  display: flex;
  list-style: none;
  padding: 0px;
  padding-bottom: 12px;
  margin: 0;
  border-bottom: ridge 1px;
}

.navbar2 {
  display: flex;
  list-style: none;
  padding: 0px;
  padding-bottom: 12px;
  padding-top: 12px;
  margin: 0;
}

.nav-element {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 40px;
  padding: 0 1rem;
}

.nav2-element {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 30px;
  padding: 0 10px;
}

.whole-button {
  background-color: #44c767;
  border-radius: 4px;
  border: 2px solid #18ab29;
  display: inline-block;
  cursor: pointer;
  color: #ffffff;
  font-family: Arial;
  font-size: 17px;
  padding: 19px 76px;
  text-decoration: none;
  text-shadow: 0px 1px 0px #2f6627;
  width: 50%;
}

.whole-button:hover {
  background-color: #5cbf2a;
}

.whole-button:active {
  position: relative;
  top: 1px;
}
</style>
