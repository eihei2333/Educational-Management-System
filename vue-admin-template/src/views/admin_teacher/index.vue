<template>
  <div class="app-container">
    <div class="filter-container">

      <el-input v-model="listQueryTeacher.gh" placeholder="工号" style="width: 200px;" class="filter-item" @keyup.enter.native="handleFilterTeacher" />

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
          this.$store.dispatch('admin/creatTeacher', this.tempTeacher).then(response => {
            this.$message(response)
          }).catch(() => {
          })
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
      this.$store.dispatch('admin/getAllTeacher', this.listQueryTeacher).then(response => {
        this.listTeacher = response
        this.listLoading = false
      }).catch(() => {
      })
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

    handleTeacherDelete(row, index) {
      const data = { gh: this.currentTeacher.gh }
      this.$store.dispatch('admin/deleteTeacher', data).then(response => {
        this.$message(response)
      }).catch(() => {
      })
    }
  }
}
</script>
