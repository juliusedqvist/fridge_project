<template>
  <div class="content-wrapper">
    <div></div>
    <div>
      <ul class="navbar">
        <li class="nav-element" style="flex-grow: 4">
          Latest scanned code: {{ latestCode }}
        </li>
        <li class="nav-element" style="flex-grow: 1">
          <button @click="findProduct(latestCode)">Get product</button>
        </li>
      </ul>
    </div>
    <div class="navbar2">
      <li class="nav2-element" style="flex-grow: 4">{{ product }}</li>
      <li class="nav2-element" style="flex-grow: 1">
        <button @click="getWeight">scale</button>
      </li>
      <li class="nav2-element" style="flex-grow: 1">{{ weight }}</li>
    </div>
    <p class="whole-button" @click="addToDatabase">Add to database</p>
    <button @click="startButton">{{ show ? 'Hide' : 'Show' }}</button>
    <div v-if="show">
      <div class="scanner-container" ref="scannerContainer"></div>
      <p>{{ resultText }}</p>
      <h2>Loggar</h2>
      <pre class="log-area">{{ logs }}</pre>
    </div>
  </div>
</template>

<script setup>
import { ref, onBeforeUnmount, nextTick } from 'vue'
import Quagga from '@ericblade/quagga2'
import axios from 'axios'

const scannerContainer = ref(null)
const resultText = ref('Ingen streckkod scannad ännu')
const logs = ref('')

const show = ref(false)
const latestCode = ref('')
const product = ref('Produktnamn')
const productFields = ref('')
const weight = ref('N/A')

async function addToDatabase() {
  console.log(productFields.value)
  if (
    productFields.value.exp_date === 0 ||
    productFields.value.exp_date === '0'
  ) {
    const oneWeekLater = new Date()
    oneWeekLater.setDate(oneWeekLater.getDate() + 7)
    productFields.value.exp_date = oneWeekLater.toISOString().split('T')[0] // format: YYYY-MM-DD
  }
  console.log(productFields.value)
  const res = await axios.post('/api/add_product', productFields.value)
  product.value = "";
}

async function getWeight() {
  try {
    const response = await axios.get(`/api/weight`)
    weight.value = `${response.data.weight}`
    productFields.value.weight = parseInt(response.data.weight)
  } catch (error) {
    console.log(`Fel vid API-förfrågan: ${error.message}`)
  }
}

function startButton() {
  show.value = !show.value

  if (show.value) {
    log('Komponenten monterad')
    nextTick(() => {
      startScanner()
    })
  } else {
    Quagga.stop()
    log('Scanner stoppad')
  }
}

async function findProduct(code) {
  try {
    const response = await axios.get(
      `https://world.openfoodfacts.org/api/v0/product/${code}.json`
    )
    const productData = response.data

    if (productData.status === 1) {
      show.value = !show.value
      log(
        `Produkt hittad: ${productData.product.product_name || 'Namn saknas'}`
      )
      product.value = `${productData.product.brands}: ${productData.product.product_name}`
      console.log(productData)

      productFields.value = {
        name: productData.product.product_name,
        weight: 0,
        kcal: productData.product.nutriments['energy-kcal_100g'],
        protein: productData.product.nutriments.proteins_100g,
        exp_date: 0,
      }
    } else {
      log('Produkt hittades inte')
    }
  } catch (error) {
    log(`Fel vid API-förfrågan: ${error.message}`)
  }
}

function log(msg) {
  logs.value += msg + '\n'
  console.log(msg)
}

function startScanner() {
  if (!scannerContainer.value) {
    log('Ingen scannerContainer ref hittad')
    return
  }

  Quagga.init(
    {
      inputStream: {
        type: 'LiveStream',
        constraints: {
          facingMode: 'environment',
        },
        target: scannerContainer.value,
      },
      decoder: {
        readers: ['code_128_reader', 'ean_reader', 'ean_8_reader'],
      },
    },
    (err) => {
      if (err) {
        log(`Init error: ${err}`)
        return
      }
      Quagga.start()
      log('Scanner startad')
    }
  )

  Quagga.onDetected((result) => {
    const code = result.codeResult.code
    resultText.value = `Scannad kod: ${code}`
    log(`Kod upptäckt: ${code}`)
    latestCode.value = code
  })
}

onBeforeUnmount(() => {
  Quagga.stop()
  log('Scanner stoppad')
})
</script>

<style scoped>
.content-wrapper {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 1rem;
  box-sizing: border-box;
  overflow-x: hidden;
}

.navbar {
  display: flex;
  list-style: none;
  padding: 0 0 12px 0;
  margin: 0;
  border-bottom: ridge 1px;
}

.navbar2 {
  display: flex;
  list-style: none;
  padding: 12px 0 12px 0;
  margin: 0;
}

.nav-element {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 40px;
  padding: 0 1rem;
  flex-grow: 1;
  min-width: 0;
  overflow-wrap: break-word;
}

.nav2-element {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  height: 30px;
  padding: 0 10px;
  flex-grow: 1;
  min-width: 0;
  overflow-wrap: break-word;
}

.whole-button {
  background-color: #222;
  border-radius: 6px;
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  color: #fff;
  font-family: Arial, sans-serif;
  font-size: 18px;
  padding: 20px;
  text-decoration: none;
  width: 100%;
  box-sizing: border-box;
  word-wrap: break-word;
  margin-bottom: 1rem;
}

.whole-button:hover {
  background-color: #333;
}

.whole-button:active {
  background-color: #444;
  top: 1px;
}

.scanner-container {
  width: 100%;
  max-width: 300px;
  height: 300px;
  border: 1px solid #ccc;
  margin-bottom: 0.5rem;
}

.log-area {
  background: #f0f0f0;
  padding: 1em;
  height: 150px;
  overflow-y: auto;
  white-space: pre-wrap;
}
</style>
