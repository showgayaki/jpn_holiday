<template>
  <div class="holiday-wrap">
    <h2>日本の祝祭日</h2>
    <div class="holiday-filter">
      <p>
        <label class="filter-label" for="date-filter">date</label>
        <el-input id="date-filter" class="filter-text" placeholder="Search Date" v-model="date_search" suffix-icon="search"></el-input>
      </p>
      <p>
        <label class="filter-label" for="name-filter">name</label>
        <el-input id="name-filter" class="filter-text" placeholder="Search Name" v-model="name_search" suffix-icon="search">name</el-input>
      </p>
    </div>
    <div class="api-url-wrap">
      <p class="api-url">API URL:</p>
      <p class="view-url">
        <span>{{ api_url }}</span>
        <span v-if="date_search">{{ date_search.replace(date_search, '?date=' + date_search) }}</span>
        <span v-else-if="name_search">{{ name_search.replace(name_search, '?name=' + name_search) }}</span>
        <span v-if="date_search && name_search">{{ name_search.replace(name_search, '&name=' + name_search) }}</span>
      </p>
    </div>
    <el-table class="holiday-table"
        :data="search_record"
        :default-sort="{prop: 'date', order: 'ascending'}"
    >
      <el-table-column prop="date" label="日付" sortable></el-table-column>
      <el-table-column prop="name" label="名前" sortable></el-table-column>
    </el-table>
  </div>
</template>

<script lang="ts">
import Vue from "vue";
import axios, { AxiosResponse } from "axios";

const API_URL = 'http://127.0.0.1:8000/api/jpn_holiday/';

// API 実行結果
class JpnHoliday {
  date: string = "";
  name: string = "";
}

export default Vue.extend({
  data(){
    return {
      api_url: API_URL,
      holidays: [new JpnHoliday()],
      date_search: '',
      name_search: '',
    };
  },
  created: async function(){
    const res: AxiosResponse = await axios.get(
        API_URL,
    );
    // console.log(res.data);
    this.holidays = res.data;
  },
  computed: {
    search_record(){
      return this.holidays.filter(holiday => {
        if(this.date_search === '' && this.name_search === ''){
          return this.holidays;
        }
        if(this.date_search !== '' && this.name_search !== ''){
          return holiday.date.includes(this.date_search) &&
                  holiday.name.includes(this.name_search);
        }
        if(this.date_search !== ''){
          return holiday.date.includes(this.date_search);
        }
        if(this.name_search !== ''){
          return holiday.name.includes(this.name_search);
        }
      })
    }
  }
});
</script>

<style scoped>
.holiday-filter{
  margin-top: 1rem;
}
.filter-label{
  display: inline-block;
  width: 50px;
}
.filter-text{
  margin-bottom: 1rem;
}
.filter-text{
  width: 300px;
}
.api-url-wrap{
  display: flex;
  flex-wrap: wrap;
  margin: 0.5rem 0;
}
.api-url{
  margin-right: 1rem;
}
.holiday-table{
  border: 1px solid rgba(0, 0, 0, .2);
}
</style>
