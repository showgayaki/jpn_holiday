<template>
  <tableJpnHoliday></tableJpnHoliday>
</template>

<script lang="ts">
import Vue from 'vue';
import TableJpnHoliday from '@/components/TableJpnHoliday.vue';

export default Vue.extend({
  components:{
    tableJpnHoliday: TableJpnHoliday,
  }
});
</script>
