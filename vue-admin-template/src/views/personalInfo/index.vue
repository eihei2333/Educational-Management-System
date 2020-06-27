<template>
  <div class="app-container">
    <el-form ref="TermForm" :model="currentPass" label-width="200px" :rules="rules">
      <el-form-item label="设置新密码" prop="term">
        <el-input v-model="currentPass.pass" placeholder="请输入新密码" style="width: 200px;" prop="xf"/>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmitTerm()">确定</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>

export default {
  data() {
    return {
      currentPass: {
        pass: undefined
      },
      rules: {
        pass: [{ required: true, message: '请填写密码', trigger: 'blur' }]
      }
    }
  },
  methods: {
    onSubmitTerm() {
      this.$refs['TermForm'].validate((valid) => {
        if (valid) {
          this.loading = true
          this.$store.dispatch('user/changePassword', this.currentPass).then(response => {
            this.$message(response)
          }).catch(() => {
          })
        } else {
          this.$message('cnm')
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

