<template>
    <div class="login card">
        <div class="login-title">登录</div>
        <div class="login-context">
            <el-form ref="loginForm" :model="loginForm" status-icon :rules="rulesForm" label-width="100px" size="small">
                <el-form-item label="邮箱" prop="email" class="form-item">
                    <el-input v-model="loginForm.email" placeholder="请输入邮箱" size="small"></el-input>
                </el-form-item>
                <el-form-item label="密码" prop="password" class="form-item">
                    <el-input v-model="loginForm.password" placeholder="请输入密码" size="small" show-password></el-input>
                </el-form-item>
                <el-form-item label="验证码" prop="captcha" class="form-item">
                    <el-input v-model="loginForm.captcha" placeholder="请输入验证码" size="small"  style="width: 200px;"></el-input>
                    <div class="captcha-img" @click="getCaptcha()"><img :src="captchaImg"></div>
                </el-form-item>
                <el-form-item class="form-item">
                    <div class="form-btn-grp">
                      <el-button type="primary" @click="login('loginForm')">登录</el-button>
                    </div>
                </el-form-item>
            </el-form>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Login",
        created() {
            this.getCaptcha();
        },
        data() {
            return {
                tokenId: "",
                captchaImg: "",
                loginForm: {
                    email: "",
                    password: "",
                    captcha: ""
                },
                rulesForm:{
                    email:[
                      { required: true, message: '请输入邮箱地址', trigger: 'blur' },
                      { type: 'email', message: '请输入正确的邮箱地址', trigger: ['blur', 'change'] }
                    ],
                    password: [
                      { required: true, message: '请输入登录密码', trigger: 'blur' },
                      { min: 8, max: 20, message: '长度在 8 到 20 个字符', trigger: 'blur' }
                    ],
                    captcha: [
                      { required: true, message: '请输入验证码', trigger: 'blur' },
                    ],
                }
            }
        },
        methods: {
            login(formName) {
                let form = {
                    email: this.loginForm.email,
                    password: this.loginForm.password,
                    captcha: this.loginForm.captcha
                };
                let v = this;
                this.$refs[formName].validate((valid) => {
                    if (valid) {
                        v.$util.postAjax(v, v.$api.user.login, form, function (result) {
                            if (result.response === "success") {
                                v.$notify({
                                    title: '登录成功',
                                    message: '登录成功',
                                    type: 'success'
                                });
                            } else {
                                v.$message.error(result.msg);
                            }
                        });
                    } else {
                        return false;
                    }
                });
            },
            getCaptcha() {
                let v = this;
                let random_str = new Date().getTime();
                for (let i = 5; i > 0; i--) {
                    let j = Math.floor(Math.random() * (i + 1));
                    random_str += j;
                }
                v.tokenId = random_str;
                let data = {
                  "token": v.tokenId
                };
                v.$util.postAjax(v, v.$api.user.getCaptcha, data, function (result) {
                    if (result.response === "success") {
                        v.captchaImg = result.data;
                    } else {
                        v.$message.error(result.msg);
                    }
                });
            }
        }
    }
</script>

<style>
    .login {
        width: 95%;
        margin: 20px auto;
        min-height: 350px;
        background: #fff;
        box-sizing: border-box;
    }
    .login-title {
        padding: 15px 20px;
        box-sizing: border-box;
        font-size: 16px;
        margin-bottom: 20px;
        border-bottom: 1px solid #eaeaea;
    }
    .login-context {
        padding: 30px 20px;
        position: relative;
        box-sizing: border-box;
        margin: 0 auto;
        width: 40%;
    }
    .form-item {
        margin-bottom: 25px !important;
        width: 400px;
    }
    .el-form-item__error {
        padding-top: 5px;
    }
    .el-form-item--feedback .el-input__validateIcon {
        color: #86FF40;
    }
    .captcha-img {
        position: relative;
        display: inline-block;
        width: 90px;
        height: 32px;
        line-height: 32px;
        box-sizing: border-box;
        vertical-align: middle;
    }
    .captcha-img img {
        height: 100%;
    }
</style>