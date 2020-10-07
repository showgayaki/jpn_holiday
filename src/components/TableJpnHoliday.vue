<template>
  <div class="holiday-list">
    <h2>日本の祝祭日</h2>
    <el-table class="jpn-holiday"
        :data="holidays"
        :default-sort="{prop: 'date', order: 'ascending'}"
    >
      <!-- <el-table-column prop="id" label="ID" sortable></el-table-column> -->
      <el-table-column prop="date" label="日付" sortable></el-table-column>
      <el-table-column prop="name" label="名前" sortable></el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import axios, { AxiosResponse } from "axios";

// API 実行結果
class JpnHoliday {
  id: number = 0;
  date: string = "";
  name: string = "";
}

export default Vue.extend({
  data(){
    return {
      holidays: [new JpnHoliday()],
    };
  },
  created: async function(){
    const res: AxiosResponse = await axios.get(
        "http://127.0.0.1:8000/api/jpn_holiday/",
    );
    console.log(res.data);
    this.holidays = res.data;
  },
});
</script>

<style scoped>
th.is-leaf{
  padding: 0;
}
.jpn-holiday{
  width: 50%;
  margin-top: 1rem;
  border: 1px solid rgba(0, 0, 0, .2);
}
</style>