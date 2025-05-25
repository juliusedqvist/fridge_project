<template>
  <table-component :headers="headers" :data="data">
    <template #column0="{ entity }">
      {{ entity.name }}
    </template>
    <template #column1="{ entity }">
      {{ entity.age }}
    </template>
    <template #column2="{ entity }">
      <ul>
        <li v-for="(hobbie, i) in entity.hobbies" :key="`${hobbie}-${i}`">
          {{ hobbie }}
        </li>
      </ul>
    </template>
  </table-component>
</template>

<script>
import TableComponent from '~/components/table.vue'

export default {
  components: {
    TableComponent,
  },
  data() {
    return {
      headers: ['Name', 'Age', 'Favourite Hobbies'],
      data: [
        {
          name: 'James',
          age: 21,
          hobbies: ['tennis', 'coding'],
        },
        {
          name: 'Carol',
          age: 22,
          hobbies: ['gaming', 'reading', 'debating'],
        },
        {
          name: 'Sam',
          age: 25,
          hobbies: ['brunching', 'going to the gym', 'painting'],
        },
      ],
    }
  },
}
</script>
