<template>
  <table-component :headers="headers" :data="data">
    <template #column0="{ entity }">
      {{ entity.name }}
    </template>
    <template #column1="{ entity }">
      {{ entity.age }}
    </template>
    <template #column2="{ entity }">
      <li v-for="(hobbie, i) in entity.hobbies" :key="`${hobbie}-${i}`">
        {{ hobbie }}
      </li>
    </template>
  </table-component>
</template>

<script lang="ts">
import Vue from 'vue'
import TableComponent from '~/components/Table.vue'

export default Vue.extend({
  components: {
    TableComponent
  },

  data: () => ({
    headers: [
      'Name',
      'Age',
      'Favourite Hobbies'
    ],
    data: [
      {
        name: 'James',
        age: 21,
        hobbies: ['tennis', 'coding']
      },
      {
        name: 'Carol',
        age: 22,
        hobbies: ['gaming', 'reading', 'debating']
      },
      {
        name: 'Sam',
        age: 25,
        hobbies: ['brunching', 'going to the gym', 'painting']
      },
    ],
  })
})

</script>
