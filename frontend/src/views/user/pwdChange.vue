<template>
  <div class="app-container">
    <el-form ref="form" :model="form" label-width="120px">
      <el-form-item prop="old_password" label="旧密码">
        <el-input
          :type="passwordType"
          v-model="form.old_password"
          name="old_password"
          auto-complete="on"
          style="width: 50%"
        />
      </el-form-item>
      <el-form-item prop="password" label="新密码">
        <el-input
          :type="passwordType"
          v-model="form.password"
          name="password"
          auto-complete="on"
          style="width: 50%"
        />
      </el-form-item>
      <el-form-item prop="confirm_password" label="确认密码">
        <el-input
          :type="passwordType"
          v-model="form.confirm_password"
          name="confirm_password"
          auto-complete="on"
          style="width: 50%"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="handleUpdate">修改</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
  import {isvalidPassword} from '@/utils/validate'
  import {User} from '@/api/user'
  import {Message} from 'element-ui'

  export default {
    name: 'changePassword',
    data() {
      const validatePassword = (rule, value, callback) => {
        if (!isvalidPassword(value)) {
          callback(new Error('Please enter the correct password'))
        } else {
          callback()
        }
      }
      const validateConfirmPassword = (rule, value, callback) => {
        if (value != this.form.confirm_password) {
          callback(new Error('Please enter the confirm_password'))
        } else {
          callback()
        }
      }
      return {
        passwordType: 'password',
        form: {
          old_password: '',
          password: '',
          confirm_password: '',
        },
        registerRules: {
          password: [{required: true, trigger: 'blur', validator: validatePassword}],
          confirm_password: [{required: true, trigger: 'blur', validator: validateConfirmPassword}],
        }
      }
    },
    methods: {
      handleUpdate() {
        this.$refs['form'].validate(valid => {
          if (valid) {
            this.loading = true
            User.change_password(this.form).then(response => {
              this.loading = false
              Message({message: '更新成功!', type: 'success', duration: 2 * 1000})
              this.showDialog = false
            }).catch(error => {
              this.loading = false
            })
          } else {
            return false
          }
        })
      },
    }
  }
</script>
