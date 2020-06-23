<template>
  <div class="app-container">
    <div class="filter-container">

      <el-input v-model="listQueryTeacher.xh" placeholder="工号" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilterTeacher" />

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilterTeacher">
        查询
      </el-button>

      <el-button v-waves class="filter-item" type="primary" icon="el-icon-download" @click="handleClearTeacher">
        清空
      </el-button>

    </div>

    <el-table
      :key="tableKey"
      v-loading="listLoading"
      :data="listTeacher"
      border
      fit
      highlight-current-row
      style="width: 100%;"
      @current-change="handleCurrentTeacherChange">
      <el-table-column label="工号" prop="gh" align="center" width="150px">
        <template slot-scope="{row}">
          <span>{{ row.gh }}</span>
        </template>
      </el-table-column>
      <el-table-column label="姓名" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.xm }}</span>
        </template>
      </el-table-column>
      <el-table-column label="院系" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.yx }}</span>
        </template>
      </el-table-column>
    </el-table>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreateTeacher">
      添加
    </el-button>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleTeacherDelete">
      删除
    </el-button>
    <pagination v-show="total>0" :total="total" :page.sync="listQueryTeacher.page" :limit.sync="listQueryTeacher.limit" @pagination="getTeacher" />

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogTeacherFormVisible">
      <el-form ref="TeacherForm" :rules="rulesTeacher" :model="tempTeacher" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="工号" prop="gh">
          <el-input v-model="tempTeacher.gh" />
        </el-form-item>
        <el-form-item label="姓名" prop="xm">
          <el-input v-model="tempTeacher.xm" />
        </el-form-item>
        <el-form-item label="院系号" prop="yxh">
          <el-input v-model="tempTeacher.yxh" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogTeacherFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="createTeacher()">
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
      currentTeacher: null,
      tableKey: 0,
      listTeacher: null,
      teacherList: null,
      total: 0,
      listLoading: true,
      listQueryTeacher: {
        page: 1,
        limit: 20,
        gh: undefined,
        xm: undefined
      },
      tempTeacher: {
        gh: undefined,
        xm: undefined,
        yxh: undefined
      },

      dialogTeacherFormVisible: false,
      dialogStatus: '',
      textMap: {
        teacher: '添加教师'
      },
      rulesTeacher: {
        gh: [{ required: true, message: '请填写工号', trigger: 'blur' }],
        xm: [{ required: true, message: '请填写姓名', trigger: 'blur' }],
        yxh: [{ required: true, message: '请填写院系号', trigger: 'blur' }]
      }
    }
  },
  created() {
    this.getTeacher()
  },
  methods: {
    createTeacher() {
      this.$refs['TeacherForm'].validate((valid) => {
        if (valid) {
          // this.temp.id = parseInt(Math.random() * 100) + 1024 // mock a id
          // this.temp.author = 'vue-element-admin'
          // createArticle(this.temp).then(() => {
          //   this.list.unshift(this.temp)
          //   this.dialogFormVisible = false
          //   this.$notify({
          //     title: 'Success',
          //     message: 'Created Successfully',
          //     type: 'success',
          //     duration: 2000
          //   })
          // })
        }
      })
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
    getTeacher() {

    },
    handleFilterTeacher() {
      this.listQueryTeacher.page = 1
      this.getTeacher()
    },
    handleClearTeacher() {
      this.listQueryTeacher = {
        page: 1,
        limit: 20,
        xh: undefined,
        xm: undefined
      }
    },
    handleCurrentTeacherChange(val) {
      this.currentTeacher = val
    },

    resetTempTeacher() {
      this.tempClass = {
        xh: undefined
      }
    },
    handleCreateTeacher() {
      this.resetTempTeacher()
      this.dialogStatus = 'teacher'
      this.dialogTeacherFormVisible = true
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

    handleTeacherDelete(row, index) {
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
