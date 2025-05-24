<template>
  <div class="page-container">
    <div>
    </div>
    <div>
      <ul class="navbar">
        <li class="nav-element" style="flex-grow: 1;">Latest scanned code: {{ latestCode }}</li>
        <li class="nav-element" style="width: 120px;">
          <button @click="findProduct(latestCode)">Get product</button>
        </li>
      </ul>
    </div>
    <div class="navbar2">
      <li class="nav2-element" style="flex-grow: 1;">{{ product }}</li>
      <li class="nav2-element">
        <button @click="getWeight">scale</button>
      </li>
      <li class="nav2-element">{{ weight }}</li>
    </div>

    <p class="whole-button" @click="addToDatabase">Add to database</p>

    <button class="toggle-button" @click="startButton">
      {{ show ? "Hide" : "Show" }}
    </button>

    <div v-if="show" class="scanner-wrapper">
      <div class="scanner-container" ref="scannerContainer"></div>
      <p>{{ resultText }}</p>
      <h2>Loggar</h2>
      <pre class="log-box">{{ logs }}</pre>
    </div>
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
const productFields = ref('')
const weight = ref('N/A');

async function addToDatabase() {
  console.log(productFields.value);
  if (productFields.value.exp_date === 0 || productFields.value.exp_date === "0") {
    const oneWeekLater = new Date();
    oneWeekLater.setDate(oneWeekLater.getDate() + 7);
    productFields.value.exp_date = oneWeekLater.toISOString().split('T')[0]; // format: YYYY-MM-DD
  }
  console.log(productFields.value)
  const res = await axios.post('/api/add_product', productFields.value);
}

async function getWeight() {
  try {
    const response = await axios.get(`/api/weight`);
    weight.value = `${response.data.weight}`;
    productFields.value.weight = parseInt(response.data.weight);


  } catch (error) {
    console.log(`Fel vid API-förfrågan: ${error.message}`);
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
      console.log(productData);

      // name, weight kcal/100, protein/100, expiration date

      productFields.value = {
        name: productData.product.product_name,
        weight: 0,
        kcal: productData.product.nutriments["energy-kcal_100g"],
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
.page-container {
  max-width: 900px;
  /* matches content wrapper max width */
  margin: 0 auto;
  padding: 2rem 1rem;
  background: white;
  border-radius: 8px;
  min-height: 100vh;
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
  box-sizing: border-box;
  display: flex;
  flex-direction: column;
}

/* Navbars */
.navbar,
.navbar2 {
  display: flex;
  list-style: none;
  padding: 0;
  margin: 0 0 1rem 0;
  border-bottom: 1px solid #ccc;
  align-items: center;
}

.navbar2 {
  border-bottom: none;
  padding-top: 0.5rem;
  margin-bottom: 1.5rem;
}

.nav-element,
.nav2-element {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  padding: 0 1rem;
  height: 40px;
  font-size: 1rem;
  color: #333;
}

/* Let first nav elements take all available space */
.nav-element[style*="flex-grow: 1"],
.nav2-element[style*="flex-grow: 1"] {
  flex-grow: 1;
}

/* Buttons inside navbar */
.navbar button,
.navbar2 button {
  padding: 6px 12px;
  font-size: 1rem;
  cursor: pointer;
  border: 1px solid #999;
  border-radius: 4px;
  background-color: #fff;
  transition: background-color 0.3s ease;
}

.navbar button:hover,
.navbar2 button:hover {
  background-color: #eee;
}

/* Add to database button */
.whole-button {
  background-color: #222;
  border-radius: 6px;
  border: none;
  display: block;
  cursor: pointer;
  color: #fff;
  font-family: Arial, sans-serif;
  font-size: 18px;
  padding: 15px 0;
  text-align: center;
  width: 100%;
  /* full width inside container */
  max-width: 100%;
  /* never overflow */
  box-sizing: border-box;
  margin-bottom: 1.5rem;
  user-select: none;
  transition: background-color 0.3s ease;
}

.whole-button:hover {
  background-color: #333;
}

.whole-button:active {
  background-color: #444;
  position: relative;
  top: 1px;
}

/* Show/Hide toggle button */
.toggle-button {
  padding: 10px 16px;
  margin-bottom: 1.5rem;
  font-size: 1rem;
  cursor: pointer;
  border: 1px solid #999;
  border-radius: 4px;
  background-color: #fff;
  transition: background-color 0.3s ease;
}

.toggle-button:hover {
  background-color: #eee;
}

/* Scanner container and logs */
.scanner-wrapper {
  width: 100%;
  max-width: 300px;
  margin-bottom: 1.5rem;
}

.scanner-container {
  width: 100%;
  height: 300px;
  border: 1px solid #ccc;
  margin-bottom: 0.5rem;
}

.log-box {
  background: #f0f0f0;
  padding: 1em;
  height: 150px;
  overflow-y: auto;
  font-family: monospace;
  white-space: pre-wrap;
  border-radius: 4px;
  box-sizing: border-box;
}
</style>
