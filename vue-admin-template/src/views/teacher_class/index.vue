<template>
  <div class="app-container">
    <el-form ref="TermForm" :model="currentTerm" label-width="200px" :rules="rules">
      <el-form-item label="设置选择学期" prop="term">
        <el-select v-model="currentTerm.term" placeholder="请选择当前学期">
          <el-option v-for="item in terms" :key="item" :label="item" :value="item" />
        </el-select>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmitTerm()">确定</el-button>
      </el-form-item>
    </el-form>

    <div v-if="classStatus">
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
      <el-button class="filter-item" style="margin-left: 10px;" type="primary" icon="el-icon-edit" @click="handleStudent">
        查看名单
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

      </div>

      <el-table
        :key="tableKey"
        v-loading="listLoading"
        :data="listStudent"
        border
        fit
        highlight-current-row
        style="width: 100%;"
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
        <el-table-column label="平时成绩" width="150px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.pscj }}</span>
          </template>
        </el-table-column>
        <el-table-column label="考试成绩" width="150px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.kscj }}</span>
          </template>
        </el-table-column>
        <el-table-column label="总评成绩" width="150px" align="center">
          <template slot-scope="{row}">
            <span>{{ row.zpcj }}</span>
          </template>
        </el-table-column>
        <el-table-column label="操作" align="center" width="230" class-name="small-padding fixed-width">
          <template slot-scope="{row}">
            <el-button type="primary" size="mini" @click="handleUpdate(row)">
              登记成绩
            </el-button>
          </template>
        </el-table-column>
      </el-table>
      <pagination v-show="total>0" :total="total" :page.sync="listQueryStudent.page" :limit.sync="listQueryStudent.limit" @pagination="getStudent" />
    </div>
    <!--    <el-button type="primary" size="mini" @click="handleUpdate()">-->
    <!--      登记成绩-->
    <!--    </el-button>-->
    <ve-pie v-if="studentStatus" :data="chartData" />
    <el-dialog :title="登记成绩" :visible.sync="dialogClassFormVisible">
      <el-form ref="ClassForm" :rules="rulesClass" :model="tempClass" label-position="left" label-width="100px" style="width: 400px; margin-left:50px;">
        <el-form-item label="平时成绩" prop="pscj">
          <el-input v-model="tempClass.pscj" />
        </el-form-item>
        <el-form-item label="考试成绩" prop="kscj">
          <el-input v-model="tempClass.kscj" />
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogClassFormVisible = false">
          取消
        </el-button>
        <el-button type="primary" @click="handleUpdate1">
          确认
        </el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import VePie from 'v-charts/lib/pie.common'
import Pagination from '@/components/Pagination/index'
import waves from '@/directive/waves'

const terms = [
  "{ key: 'CN', display_name: 'China' }",
  "{ key: 'US', display_name: 'USA' }",
  "{ key: 'JP', display_name: 'Japan' }",
  "{ key: 'EU', display_name: 'Eurozone' }"
]

export default {
  components: { Pagination, VePie },
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
      listQueryClass: {
        page: 1,
        limit: 20,
        kh: undefined,
        gh: undefined,
        xq: undefined
      },
      chartData: {
        columns: ['分段', '人数'],
        rows: [
          { '分段': '优', '人数': 0 },
          { '分段': '良', '人数': 0 },
          { '分段': '及格', '人数': 0 },
          { '分段': '失败', '人数': 0 }
        ]
      },
      currentTerm: {
        term: undefined
      },
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
      listQueryStudent: {
        page: 1,
        limit: 20,
        xk: undefined
      },

      terms,
      tempClass: {
        pscj: undefined,
        kscj: undefined
      },
      dialogClassFormVisible: false,
      rules: {
        term: [{ required: true, message: '请选择学期', trigger: 'blur' }]
      },
      rulesClass: {
        pscj: [{ required: true, message: '请填写平时成绩', trigger: 'blur' }],
        kscj: [{ required: true, message: '请填写考试成绩', trigger: 'blur' }]
      },
      classStatus: false,
      studentStatus: false
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
    handleUpdate(row) {
      this.dialogClassFormVisible = true
      this.currentRow = row
    },
    onSubmitTerm() {
      this.$refs['TermForm'].validate((valid) => {
        if (valid) {
          this.classStatus = true
          const data = { xq: this.currentTerm.term }
          this.$store.dispatch('teacher/getClass', data).then(response => {
            console.log('terms', response)
            this.listClass = response
            this.listLoading = false
          }).catch(() => {
          })
        } else {
          this.$message('cnm')
        }
      })
    },

    getClass() {

    },
    getStudent() {

    },
    handleFilter() {
      this.listQuery.page = 1
      this.getList()
    },
    handleCurrentClassChange(val) {
      this.studentStatus = false
      this.currentClass = val
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
    handleUpdate1() {
      const data = { xq: this.currentTerm.term, xh: this.currentRow.xh, kh: this.currentClass.kh, pscj: this.tempClass.pscj, kscj: this.tempClass.kscj }
      this.$store.dispatch('teacher/updateScore', data).then(response => {
        console.log('handleStudent', response)
        this.$message(response)
      }).catch(() => {
      })
    },
    handleFilterStudent() {
      this.listQueryStudent.page = 1
      this.getStudent()
    },
    handleClass() {
      this.classStatus = true
    },
    handleStudent() {
      const data = { xq: this.currentTerm.term, xh: this.listQueryStudent.xh, kh: this.currentClass.kh }
      this.$store.dispatch('teacher/getStudent', data).then(response => {
        console.log('handleStudent', response)
        this.listStudent = response.list
        this.chartData.rows = response.rows
        this.studentStatus = true
      }).catch(() => {
      })
    }
  }
}
</script>

