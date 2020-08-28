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
                        <div class="post-item-title">标题：</div>
                    </el-col>
                    <el-col :span="10">
                        <el-input v-model="title" placeholder="请输入帖子主题"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <div class="post-item-help">例如：蜡笔小新[臼井仪人] 全50册 高清</div>
                    </el-col>
                </el-row>
                <el-row style="margin-bottom: 20px;">
                    <el-col :span="2">
                        <div class="post-item-title">正文：</div>
                    </el-col>
                    <el-col :span="20">
                        <quill-editor
                            v-model="content"
                            ref="editor"
                            :options="editorOption"
                            @blur="onEditorBlur($event)" @focus="onEditorFocus($event)"
                            @change="onEditorChange($event)">
                        </quill-editor>
                    </el-col>
                </el-row>
                <el-row style="margin-bottom: 20px;">
                    <el-col :span="2">
                        <div class="post-item-title">隐藏内容：</div>
                    </el-col>
                    <el-col :span="10">
                        <el-input v-model="hiddenContent"  placeholder="请输入需要用户购买后展示的内容"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <div class="post-item-help">例如：百度网盘地址 https://pan.baidu.com/s/xxxx 密码：4a3f</div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="2">
                        <div class="post-item-title">售价：</div>
                    </el-col>
                    <el-col :span="10">
                        <el-input v-model="cost" placeholder="请输入需要用户付费的金币数量"></el-input>
                    </el-col>
                    <el-col :span="8">
                        <div class="post-item-help">推荐：30金币到100金币之间</div>
                    </el-col>
                </el-row>
                <el-row>
                    <el-col :span="4" :offset="2">
                        <el-button type="primary" size="small" style="margin-top: 20px" @click="submit()">发表</el-button>
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
            return {
                post_id: null,
                content: null,
                hiddenContent: null,
                cost: null,
                title: null,
                editorOption: {
                    theme: 'snow',
                    placeholder: '请输入内容',
                    modules: {
                        toolbar: [
                            ['bold', 'italic', 'underline', 'strike'],
                            ['blockquote', 'code-block'],
                            ['image'],
                            [{ 'header': 1 }, { 'header': 2 }],
                            [{ 'list': 'ordered'}, { 'list': 'bullet' }],
                            [{ 'script': 'sub'}, { 'script': 'super' }],
                            [{ 'indent': '-1'}, { 'indent': '+1' }],
                            [{ 'direction': 'rtl' }],
                            [{ 'size': ['small', false, 'large', 'huge'] }],
                            [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
                            [{ 'color': [] }, { 'background': [] }],
                            [{ 'font': [] }],
                            [{ 'align': [] }],
                            ['clean']
                        ],
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
            onEditorChange () {

            },
            save() {
                let v = this;
                if(v.title != null && v.content != null) {
                    let data = {
                        post_id: v.post_id,
                        sub_forum_id: v.$route.params["sub_forum_id"],
                        title: v.title,
                        content: v.content,
                        hidden_content: v.hiddenContent,
                        cost: v.cost,
                        status: 0,
                    };
                    console.log(data);
                    v.$util.postAjax(v, v.$api.website.submitPost, data, function (result) {
                        if (result.response === "success") {
                            v.$message.success("帖子内容保存成功");
                        } else {
                            v.$message.error("帖子内容保存失败");
                        }
                    });
                }
            },
            submit() {
                let v = this;
                console.log(this.content);
                if(v.title == null) {
                    v.$message.error("请输入标题");
                    return;
                }
                if(v.content == null) {
                    v.$message.error("正文内容不能为空");
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
                    content: v.content,
                    hidden_content: v.hiddenContent,
                    cost: v.cost,
                    status: 1,
                };
                v.$util.postAjax(v, v.$api.website.submitPost, data, function (result) {
                    if (result.response === "success") {
                        v.$notify({
                            title: '发布帖子成功',
                            message: '发布成功',
                            type: 'success'
                        });
                        v.$router.push({name: forum, params: {sub_forum_id: v.$route.params["sub_forum_id"]}})
                    } else {
                        v.$notify({
                            title: '发布帖子失败',
                            message: result.info,
                            type: 'error'
                        });
                    }
                });
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
    .post-item-title{
        display: inline-block;
        height: 40px;
        line-height: 40px;
        text-align: right;
    }
    .post-item-help {
        display: inline-block;
        height: 40px;
        line-height: 40px;
        color:#acacac;
        margin-left: 10px;
    }
</style>