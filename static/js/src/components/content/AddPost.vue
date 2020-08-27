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
                <quill-editor
                    v-model="editor"
                    ref="editor"
                    :options="editorOption"
                    @blur="onEditorBlur($event)" @focus="onEditorFocus($event)"
                    @change="onEditorChange($event)">
                </quill-editor>
                <el-button type="primary" size="small" style="margin-top: 20px">发表</el-button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "AddPost",
        data() {
            return {
                editor: null,
                editorOption: {
                    theme: 'snow',
                    placeholder: '请输入内容',
                },
                modules: {
                    toolbar: [
                        ['bold', 'italic', 'underline', 'strike'],
                        ['blockquote', 'code-block'],
                        ['image','video'],
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
            }
        },
        computed: {
            editor () {
                return this.$refs.editor.quill
            }
        },
        methods: {
            // 准备编辑器
            onEditorReady (editor) {},
            // 失去焦点事件
            onEditorBlur () {},
            // 获得焦点事件
            onEditorFocus () {},
            // 内容改变事件
            onEditorChange () {},
            saveHtml (event) {
                alert(this.content)
            }
        }
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
</style>