<template>
    <div class="register card">
        <div class="register-title">注册</div>
        <div class="register-context">
            <el-form ref="registerForm" :model="registerForm" status-icon :rules="rulesForm" label-width="95px" size="small">
                <el-form-item label="昵称" prop="name" class="form-item">
                    <el-input v-model="registerForm.name" maxlength="15" placeholder="请输入昵称" size="small" show-word-limit></el-input>
                </el-form-item>
                <el-form-item label="邮箱" prop="email" class="form-item">
                    <el-input v-model="registerForm.email" placeholder="请输入邮箱" size="small"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password" class="form-item">
                    <el-input v-model="registerForm.password" placeholder="请输入密码" size="small" show-password></el-input>
                </el-form-item>
                <el-form-item label="确认密码" prop="verify" class="form-item">
                    <el-input v-model="registerForm.verify" placeholder="请确认密码" size="small"  show-password></el-input>
                </el-form-item>
                 <el-form-item prop="agreement" class="link-tab form-item">
                    <el-checkbox v-model="registerForm.agreement" @change="agreementChange()"></el-checkbox>
                    同意<a target="_blank" href="#">网站服务条款</a>
                  </el-form-item>
                <el-form-item class="form-item">
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
                if(!v.$util.checkCommonCharValid(value)){
                    callback(new Error('包含非法字符，请检查'));
                }
                let data = {name: value};
                v.$util.postAjax(v, v.$api.user.checkUserName, data, function (result) {
                    if (result.response === 'success') {
                        callback();
                    } else {
                        callback(new Error('用户名已占用，请更换。'));
                    }
                });
            };
            let validateUserEmail = (rule, value, callback) => {
                let data = {email: value};
                v.$util.postAjax(v, v.$api.user.checkUserEmail, data, function (result) {
                    if (result.response === 'success') {
                        callback();
                    } else {
                        callback(new Error('用户邮箱已占用，请更换。'));
                    }
                });
            };
            let validatePass = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请输入密码'));
                } else {
                if(!v.$util.checkCommonPasswordValid(value)){
                    callback(new Error('包含非法字符，请检查'));
                }
                if (this.registerForm.verify !== '') {
                    this.$refs.registerForm.validateField('verify');
                }
                callback();
                }
            };
            let validatePass2 = (rule, value, callback) => {
                if (value === '') {
                    callback(new Error('请再次输入密码'));
                } else if (value !== this.registerForm.password) {
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
                      { min: 3, max: 15, message: '长度在 3 到 15 个字符', trigger: 'blur' },
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
                      { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] },
                      { validator: validateUserEmail, trigger: 'blur' }
                    ],
                    agreement: [
                      { validator: checkAgreement, trigger: 'change' }
                    ]
                }
            }
        },
        methods: {
            register(formName) {
                let form = {
                    name: this.registerForm.name,
                    password: this.registerForm.password,
                    email: this.registerForm.email
                };
                let v = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        if(!v.registerForm.agreement){
                            this.$refs.registerForm.validateField('agreement');
                            return;
                        }
                        v.$util.postAjax(v, v.$api.user.register, form, function (result) {
                            if (result.response === "success") {
                                v.$notify({
                                    title: '注册成功',
                                    message: '恭喜您注册成功。',
                                    type: 'success'
                                });
                                v.$router.push({name: 'login'});
                            } else {
                                v.$message.error(result.msg);
                            }
                        });
                    } else {
                        return false;
                    }
                });
            },
            agreementChange(){
                let v = this;
                if(this.registerForm.agreement){
                    this.$confirm('选中代表您已阅读并同意《网站服务条款》', '提示', {
                    confirmButtonText: '已阅读并同意',
                    cancelButtonText: '不同意',
                    type: 'warning'
                }).then(() => {
                    v.registerForm.agreement = true;
                }).catch(() => {
                    v.registerForm.agreement = false;
                });
              }
            },
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
    .form-item {
        margin-bottom: 25px !important;
    }
    .el-form-item__error {
        padding-top: 5px;
    }
    .el-form-item--feedback .el-input__validateIcon {
        color: #86FF40;
    }
</style>