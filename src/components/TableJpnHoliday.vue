<template>
  <div class="holiday-wrap">
    <h2>日本の祝日API</h2>
    <div class="holiday-filter">
      <p>
        <label class="filter-label" for="date-filter">date</label>
        <el-input id="date-filter" class="filter-text" placeholder="Search Date" v-model="date_search" suffix-icon="el-icon-search"></el-input>
      </p>
      <p>
        <label class="filter-label" for="name-filter">name</label>
        <el-input id="name-filter" class="filter-text" placeholder="Search Name" v-model="name_search" suffix-icon="el-icon-search">name</el-input>
      </p>
    </div>
    <div class="api-url-wrap">
      <p class="api-url-label">API URL:</p>
      <div class="api-url">
        <el-button type="button" class="btn-copy" icon="el-icon-document-copy" @click="copyToClipboard()"></el-button>
        <p id="view-url" class="view-url">
          <span>{{ api_url }}</span>
          <span v-if="date_search">{{ date_search.replace(date_search, '?date=' + date_search) }}</span>
          <span v-else-if="name_search">{{ name_search.replace(name_search, '?name=' + name_search) }}</span>
          <span v-if="date_search && name_search">{{ name_search.replace(name_search, '&name=' + name_search) }}</span>
        </p>
      </div>
    </div>
    <p class="record-count">レコード件数:{{ search_record.length }}</p>
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
import Vue, { PropType } from "vue";
import axios from "axios";

const API_URL: string = process.env.VUE_APP_API_URL;

// API 実行結果
class JpnHoliday {
  date: string = "";
  name: string = "";
}

export default Vue.extend({
  data(){
    return {
      api_url: API_URL,
      holidays: [new JpnHoliday],
      date_search: '',
      name_search: '',
    };
  },
  created: async function(){
    await axios.get(this.api_url)
      .then(res =>{
        this.holidays = res.data;
      })
      .catch(error => {
        console.log(error);
      })
  },
  computed: {
    search_record(): JpnHoliday[]{
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
  },
  methods:{
    copyToClipboard(){
      const copyText: string | null = this.$el.querySelector('#view-url')!.textContent;
      if(copyText){
        navigator.clipboard
          .writeText(copyText)
          .then(() => {
            console.log('Copy Succeeded.');
          })
          .catch(e => {
            console.log(e);
          })
      }
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
  line-height: 1rem;
}
.api-url-label{
  width: 72px;
  padding-top: 0.4rem;
}
.api-url{
  display: flex;
}
button.btn-copy{
  padding: 0 0.4rem;
  background-color: #fff;
  border: 1px solid rgba(0, 0, 0, .2);
  border-right: 0;
  border-radius: 3px 0 0 3px;
  cursor: pointer;
}
.view-url{
  width: calc(100vw - (159px + 0.8rem));
  padding: 0.4rem;
  border: 1px solid rgba(0, 0, 0, .2);
  border-radius: 0 3px 3px 0;
  white-space: nowrap;
  overflow-x: auto;
}
.holiday-table{
  border: 1px solid rgba(0, 0, 0, .2);
}
</style>
