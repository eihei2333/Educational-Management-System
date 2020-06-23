<template>
  <div class="app-container">
    <div class="filter-container">

      <el-input v-model="listQueryStudent.xh" placeholder="学号" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilterStudent" />

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilterStudent">
        查询
      </el-button>

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-download" @click="handleClearStudent">
        清空
      </el-button>

    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="listStudent"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @current-change="handleCurrentStudentChange">

      <el-table-column label="学号" prop="xh" align="center" width="150px">
        <template slot-scope="{row}">
          <span>{{ row.xh }}</span>
        </template>
      </el-table-column>
      <el-table-column label="姓名" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.xm }}</span>
        </template>
      </el-table-column>
    </el-table>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreateStudent">
      添加
    </el-button>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleStudentDelete">
      删除
    </el-button>
    <pagination v-show="total>0" :total="total" :page.sync="listQueryStudent.page" :limit.sync="listQueryStudent.limit" @pagination="getStudent" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogStudentFormVisible">
      <el-form ref="dataForm" :rules="rulesStudent" :model="tempStudent" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="学号" prop="xh">
          <el-input v-model="tempStudent.xh" />
        </el-form-item>
        <el-form-item label="姓名" prop="xm">
          <el-input v-model="tempStudent.xm" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogStudentFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="dialogStatus==='student'?createStudent():updateStudent()">
          确认
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
// import { fetchList, fetchPv, createArticle, updateArticle } from '@/api/article'
import waves from '@/directive/waves' // waves directive

import Pagination from '@/components/Pagination' // secondary package based on el-pagination

const terms = [
  "{ key: 'CN', display_name: 'China' }",
  "{ key: 'US', display_name: 'USA' }",
  "{ key: 'JP', display_name: 'Japan' }",
  "{ key: 'EU', display_name: 'Eurozone' }"
]

// arr to obj, such as { CN : "China", US : "USA" }
// const calendarTypeKeyValue = calendarTypeOptions.reduce((acc, cur) => {
//   acc[cur.key] = cur.display_name
//   return acc
// }, {})

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
      currentStudent: null,
      tableKey: 0,
      list: null,
      listClass: null,
      listStudent: null,
      classList: null,
      studentList: null,
      total: 0,
      listLoading: true,
      listQuery: {
        page: 1,
        limit: 20,
        kh: undefined,
        km: undefined,
        xq: undefined
      },
      listQueryClass: {
        page: 1,
        limit: 20,
        kh: undefined,
        gh: undefined,
        xq: undefined
      },
      listQueryStudent: {
        page: 1,
        limit: 20,
        xk: undefined,
        xm: undefined
      },

      terms,
      temp: {
        kh: undefined,
        km: undefined,
        xq: undefined,
        xf: 0,
        xs: 0
      },
      tempClass: {
        gh: undefined,
        sksj: undefined
      },
      tempStudent: {
        xh: undefined
      },
      dialogFormVisible: false,
      dialogClassFormVisible: false,
      dialogStudentFormVisible: false,
      dialogStatus: '',
      textMap: {
        student: '添加学生',
        create: '添加课程',
        class: '添加班级'
      },
      //dialogPvVisible: false,
      rules: {
        kh: [{ required: true, message: '请填写课号', trigger: 'blur' }],
        km: [{ required: true, message: '请填写课名', trigger: 'blur' }],
        xf: [{ required: true, message: '请填写学分', trigger: 'blur' }],
        xs: [{ required: true, message: '请填写学时', trigger: 'blur' }],
        xq: [{ required: true, message: '请填写学期', trigger: 'blur' }]
      },
      rulesClass: {
        gh: [{ required: true, message: '请填写工号', trigger: 'blur' }],
        sksj: [{ required: true, message: '请填写上课时间', trigger: 'blur' }]
      },
      rulesStudent: {
        xh: [{ required: true, message: '请填写学号', trigger: 'blur' }],
        xm: [{ required: true, message: '请填写姓名', trigger: 'blur' }],
      },
      classStatus: false,
      studentStatus: false
    }
  },
  created() {
    this.getList()
  },
  methods: {
    createCourse() {

    },
    updateCourse() {

    },
    createClass() {

    },
    updateClass() {

    },
    createStudent() {

    },
    updateStudent() {

    },
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
    getClass() {

    },
    getStudent() {

    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleClear() {
      this.listQuery = {
        page: 1,
        limit: 20,
        kh: undefined,
        km: undefined,
        xq: undefined
      }
    },

    handleFilterClass() {
      this.listQueryClass.page = 1
      this.getClass()
    },
    handleClearClass() {
      this.listQueryClass = {
        page: 1,
        limit: 20,
        kh: undefined,
        km: undefined,
        xq: undefined
      }
    },
    handleFilterStudent() {
      this.listQueryStudent.page = 1
      this.getStudent()
    },
    handleClearStudent() {
      this.listQueryStudent = {
        page: 1,
        limit: 20,
        xh: undefined,
        xm: undefined
      }
    },
    handleCurrentChange(val) {
      this.currentRow = val
    },

    handleCurrentClassChange(val) {
      this.currentClass = val
    },
    handleCurrentStudentChange(val) {
      this.currentStudent = val
    },

    resetTemp() {
      this.temp = {
        kh: undefined,
        km: undefined,
        xq: undefined,
        xf: 0,
        xs: 0
      }
    },
    resetTempClass() {
      this.tempClass = {
        gh: undefined,
        sksj: undefined
      }
    },
    resetTempStudent() {
      this.tempClass = {
        xh: undefined
      }
    },
    handleCreate() {
      this.resetTemp()
      this.dialogStatus = 'create'
      this.dialogFormVisible = true
      this.$nextTick(() => {
        this.$refs['dataForm'].clearValidate()
      })
    },
    handleCreateClass() {
      this.resetTempClass()
      this.dialogStatus = 'class'
      this.dialogClassFormVisible = true
    },
    handleCreateStudent() {
      this.resetTempStudent()
      this.dialogStatus = 'student'
      this.dialogStudentFormVisible = true
    },
    handleClass() {
      this.classStatus = true
    },
    handleStudent() {
      this.studentStatus = true
    },
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
    handleDelete(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Delete Successfully',
        type: 'success',
        duration: 2000
      })
      this.list.splice(index, 1)
    },

    handleClassDelete(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Delete Successfully',
        type: 'success',
        duration: 2000
      })
      this.list.splice(index, 1)
    },

    handleStudentDelete(row, index) {
      this.$notify({
        title: 'Success',
        message: 'Delete Successfully',
        type: 'success',
        duration: 2000
      })
      this.list.splice(index, 1)
    }
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
