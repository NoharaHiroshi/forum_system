<template>
    <div class="register card">
        <div class="register-title">注册</div>
        <div class="register-context">
            <el-form ref="registerForm" :model="registerForm" status-icon :rules="rulesForm" label-width="95px" size="small">
                <el-form-item label="昵称" prop="name">
                    <el-input v-model="registerForm.name" maxlength="15" placeholder="请输入昵称" size="small" show-word-limit></el-input>
                </el-form-item>
                <el-form-item label="邮箱" prop="email">
                    <el-input v-model="registerForm.email" placeholder="请输入邮箱" size="small"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password">
                    <el-input v-model="registerForm.password" placeholder="请输入密码" size="small" show-password></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="verify">
                    <el-input v-model="registerForm.verify" placeholder="请确认密码" size="small"  show-password></el-input>
                </el-form-item>
                 <el-form-item prop="agreement" class="link-tab">
                    <el-checkbox v-model="form.agreement" @change="agreementChange()"></el-checkbox>
                    同意<a target="_blank" href="#">网站服务条款</a>
                  </el-form-item>
                <el-form-item>
                    <div class="form-btn-grp">
                      <el-button type="primary" @click="register('registerForm')">注册</el-button>
                    </div>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Register",
        data() {
            let v = this;
            let validateUsername = (rule, value, callback) => {
                if(!v.$util.CheckCommonCharValid(value)){
                    callback(new Error('包含非法字符，请检查'));
                }
                let data = {userId:value};
                v.$util.postAjax(v, v.$api.public.checkusername, data, function (result) {
                    if (result.code === '0') {
                        callback();
                    } else {
                        callback(new Error('用户名已占用，请更换。'));
                    }
                });
            };
            let validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                if(!v.$util.CheckCommonPasswordValid(value)){
                    callback(new Error('包含非法字符，请检查'));
                }
                if (this.form.repassword !== '') {
                    this.$refs.form.validateField('repassword');
                }
                callback();
                }
            };
            let validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.form.password) {
                    callback(new Error('两次输入密码不一致!'));
                } else {
                    callback();
                }
            };
            let checkAgreement = (rule, value, callback) => {
              if(!value){
                return callback(new Error('请阅读并同意协议.'));
              }
              else{
                callback();
              }
            };
            return {
                registerForm: {
                    name: "",
                    email: "",
                    password: "",
                    verify: "",
                    agreement: false
                },
                rulesForm:{
                    name:[
                      { required: true, message: '请输入昵称', trigger: 'blur' },
                      { min: 6, max: 20, message: '长度在 3 到 15 个字符', trigger: 'blur' },
                      { validator: validateUsername, trigger: 'blur' }
                    ],
                    password: [
                      { required: true, message: '请输入登录密码', trigger: 'blur' },
                      { min: 8, max: 20, message: '长度在 8 到 20 个字符', trigger: 'blur' },
                      { validator: validatePass, trigger: 'blur' }
                    ],
                    verify: [
                      { required: true, message: '请输入确认密码', trigger: 'blur' },
                      { validator: validatePass2, trigger: 'blur' }
                    ],
                    email:[
                              { required: true, message: '请输入邮箱地址', trigger: 'blur' },
                              { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
                            ],
                    agreement: [
                      { validator: checkAgreement, trigger: 'change' }
                    ]
                  }
            }
        },
        methods: {
            register() {

            }
        }
    }
</script>

<style>
    .register {
        width: 95%;
        margin: 20px auto;
        min-height: 350px;
        background: #fff;
        box-sizing: border-box;
    }
    .register-title {
        padding: 15px 20px;
        box-sizing: border-box;
        font-size: 16px;
        margin-bottom: 20px;
        border-bottom: 1px solid #eaeaea;
    }
    .register-context {
        padding: 30px 20px;
        position: relative;
        box-sizing: border-box;
        margin: 0 auto;
        width: 40%;
    }
</style>