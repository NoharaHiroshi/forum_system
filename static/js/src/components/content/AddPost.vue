<template>
    <div class="context" style="width: 95%;margin: 0 auto;">
        <el-breadcrumb separator-class="el-icon-arrow-right" class="margin-bottom20" style="font-size: 12px;">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>漫画资源</el-breadcrumb-item>
            <el-breadcrumb-item>发表帖子</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="margin-bottom20 card post-rule-context">
            <div class="post-rule-header">
                <div style="font-size: 16px;margin-bottom: 15px;">发帖规范</div>
            </div>
            <div class="post-rule-content">
                <div class="post-rule-item">1.发贴前请搜索一下，避免发布相同内容的帖子。</div>
                <div class="post-rule-item">2.标题请尽可能的详细的描述资源，包括但不限于资源名、作者、文件格式（zip/pdf）、清晰度、资源类型（连载/单行本）、册数。</div>
                <div class="post-rule-item">3.内容中的图片，不可以上传暴力、血腥、色情内容的图片。</div>
                <div class="post-rule-item">4.有版权、H类型、限制级、R18、本子类型资源均不可以发布。</div>
            </div>
        </div>
        <div class="margin-bottom20 card post-context">
            <div>
                <div class="post-rule-header">
                    <div style="font-size: 16px;margin-bottom: 15px;">发表帖子</div>
                </div>
                <el-row style="margin-bottom: 20px;">
                    <el-col :span="2">
                        <div class="add-post-item-title">标题：</div>
                    </el-col>
                    <el-col :span="10">
                        <el-input v-model="title" placeholder="请输入帖子主题" maxlength="40" show-word-limit></el-input>
                    </el-col>
                    <el-col :span="8">
                        <div class="post-item-help">提示：蜡笔小新[臼井仪人] 全50册 高清</div>
                    </el-col>
                </el-row>
                <el-row style="margin-bottom: 20px;">
                    <el-col :span="2">
                        <div class="add-post-item-title">封面：</div>
                    </el-col>
                    <el-col :span="4">
                        <el-upload
                            class="uploader"
                            :action="upload_imag_url"
                            :show-file-list="false"
                            name="img"
                            :on-success="handleCoverSuccess"
                            :before-upload="beforeCoverUpload">
                            <img v-if="cover_image_url" :src="cover_image_url" class="cover">
                            <i v-else class="el-icon-plus avatar-uploader-icon"></i>
                        </el-upload>
                    </el-col>
                    <el-col :span="8">
                        <div class="post-item-help" style="line-height: 178px;">提示：用于在首页中显示</div>
                    </el-col>
                </el-row>
                <el-row style="margin-bottom: 20px;">
                    <el-col :span="2">
                        <div class="add-post-item-title">正文：</div>
                    </el-col>
                    <el-col :span="20">
                        <quill-editor
                            v-model="content"
                            ref="editor"
                            :options="editorOption"
                            @blur="onEditorBlur($event)" @focus="onEditorFocus($event)"
                            @change="onEditorChange($event)">
                        </quill-editor>
                        <div style="float: right; margin-top: 5px; color: #aaa;" id="content_len">{{content_length}} / {{max_content_length}}</div>
                    </el-col>
                </el-row>
                <el-row style="margin-bottom: 20px;">
                    <el-col :span="2">
                        <div class="add-post-item-title">隐藏内容：</div>
                    </el-col>
                    <el-col :span="10">
                        <el-input v-model="hiddenContent"  placeholder="请输入需要用户购买后展示的内容"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <div class="post-item-help">提示：百度网盘地址 https://pan.baidu.com/s/xxxx 密码：4a3f</div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="2">
                        <div class="add-post-item-title">售价：</div>
                    </el-col>
                    <el-col :span="10">
                        <el-input v-model="cost" placeholder="请输入需要用户付费的金币数量"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <div class="post-item-help">提示：推荐30金币到100金币之间</div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="4" :offset="2">
                        <el-button type="primary" size="small" style="margin-top: 20px" @click="submit()">发表</el-button>
                        <el-button type="warning" size="small" style="margin-top: 20px" @click="save()">保存为草稿</el-button>
                    </el-col>
                </el-row>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AddPost",
        data() {
            const uploadConfig = {
                action:  this.$api.lib.uploadImage,  // 必填参数 图片上传地址
                resource_url: this.$config.image_url,
                methods: 'POST',  // 必填参数 图片上传方式
                token: '',  // 可选参数 如果需要token验证，假设你的token有存放在sessionStorage
                name: 'img',  // 必填参数 文件的参数名
                size: 500,  // 可选参数   图片大小，单位为Kb, 1M = 1024Kb
                accept: 'image/png, image/gif, image/jpeg, image/bmp, image/x-icon'  // 可选 可上传的图片格式
            };
            const toolOptions = [
                ['bold', 'italic', 'underline', 'strike'],
                ['blockquote', 'code-block'],
                [{'header': 1}, {'header': 2}],
                [{'list': 'ordered'}, {'list': 'bullet'}],
                [{'script': 'sub'}, {'script': 'super'}],
                [{'indent': '-1'}, {'indent': '+1'}],
                [{'direction': 'rtl'}],
                [{'size': ['small', false, 'large', 'huge']}],
                [{'header': [1, 2, 3, 4, 5, 6, false]}],
                [{'color': []}, {'background': []}],
                [{'font': []}],
                [{'align': []}],
                ['clean'],
                ['image']
            ];
            const handlers = {
                image: function image() {
                    let self = this;

                    let fileInput = this.container.querySelector('input.ql-image[type=file]');
                    if (fileInput === null) {
                        fileInput = document.createElement('input');
                        fileInput.setAttribute('type', 'file');
                        // 设置图片参数名
                        if (uploadConfig.name) {
                            fileInput.setAttribute('name', uploadConfig.name);
                        }
                        // 可设置上传图片的格式
                        fileInput.setAttribute('accept', uploadConfig.accept);
                        fileInput.classList.add('ql-image');
                        // 监听选择文件
                        fileInput.addEventListener('change', function () {
                            // 创建formData
                            let formData = new FormData();
                            formData.append(uploadConfig.name, fileInput.files[0]);
                            formData.append('object','product');
                            // 如果需要token且存在token
                            if (uploadConfig.token) {
                                formData.append('token', uploadConfig.token)
                            }
                            // 图片上传
                            let xhr = new XMLHttpRequest();
                            xhr.open(uploadConfig.methods, uploadConfig.action, true);
                            // 上传数据成功，会触发
                            xhr.onload = function (e) {
                                if (xhr.status === 200) {
                                    let res = JSON.parse(xhr.responseText);
                                    console.log(res);
                                    let length = self.quill.getSelection(true).index;
                                    //这里很重要，你图片上传成功后，img的src需要在这里添加，res.path就是你服务器返回的图片链接。
                                    self.quill.insertEmbed(length, 'image', uploadConfig.resource_url + res.data.src);
                                    self.quill.setSelection(length + 1)
                                }
                                fileInput.value = ''
                            };
                            // 开始上传数据
                            xhr.upload.onloadstart = function (e) {
                                fileInput.value = ''
                            };
                            // 当发生网络异常的时候会触发，如果上传数据的过程还未结束
                            xhr.upload.onerror = function (e) {
                            };
                            // 上传数据完成（成功或者失败）时会触发
                            xhr.upload.onloadend = function (e) {
                                // console.log('上传结束')
                            };
                            xhr.send(formData)
                        });
                        this.container.appendChild(fileInput);
                    }
                    fileInput.click();
                }
            };
            return {
                post_id: null,
                content: null,
                hiddenContent: null,
                cost: null,
                title: null,
                content_length: 0,
                max_content_length: 200,
                cover_image_url: null,
                cover_image_id: null,
                upload_imag_url: this.$api.lib.uploadImage,
                upload_config: uploadConfig,
                editorOption: {
                    theme: 'snow',
                    placeholder: '请输入内容',
                    modules: {
                        toolbar: {
                            container: toolOptions,
                            handlers: handlers
                        },
                        history: {
                            delay: 2000,
                            maxStack: 500,
                            userOnly: true
                        }
                    }
                },
            }
        },
        computed: {
            editor () {
                return this.$refs.editor.quill
            }
        },
        created() {
            this.get_post();
        },
        methods: {
            // 失去焦点事件
            onEditorBlur () {
                this.save();
            },
            // 获得焦点事件
            onEditorFocus (e) {
                console.log(e);
            },
            // 内容改变事件
            onEditorChange (e) {
                // 判断是否达到最大编辑字数
                this.content_length = e.text.length;
                if(this.content_length >= this.max_content_length) {
                    $("#content_len").css("color", "#F56C6C");
                    e.quill.deleteText(this.max_content_length, 4);
                }else {
                    $("#content_len").css("color", "#AAA");
                }
            },
            get_post() {
                let v = this;
                let params = {
                    sub_forum_id: v.$route.params["sub_forum_id"],
                };
                v.$util.getAjax(v, v.$api.website.getPost, params, function (result) {
                    if (result.response === "success") {
                        if(result.data){
                            v.post_id = result.data.id;
                            v.content = result.data.content;
                            v.hiddenContent = result.data.hidden_content;
                            v.cover_image_id = result.data.cover_image_id;
                            v.cover_image_url = v.upload_config.resource_url + result.data.cover_image_url;
                            v.cost = result.data.cost;
                            v.title = result.data.title;
                        }
                    } else {
                        v.$message.error("获取帖子内容失败");
                    }
                });
            },
            save() {
                let v = this;
                if(v.content != null) {
                    let data = {
                        post_id: v.post_id,
                        sub_forum_id: v.$route.params["sub_forum_id"],
                        title: v.title,
                        content: v.content,
                        cover_image_id: v.cover_image_id,
                        hidden_content: v.hiddenContent,
                        cost: v.cost,
                        status: 0,
                    };
                    v.$util.postAjax(v, v.$api.website.submitPost, data, function (result) {
                        if (result.response === "success") {
                            v.$message.success("帖子内容保存成功");
                            v.post_id = result.data.id;
                        } else {
                            v.$message.error("帖子内容保存失败");
                        }
                    });
                }
            },
            submit() {
                let v = this;
                if(v.title == null) {
                    v.$message.error("请输入标题");
                    return;
                }
                if(v.content == null) {
                    v.$message.error("正文内容不能为空");
                    return;
                }
                if(v.cover_image_id == null) {
                    v.$message.error("封面图片不能为空");
                    return;
                }
                if(v.hiddenContent == null) {
                    v.$message.error("请输入隐藏内容");
                    return;
                }
                if(v.cost == null) {
                    v.$message.error("请输入售卖价格");
                    return;
                }
                let data = {
                    post_id: v.post_id,
                    sub_forum_id: v.$route.params["sub_forum_id"],
                    user_id: v.$store.state.user.id,
                    title: v.title,
                    cover_image_id: v.cover_image_id,
                    content: v.content,
                    hidden_content: v.hiddenContent,
                    cost: v.cost,
                    status: 1,
                };
                v.$util.postAjax(v, v.$api.website.submitPost, data, function (result) {
                    if (result.response === "success") {
                        v.$message.success("发布帖子成功");
                        v.$router.push({name: "forum", params: {sub_forum_id: v.$route.params["sub_forum_id"]}})
                    } else {
                        v.$message.error("发布帖子失败，原因 ：" + result.info);
                    }
                });
            },
            handleCoverSuccess(res, file) {
                this.cover_image_url = URL.createObjectURL(file.raw);
                if(res.response === "success"){
                    this.cover_image_id = res.data.id;
                }else {
                    this.$message.error('封面图片上传失败');
                }
            },
            beforeCoverUpload(file) {
                const isImg = (file.type === 'image/jpeg' || file.type === 'image/png');
                const isLt2M = file.size / 1024 / 1024 < 2;

                if (!isImg) {
                  this.$message.error('请上传jpeg|png格式图片');
                }
                if (!isLt2M) {
                  this.$message.error('上传封面图片大小不能超过2MB');
                }
                return isImg && isLt2M;
            }
        },
    }
</script>

<style>
    .post-rule-context {
        background: #fff;
        padding: 15px 20px;
    }
    .post-rule-content {
        background: #efefef;
        padding: 10px;
    }
    .post-rule-item {
        height: 25px;
        line-height: 25px;
        font-size: 12px;
        color: #888;
    }
    .post-context {
        background: #fff;
        padding: 15px 20px;
    }
    .ql-container {
        height: 300px;
    }
    .add-post-item-title{
        text-align: right;
        height: 40px;
        line-height: 40px;
        font-size: 12px;
        color: #888;
        display: inline-block;
        width: 100%;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }
    .post-item-help {
        display: inline-block;
        height: 40px;
        line-height: 40px;
        color:#acacac;
        margin-left: 10px;
    }
    .uploader .el-upload {
        border: 1px dashed #d9d9d9;
        border-radius: 6px;
        cursor: pointer;
        position: relative;
        overflow: hidden;
    }
      .uploader .el-upload:hover {
        border-color: #409EFF;
    }
      .avatar-uploader-icon {
        font-size: 28px;
        color: #8c939d;
        width: 178px;
        height: 178px;
        line-height: 178px;
        text-align: center;
    }
      .cover {
        height: 178px;
        display: block;
    }
</style>