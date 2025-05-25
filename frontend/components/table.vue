<template>
  <div class="table-wrapper">
    <table class="present-data">
      <thead>
        <tr>
          <th v-for="(header, i) in headers" :key="`header-${i}`" class="header-item">
            {{ header }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="entity in data" :key="`entity-${entity.name}`" class="table-rows">
          <td v-for="(header, i) in headers" :key="`cell-${entity.name}-${i}`">
            <slot :name="`column${i}`" :entity="entity" />
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: 'TableComponent',
  props: {
    headers: {
      type: Array,
      required: true,
    },
    data: {
      type: Array,
      required: true,
    },
  },
}
</script>
