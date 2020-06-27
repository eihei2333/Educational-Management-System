<template>
  <div class="app-container">
    <el-form ref="creditSetting" :model="creditSetting" label-width="200px" :rules="rules">
      <el-form-item label="设置当前学期" prop="term">
        <el-select v-model="creditSetting.term" placeholder="请选择当前学期">
          <el-option v-for="item in terms" :key="item" :label="item" :value="item" />
        </el-select>
      </el-form-item>
<!--      <el-form-item>-->
<!--        <el-button type="primary" @click="onSubmitTerm()">确定</el-button>-->
<!--      </el-form-item>-->
<!--    </el-form>-->

<!--    <el-form ref="creditSetting" :model="creditSetting" label-width="200px" :rules="rules">-->
      <el-form-item label="选择院系学分上限" required>
        <el-col :span="5">
          <el-form-item prop="yxh">
            <el-select v-model="creditSetting.yxh" placeholder="请选择院系">
              <el-option v-for="item in DepartmentList" :key="item.yxh" :label="item.display_name" :value="item.yxh" />
            </el-select>
          </el-form-item>
        </el-col>
        <el-col :span="11">
          <el-form-item prop="credit">
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
        term: '',
        yxh: '',
        credit: ''
      },
      DepartmentList,

      rules: {
        term: [{ required: true, message: '请填写学期', trigger: 'blur' }],
        yxh: [{ required: true, message: '请填写院系', trigger: 'blur' }],
        credit: [{ required: true, message: '请填写学分上限', trigger: 'blur' }]
      }
    }
  },
  created: function() {
    this.$store.dispatch('user/getTerm').then(response => {
      this.terms = response.terms
      this.$store.dispatch('user/getCollege').then(response => {
        this.DepartmentList = response.college
      }).catch(() => {
      })
    }).catch(() => {
    })
  },
  methods: {
    onSubmitTerm() {
      this.$refs['creditSetting'].validate((valid) => {
        if (valid) {
          this.$message(this.creditSetting.term)
          console.log(this.creditSetting.term)
        } else {
          this.$message('cnm')
          console.log(this.creditSetting.term)
        }
      })
    },
    onSubmitCredit() {
      this.$refs.creditSetting.validate((valid) => {
        if (valid) {
          this.$store.dispatch('admin/setSx', this.creditSetting).then(res => {
            this.$message(res)
          }).catch(() => {
            this.loading = false
          })
        } else {
          this.$message('valid!')
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

