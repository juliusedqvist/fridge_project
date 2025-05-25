<template>
  <table-component :headers="headers" :data="tableData">
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
  </table-component>
  <div class="form">
    <input type="text" value="Id">
    <button>Delete</button>
  </div>
</template>

<script>
import TableComponent from '~/components/table.vue'
import axios from 'axios'

export default {
  components: {
    TableComponent,
  },
  data() {
    return {
      headers: [
        'Food_Id',
        'Name',
        'Weight (g)',
        'Kcal per 100g',
        'Protein per 100g',
        'Expiration Date',
        'State',
      ],
      tableData: [],
    }
  },
  mounted() {
    this.getContent()
  },
  methods: {
    async getContent() {
      try {
        const response = await axios.get('/api/get_products')
        this.tableData = response.data
      } catch (error) {
        console.error(`Fel vid API-förfrågan: ${error.message}`)
      }
    },
    async deleteProduct(id) {
      try {
        await axios.post('/api/delete_product', { id })
        await this.getContent()
      } catch (error) {
        console.error(`Fel vid borttagning: ${error.message}`)
      }
    },
  },
}
</script>
