<template>
  <div class="app-container">
    <div class="filter-container">
      <el-input v-model="listQuery.kh" placeholder="课号" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-input v-model="listQuery.km" placeholder="课名" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilter" />
      <el-select v-model="listQuery.xq" placeholder="学期" clearable style="width: 200px" class="filter-item">
        <el-option v-for="item in terms" :key="item" :label="item" :value="item" />
      </el-select>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter">
        查询
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilter1">
        查询全部
      </el-button>
      <el-button v-waves class="filter-item" type="primary" icon="el-icon-download" @click="handleClear">
        清空
      </el-button>
    </div>

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
      <el-table-column label="开设院系" width="80px">
        <template slot-scope="{row}">
          <span>{{ row.mc }}</span>
        </template>
      </el-table-column>
    </el-table>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreate">
      添加
    </el-button>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleClass">
      查看
    </el-button>
    <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleDelete">
      删除
    </el-button>
    <pagination v-show="total>0" :total="total" :page.sync="listQuery.page" :limit.sync="listQuery.limit" @pagination="getList" />

    <p />
    <div v-if="classStatus">
      <div class="filter-container">

        <el-input v-model="listQueryClass.gh" placeholder="教师号" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilterClass" />

        <el-button v-waves class="filter-item" type="primary" icon="el-icon-search" @click="handleFilterClass">
          查询
        </el-button>

        <el-button v-waves class="filter-item" type="primary" icon="el-icon-download" @click="handleClearClass">
          清空
        </el-button>

      </div>

      <el-table
        :key="tableKey"
        v-loading="listLoading"
        :data="listClass"
        border
        fit
        highlight-current-row
        style="width: 100%;"
        @current-change="handleCurrentClassChange"
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
        <el-table-column label="教师号" width="80px">
          <template slot-scope="{row}">
            <span>{{ row.gh }}</span>
          </template>
        </el-table-column>
        <el-table-column label="上课时间" width="80px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.sksj }}</span>
          </template>
        </el-table-column>
        <el-table-column label="选课人数" width="150px">
          <template slot-scope="{row}">
            <span>{{ row.rs }}</span>
          </template>
        </el-table-column>
      </el-table>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleCreateClass">
        添加
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleStudent">
        查看
      </el-button>
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleClassDelete">
        删除
      </el-button>
      <pagination v-show="total>0" :total="total" :page.sync="listQueryClass.page" :limit.sync="listQueryClass.limit" @pagination="getClass" />
    </div>
    <p />
    <div v-if="studentStatus">
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
        @current-change="handleCurrentStudentChange"
      >

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
    </div>
    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogFormVisible">
      <el-form ref="CourseForm" :rules="rules" :model="temp" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="课号" prop="kh">
          <el-input v-model="temp.kh" />
        </el-form-item>
        <el-form-item label="课名" prop="km">
          <el-input v-model="temp.km" />
        </el-form-item>
        <el-form-item label="学期" prop="xq">
          <el-select v-model="temp.xq" class="filter-item" placeholder="请选择开设学期">
            <el-option v-for="item in terms" :key="item" :label="item" :value="item" />
          </el-select>
        </el-form-item>
        <el-form-item label="学分" prop="xf">
          <el-input v-model="temp.xf" placeholder="请输入学分" />
        </el-form-item>
        <el-form-item label="学时" prop="xs">
          <el-input v-model="temp.xs" />
        </el-form-item>
        <el-form-item label="开设院系" prop="yx">
          <el-input v-model="temp.yx" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="createCourse()">
          确认
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogClassFormVisible">
      <el-form ref="ClassForm" :rules="rulesClass" :model="tempClass" label-position="left" label-width="100px" style="width: 400px; margin-left:50px;">
        <el-form-item label="工号" prop="gh">
          <el-input v-model="tempClass.gh" />
        </el-form-item>
        <el-form-item label="上课时间" prop="sksj">
          <el-input v-model="tempClass.sksj" placeholder="例：三1-2" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogClassFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="createClass()">
          确认
        </el-button>
      </div>
    </el-dialog>

    <el-dialog :title="textMap[dialogStatus]" :visible.sync="dialogStudentFormVisible">
      <el-form ref="StudentForm" :rules="rulesStudent" :model="tempStudent" label-position="left" label-width="70px" style="width: 400px; margin-left:50px;">
        <el-form-item label="学号" prop="xh">
          <el-input v-model="tempStudent.xh" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogStudentFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="createStudent()">
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
    statusFilter(status) {
      const statusMap = {
        published: 'success',
        draft: 'info',
        deleted: 'danger'
      }
      return statusMap[status]
    }
    // typeFilter(type) {
    //   return calendarTypeKeyValue[type]
    // }
  },
  data() {
    return {
      currentRow: null,
      currentClass: null,
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
        xf: undefined,
        xs: undefined,
        yx: undefined
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
      rules: {
        kh: [{ required: true, message: '请填写课号', trigger: 'blur' }],
        km: [{ required: true, message: '请填写课名', trigger: 'blur' }],
        xf: [{ required: true, message: '请填写学分', trigger: 'blur' }],
        xs: [{ required: true, message: '请填写学时', trigger: 'blur' }],
        xq: [{ required: true, message: '请填写学期', trigger: 'blur' }],
        ys: [{ required: true, message: '请填写院系', trigger: 'blur' }]
      },
      rulesClass: {
        gh: [{ required: true, message: '请填写工号', trigger: 'blur' }],
        sksj: [{ required: true, message: '请填写上课时间', trigger: 'blur' }]
      },
      rulesStudent: {
        xh: [{ required: true, message: '请填写学号', trigger: 'blur' }]
      },
      classStatus: false,
      studentStatus: false
    }
  },
  created: function() {
    this.$store.dispatch('user/getTerm').then(response => {
      this.terms = response.terms
      this.$store.dispatch('admin/getAllCourse', this.listQuery).then(response => {
        this.list = response
        this.listLoading = false
      }).catch(() => {
      })
    }).catch(() => {
    })
  },
  methods: {
    handleFilter1() {
      this.listQuery.page = 1
      this.$store.dispatch('admin/getAllCourse', this.listQuery).then(response => {
        this.list = response
        this.listLoading = false
      }).catch(() => {
      })
    },
    createCourse() {
      this.$refs['CourseForm'].validate((valid) => {
        if (valid) {
          this.$store.dispatch('admin/createCourse', this.temp).then(response => {
            this.$message(response)
          }).catch(() => {
          })
        }
      })
    },

    createClass() {
      this.$refs['ClassForm'].validate((valid) => {
        if (valid) {
          const data = { kh: this.currentRow.kh, xq: this.listQuery.xq, gh: this.tempClass.gh, sksj: this.tempClass.sksj }
          this.$store.dispatch('admin/createClass', data).then(response => {
            this.$message(response)
          }).catch(() => {
          })
        }
      })
    },

    createStudent() {
      this.$refs['StudentForm'].validate((valid) => {
        if (valid) {
          const data = { kh: this.currentClass.kh, xq: this.listQuery.xq, gh: this.currentClass.gh, xh: this.tempStudent.xh }
          this.$store.dispatch('admin/createStudentInClass', data).then(response => {
            this.$message(response)
          }).catch(() => {
          })
        }
      })
    },
    getList() {
      this.$store.dispatch('admin/getCourseByTerm', this.listQuery).then(response => {
        this.list = response
        this.listLoading = false
      }).catch(() => {
      })
    },
    getClass() {
      this.$store.dispatch('admin/getClass', this.currentRow, this.listQuery.xq).then(response => {
        this.listClass = response
        console.log(this.list)
      }).catch(() => {
      })
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
      this.classStatus = true
      console.log('Row', this.currentRow)
      const data = { kh: this.currentRow.kh, xq: this.listQuery.xq, gh: this.listQueryClass.gh }
      this.$store.dispatch('admin/getClass', data).then(response => {
        this.listClass = response
      }).catch(() => {
      })
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
      this.studentStatus = true
      console.log('Row', this.currentClass)
      const data = { kh: this.currentClass.kh, xq: this.listQuery.xq, gh: this.currentClass.gh, xh: this.listQueryStudent.xh }
      this.$store.dispatch('admin/getStudent', data).then(response => {
        this.listStudent = response
      }).catch(() => {
      })
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
      this.classStatus = false
      this.currentRow = val
    },

    handleCurrentClassChange(val) {
      this.studentStatus = false
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
      console.log('Row', this.currentRow)
      const data = { kh: this.currentRow.kh, xq: this.listQuery.xq }
      this.$store.dispatch('admin/getClass', data).then(response => {
        this.listClass = response
      }).catch(() => {
      })
    },
    handleStudent() {
      this.studentStatus = true
      console.log('Row', this.currentClass)
      const data = { kh: this.currentClass.kh, xq: this.listQuery.xq, gh: this.currentClass.gh }
      this.$store.dispatch('admin/getStudent', data).then(response => {
        this.listStudent = response
      }).catch(() => {
      })
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
      console.log('Row', this.currentClass)
      const data = { kh: this.currentRow.kh }
      this.$store.dispatch('admin/deletCourse', data).then(response => {
        this.$message(response)
      }).catch(() => {
      })
      // this.list.splice(index, 1)
    },

    handleClassDelete(row, index) {
      const data = { kh: this.currentClass.kh, xq: this.listQuery.xq, gh: this.currentClass.gh, sksj: this.currentClass.sksj }
      this.$store.dispatch('admin/deletClass', data).then(response => {
        this.$message(response)
      }).catch(() => {
      })
    },

    handleStudentDelete(row, index) {
      const data = { kh: this.currentClass.kh, xq: this.listQuery.xq, gh: this.currentClass.gh, xh: this.currentStudent.xh }
      this.$store.dispatch('admin/deletStudentFromClass', data).then(response => {
        this.$message(response)
      }).catch(() => {
      })
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
