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

    <el-form ref="CreditForm" :model="creditSetting" label-width="200px" :rules="rules">
      <el-form-item label="选择院系学分上限" required>
        <el-col :span="5">
          <el-form-item prop="yx">
            <el-select v-model="creditSetting.yxh" placeholder="请选择院系">
              <el-option v-for="item in DepartmentList" :key="item.yxh" :label="item.display_name" :value="item.yxh" />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="11">
          <el-form-item prop="xf">
            <el-input v-model="creditSetting.credit" placeholder="请输入学分上限" style="width: 200px;" prop="xf"/>
          </el-form-item>
        </el-col>
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="onSubmitCredit()">确定</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
const terms = [
  "{ key: 'CN', display_name: 'China' }",
  "{ key: 'US', display_name: 'USA' }",
  "{ key: 'JP', display_name: 'Japan' }",
  "{ key: 'EU', display_name: 'Eurozone' }"
]

const DepartmentList = [
  { yxh: '000', display_name: '计算机' },
  { yxh: '001', display_name: '通信' },
  { yxh: '002', display_name: '社会' },
  { yxh: '003', display_name: '机自' }
]
export default {
  data() {
    return {
      terms,
      currentTerm: {
        term: undefined
      },
      creditSetting: {
        yxh: '',
        credit: ''
      },
      DepartmentList,

      rules: {
        term: [{ required: true, message: '请填写学期', trigger: 'blur' }],
        yx: [{ required: true, message: '请填写院系', trigger: 'blur' }],
        xf: [{ required: true, message: '请填写学分上限', trigger: 'blur' }]
      }
    }
  },
  methods: {
    onSubmitTerm() {
      this.$refs['TermForm'].validate((valid) => {
        if (valid) {
          this.$message('submit!')
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
        } else {
          this.$message('cnm')
        }
      })
    },
    onSubmitCredit() {
      this.$refs['CreditForm'].validate((valid) => {
        if (valid) {
          this.$message('submit!')
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
        } else {
          // this.$message(this.CreditSetting)
        }
      })
    }
  }
}
</script>

<style scoped>
.line{
  text-align: center;
}
</style>

