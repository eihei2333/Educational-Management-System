<template>
  <div class="app-container">
    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="list"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @current-change="handleCurrentChange"
    >
      <el-table-column label="课号" prop="kh" align="center" width="150px">
        <template slot-scope="{row}">
          <span>{{ row.kh }}</span>
        </template>
      </el-table-column>
      <el-table-column label="课名" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.km }}</span>
        </template>
      </el-table-column>
      <el-table-column label="教师号" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.gh }}</span>
        </template>
      </el-table-column>
      <el-table-column label="教师名" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.mz }}</span>
        </template>
      </el-table-column>
      <el-table-column label="学分" width="80px">
        <template slot-scope="{row}">
          <span>{{ row.xf }}</span>
        </template>
      </el-table-column>
      <el-table-column label="学时" width="80px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.xs }}</span>
        </template>
      </el-table-column>
      <el-table-column label="时间" width="80px">
        <template slot-scope="{row}">
          <span>{{ row.sj }}</span>
        </template>
      </el-table-column>
      <el-table-column label="选课人数" width="80px">
        <template slot-scope="{row}">
          <span>{{ row.rs }}</span>
        </template>
      </el-table-column>
    </el-table>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
      确认
    </el-button>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
  </div>
</template>

<script>
// import { fetchList, fetchPv, createArticle, updateArticle } from '@/api/article'
import waves from '@/directive/waves' // waves directive

import Pagination from '@/components/Pagination' // secondary package based on el-pagination

// arr to obj, such as { CN : "China", US : "USA" }
// const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
//   acc[cur.key] = cur.display_name
//   return acc
// }, {})
const terms = [
  "{ key: 'CN', display_name: 'China' }",
  "{ key: 'US', display_name: 'USA' }",
  "{ key: 'JP', display_name: 'Japan' }",
  "{ key: 'EU', display_name: 'Eurozone' }"
]
export default {
  name: 'ComplexTable',
  components: { Pagination },
  directives: { waves },
  filters: {
    // statusFilter(status) {
    //   const statusMap = {
    //     published: 'success',
    //     draft: 'info',
    //     deleted: 'danger'
    //   }
    //   return statusMap[status]
    // }
    // typeFilter(type) {
    //   return calendarTypeKeyValue[type]
    // }
  },
  data() {
    return {
      currentRow: null,
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        kh: undefined,
        km: undefined,
        gh: undefined
      },
      terms
    }
  },
  created() {
    this.$store.dispatch('user/getTerm').then(response => {
      console.log('terms', response)
      this.terms = response.terms
      this.getList()
    }).catch(() => {
    })
  },
  methods: {
    getList() {
      const data = { xq: this.terms[0], gh: this.listQuery.gh, kh: this.listQuery.kh }
      this.$store.dispatch('student/getSelectedCourse', data).then(response => {
        console.log('terms', response)
        this.list = response
        this.listLoading = false
      }).catch(() => {
      })
    },
    handleCurrentChange(val) {
      this.classStatus = false
      this.currentRow = val
    },
    handleCreate() {
      this.$confirm('确认退这门课吗?', '提示', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(() => {
        const data = { xq: this.terms[0], gh: this.currentRow.gh, kh: this.currentRow.kh }
        this.$store.dispatch('student/delet', data).then(response => {
          console.log('terms', response)
          this.$message(response)
        }).catch(() => {
        })
      }).catch(() => {
        this.$message({
          type: 'info',
          message: '已取消退课'
        })
      })
    }
    // handleUpdate(row) {
    //   this.temp = Object.assign({}, row) // copy obj
    //   this.temp.timestamp = new Date(this.temp.timestamp)
    //   this.dialogStatus = 'update'
    //   this.dialogFormVisible = true
    //   this.$nextTick(() => {
    //     this.$refs['dataForm'].clearValidate()
    //   })
    // },
    // updateData() {
    //   this.$refs['dataForm'].validate((valid) => {
    //     if (valid) {
    //       const tempData = Object.assign({}, this.temp)
    //       tempData.timestamp = +new Date(tempData.timestamp) // change Thu Nov 30 2017 16:41:05 GMT+0800 (CST) to 1512031311464
    //       updateArticle(tempData).then(() => {
    //         const index = this.list.findIndex(v => v.id === this.temp.id)
    //         this.list.splice(index, 1, this.temp)
    //         this.dialogFormVisible = false
    //         this.$notify({
    //           title: 'Success',
    //           message: 'Update Successfully',
    //           type: 'success',
    //           duration: 2000
    //         })
    //       })
    //     }
    //   })
    // },
    // handleFetchPv(pv) {
    //   fetchPv(pv).then(response => {
    //     this.pvData = response.data.pvData
    //     this.dialogPvVisible = true
    //   })
    // },
    // handleDownload() {
    //   this.downloadLoading = true
    //   import('@/vendor/Export2Excel').then(excel => {
    //     const tHeader = ['timestamp', 'title', 'type', 'importance', 'status']
    //     const filterVal = ['timestamp', 'title', 'type', 'importance', 'status']
    //     const data = this.formatJson(filterVal)
    //     excel.export_json_to_excel({
    //       header: tHeader,
    //       data,
    //       filename: 'table-list'
    //     })
    //     this.downloadLoading = false
    //   })
    // },
    // formatJson(filterVal) {
    //   return this.list.map(v => filterVal.map(j => {
    //     if (j === 'timestamp') {
    //       return parseTime(v[j])
    //     } else {
    //       return v[j]
    //     }
    //   }))
    // }
    // getSortClass: function(key) {
    //   const sort = this.listQuery.sort
    //   return sort === `+${key}` ? 'ascending' : 'descending'
    // }
  }
}
</script>
