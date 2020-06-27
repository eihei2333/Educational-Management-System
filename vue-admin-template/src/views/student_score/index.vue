<template>
  <div class="app-container">
    <el-form ref="TermForm" :model="currentTerm" label-width="200px" :rules="rules">
      <el-form-item label="设置当前学期" prop="term">
        <el-select v-model="currentTerm.term" placeholder="请选择当前学期">
          <el-option v-for="item in terms" :key="item" :label="item" :value="item" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmitTerm()">确定</el-button>
      </el-form-item>
    </el-form>

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
      <el-table-column label="总评成绩" width="80px">
        <template slot-scope="{row}">
          <span>{{ row.zpcj }}</span>
        </template>
      </el-table-column>
    </el-table>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />
    <ve-bar v-if="chartStatus" :data="chartData" :extend="extend"></ve-bar>
  </div>

</template>

<script>
// import { fetchList, fetchPv, createArticle, updateArticle } from '@/api/article'
import waves from '@/directive/waves' // waves directive
import Pagination from '@/components/Pagination' // secondary package based on el-pagination
import VeBar from 'v-charts/lib/bar'

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
  components: { Pagination, VeBar },
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
    this.extend = {
      series: {
        label: {
          normal: {
            show: true
          }
        }
      }
    }
    return {
      currentRow: null,
      currentTerm: {
        term: undefined
      },
      terms,
      tableKey: 0,
      list: null,
      total: 0,
      listLoading: true,
      chartStatus: false,
      listQuery: {
        page: 1,
        limit: 20,
        kh: undefined,
        km: undefined,
        gh: undefined
      },
      chartData: {
        columns: ['课名', '平时成绩', '考试成绩', '总评成绩'],
        rows: [
          { '课名': '1/1', '平时成绩': 1393, '考试成绩': 1093, '总评成绩': 0.32 },
          { '课名': '1/2', '平时成绩': 3530, '考试成绩': 3230, '总评成绩': 0.26 },
          { '课名': '1/3', '平时成绩': 2923, '考试成绩': 2623, '总评成绩': 0.76 },
          { '课名': '1/4', '平时成绩': 1723, '考试成绩': 1423, '总评成绩': 0.49 },
          { '课名': '1/5', '平时成绩': 3792, '考试成绩': 3492, '总评成绩': 0.323 },
          { '课名': '1/6', '平时成绩': 4593, '考试成绩': 4293, '总评成绩': 0.78 }
        ]
      }
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
      // this.listLoading = true
      // fetchList(this.listQuery).then(response => {
      //   this.list = response.data.items
      //   this.total = response.data.total
      //
      //   // Just to simulate the time of the request
      //   setTimeout(() => {
      //     this.listLoading = false
      //   }, 1.5 * 1000)
      // })
    },
    onSubmitTerm() {
      const data = { xq: this.currentTerm.term }
      this.$store.dispatch('student/getScore', data).then(response => {
        this.list = response.list
        this.listLoading = false
        this.chartData.rows = response.rows
        console.log(response)
        this.chartStatus = true
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
        this.$message({
          type: 'success',
          message: '退课成功!'
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
