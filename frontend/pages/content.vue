<template>
  <table-component :headers="headers" :data="tableData">
    <template #column0="{ entity }">
      {{ entity.Name }}
    </template>
    <template #column1="{ entity }">
      {{ entity.Weight }} g
    </template>
    <template #column2="{ entity }">
      {{ entity.KcalPer100g }} kcal/100g
    </template>
    <template #column3="{ entity }">
      {{ entity.ProteinPer100g }} g
    </template>
    <template #column4="{ entity }">
      {{ new Date(entity.Exp_Date).toLocaleDateString() }}
    </template>
    <template #column5="{ entity }">
      {{ entity.State }}
    </template>
  </table-component>
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
  },
}
</script>
