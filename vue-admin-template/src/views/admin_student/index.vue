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
      <el-table-column label="院系" width="150px" align="center">
        <template slot-scope="{row}">
          <span>{{ row.yx }}</span>
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
      <el-form ref="tempStudent" :rules="rulesStudent" :model="tempStudent" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="学号" prop="xh">
          <el-input v-model="tempStudent.xh" />
        </el-form-item>
        <el-form-item label="姓名" prop="xm">
          <el-input v-model="tempStudent.xm" />
        </el-form-item>
        <el-form-item label="院系号" prop="yxh">
          <el-input v-model="tempStudent.yxh" />
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
      listStudent: null,
      studentList: null,
      total: 0,
      listLoading: true,
      listQueryStudent: {
        page: 1,
        limit: 20,
        xh: undefined,
        xm: undefined
      },

      terms,

      tempStudent: {
        xh: undefined,
        xm: undefined,
        yxh: undefined
      },
      dialogStudentFormVisible: false,
      dialogStatus: '',
      textMap: {
        student: '添加学生'
      },
      rulesStudent: {
        xh: [{ required: true, message: '请填写学号', trigger: 'blur' }],
        xm: [{ required: true, message: '请填写姓名', trigger: 'blur' }],
        yxh: [{ required: true, message: '请填写院系号', trigger: 'blur' }]
      }
    }
  },
  created() {
    this.getStudent()
  },
  methods: {
    createStudent() {
      this.$refs['tempStudent'].validate((valid) => {
        if (valid) {
          this.$store.dispatch('admin/creatStudent', this.tempStudent).then(response => {
            this.$message(response)
          }).catch(() => {
          })
        }
      })
    },
    getStudent() {
      this.$store.dispatch('admin/getAllStudent', this.listQueryStudent).then(response => {
        this.listStudent = response
        this.listLoading = false
      }).catch(() => {
      })
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
    handleCurrentStudentChange(val) {
      this.currentStudent = val
    },

    resetTempStudent() {
      this.tempClass = {
        xh: undefined
      }
    },
    handleCreateStudent() {
      this.resetTempStudent()
      this.dialogStatus = 'student'
      this.dialogStudentFormVisible = true
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

    handleStudentDelete(row, index) {
      const data = { xh: this.currentStudent.xh }
      this.$store.dispatch('admin/deleteStudent', data).then(response => {
        this.$message(response)
      }).catch(() => {
      })
    }
  }
}
</script>
