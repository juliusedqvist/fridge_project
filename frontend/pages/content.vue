<template>
  <TableComponent :headers="headers" :data="tableData">
    <template #column0="{ entity }">
      {{ entity.Food_Id }}
    </template>
    <template #column1="{ entity }">
      {{ entity.Name }}
    </template>
    <template #column2="{ entity }">
      {{ entity.Weight }} g
    </template>
    <template #column3="{ entity }">
      {{ entity.KcalPer100g }} kcal/100g
    </template>
    <template #column4="{ entity }">
      {{ entity.ProteinPer100g }} g
    </template>
    <template #column5="{ entity }">
      {{ new Date(entity.Exp_Date).toLocaleDateString() }}
    </template>
    <template #column6="{ entity }">
      {{ entity.State }}
    </template>
  </TableComponent>

  <div class="form">
    <input type="text" v-model="inputId" />
    <button @click="deleteProduct">Delete</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import TableComponent from '~/components/table.vue'

const headers = [
  'Food_Id',
  'Name',
  'Weight (g)',
  'Kcal per 100g',
  'Protein per 100g',
  'Expiration Date',
  'State',
]

const tableData = ref([])
const inputId = ref('Id')

async function getContent() {
  try {
    const response = await axios.get('/api/get_products')
    tableData.value = response.data
  } catch (error) {
    console.error(`Fel vid API-förfrågan: ${error.message}`)
  }
}

async function deleteProduct() {
  if (!inputId.value || inputId.value === 'Id') {
    alert('Please enter a valid Id')
    return
  }
  try {
    await axios.post('/api/delete_product', { id: inputId.value })
    await getContent()
    inputId.value = 'Id'
  } catch (error) {
    console.error(`Fel vid borttagning: ${error.message}`)
  }
}

onMounted(() => {
  getContent()
})
</script>
