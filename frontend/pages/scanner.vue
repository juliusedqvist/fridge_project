<template>
  <div class="content-wrapper">
    <div></div>
    <div>
      <ul class="navbar">
        <li class="nav-element" style="flex-grow: 7">
          Latest scanned code: {{ latestCode }}
        </li>
        <li class="nav-element" style="flex-grow: 1">
          <button class="small-button" @click="findProduct(latestCode)">Get product</button>
        </li>
        <li class="nav-element" style="flex-grow: 1">
          <button class="small-button" @click="getWeight">scale</button>
        </li>
      </ul>
    </div>
    <div class="navbar2">
      <li class="nav2-element" style="flex-grow: 4">{{ product }}</li>
      <li class="nav2-element" style="flex-grow: 1">{{ weight }}</li>
    </div>
    <p class="show-button" @click="addToDatabase">Add to database</p>
    <button class="show-button" @click="startButton">{{ show ? 'Hide' : 'Show' }}</button>
    <div v-if="show" class="scanner-section">
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
  if (
    productFields.value.exp_date === 0 ||
    productFields.value.exp_date === '0'
  ) {
    const oneWeekLater = new Date()
    oneWeekLater.setDate(oneWeekLater.getDate() + 7)
    productFields.value.exp_date = oneWeekLater.toISOString().split('T')[0]
  }

  await axios.post('/api/add_product', productFields.value)
  product.value = ''
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
  padding: 1rem;
  box-sizing: border-box;
  overflow-x: hidden;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
}

.navbar {
  display: flex;
  list-style: none;
  padding: 0 0 16px 0;
  margin: 0;
  border-bottom: ridge 1px;
  height: 70px;
}

.navbar2 {
  display: flex;
  list-style: none;
  padding: 12px 0;
  margin: 0;
}

.nav-element {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 0 1rem;
  flex-grow: 1;
  min-width: 0;
  overflow-wrap: break-word;
  height: 100%;
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

/* Style for the "Show"/"Hide" button to match .whole-button */
.show-button {
  background-color: #222;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  color: #fff;
  font-family: Arial, sans-serif;
  font-size: 18px;
  padding: 16px;
  width: 100%;
  box-sizing: border-box;
  text-align: center;
  margin-bottom: 1rem;
  transition: background-color 0.2s ease;
}

.show-button:hover {
  background-color: #333;
}

.show-button:active {
  background-color: #444;
  top: 1px;
  position: relative;
}

/* Shared style for small buttons "Get product" and "scale" */
.small-button {
  background-color: #222;
  border-radius: 6px;
  border: none;
  cursor: pointer;
  color: #fff;
  font-family: Arial, sans-serif;
  font-size: 14px;
  padding: 8px 0;
  width: 140px;
  height: 50px;
  box-sizing: border-box;
  text-align: center;
  transition: background-color 0.2s ease;
}

.small-button:hover {
  background-color: #333;
}

.small-button:active {
  background-color: #444;
  top: 1px;
  position: relative;
}

.scanner-section {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  width: 100%;
  box-sizing: border-box;
  overflow: hidden;
}

.scanner-container {
  width: 100%;
  max-width: 400px;
  height: 400px;
  border: 1px solid #ccc;
  box-sizing: border-box;
  overflow: hidden;
}

.log-area {
  background: #f0f0f0;
  padding: 1em;
  height: 150px;
  overflow-y: auto;
  white-space: pre-wrap;
  width: 100%;
  max-width: 600px;
}

@media (max-width: 600px) {
  .scanner-container {
    height: 400px;
    max-width: 100%;
  }

  .small-button {
    width: 180px;
  }
}
</style>
