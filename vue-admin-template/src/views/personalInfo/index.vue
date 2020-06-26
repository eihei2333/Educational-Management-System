<template>
  <div class="app-container">
    <el-form ref="PassForm" :model="currentPass" :rules="rulesPass" label-width="200px">
      <el-form-item label="设置新密码" prop="pass">
        <el-input v-model="currentPass.pass" placeholder="请输入新密码" style="width: 200px" />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmitPass()">确定</el-button>
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
      rulesPass: {
        pass: [{ required: true, message: '请填写密码', trigger: 'blur' }]
      }
    }
  },
  methods: {
    onSubmitPass() {
      this.$refs['PassForm'].validate((valid) => {
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
    }
  }
}
</script>
