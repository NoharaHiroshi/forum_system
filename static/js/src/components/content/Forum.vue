<template>
    <div class="context" style="width: 95%;margin: 0 auto;">
        <el-breadcrumb separator-class="el-icon-arrow-right" class="margin-bottom20" style="font-size: 12px;">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>漫画资源</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="margin-bottom20 card category-context">
            <div class="category-item" v-for="category in category_list" :key="category.id">
                <span style="font-weight: 700;">{{category.name}}：</span>
                <span class="category-item-name" @click="selectCategory()" v-for="sub_category in category.sub_categories" :key="sub_category.id">{{sub_category.name}}</span>
            </div>
        </div>
        <div class="search-context">
            <el-input v-model="search" placeholder="请输入搜索内容" class="margin-bottom20 search-post"></el-input>
            <el-button type="primary" style="height: 38px;border: none;">搜索</el-button>
        </div>
        <div class="margin-bottom20 card post-context">
            <div class="post-context-header">
                <el-button style="height: 38px;float: left;" type="primary" @click="addPost()">发帖</el-button>
                <el-pagination background layout="prev, pager, next"  style="margin-top: 5px" :total="100">
                </el-pagination>
            </div>
            <div class="post-context">
                <div class="post-item" v-for="i in 20" :key="i">
                    <div class="post-item-img"></div>
                    <router-link class="post-item-title" to="/">附罪者 全一册 清原紘 中文漫画资源下</router-link>
                    <div class="post-item-info">
                        <router-link to="/" class="post-item-creator">小新</router-link>
                        <span class="post-item-read">阅读：370</span>
                    </div>
                </div>
            </div>
            <div class="post-context-header">
                <el-button style="height: 38px;float: left;" type="primary" @click="addPost()">发帖</el-button>
                <el-pagination background layout="prev, pager, next"  style="margin-top: 5px" :total="100">
                </el-pagination>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Forum",
        data() {
            return {
                category_list: null,
                search: null
            }
        },
        created() {
          this.init();
        },
        methods: {
            init() {
                let v = this;
                v.$util.getAjax(v, v.$api.website.forum, {sub_forum_id: this.$route.params["sub_forum_id"]}, function (result) {
                    if (result.response === "success") {
                        v.category_list = result.category_list;
                    } else {
                        v.$message.error(result.info);
                    }
                });
            },
            selectCategory() {

            },
            addPost() {
                this.$router.push({
                    name: 'add_post',
                    params: {
                        sub_forum_id: this.$route.params["sub_forum_id"]
                    }
                });
            }
        }
    }
</script>

<style>
    .category-context {
        background: #fff;
        padding: 10px 20px;
    }
    .category-item {
        height: 30px;
        line-height: 30px;
    }
    .category-item-name {
        margin: 0 10px;
        cursor: pointer;
    }
    .category-item-name:hover {
        color: #409eff;
        transition: .15s ease-out;
    }
    .post-context {
        background: #fff;
        padding: 10px;
    }
    .search-context {
        text-align: right;
     }
    .search-post {
        width: 20%;
        height: 40px;
        margin-right: 5px;
    }
    .post-context-header {
        text-align: right;
        overflow: hidden;
        padding: 10px;
    }
    .post-item {
        width: 23%;
        display: inline-block;
        box-sizing: border-box;
        margin: 0 1.75% 10px 0;
        padding: 0;
        border: 8px solid #fff;
        box-shadow: 2px 3px 5px #cacaca;
        -webkit-box-shadow: 2px 3px 5px #cacaca;
        -moz-box-shadow: 2px 3px 5px #cacaca;
        transition: all 0.3s linear;
        overflow: hidden;
    }
    .post-item:hover {
        box-shadow: 3px 4px 6px #bababa;
        -webkit-box-shadow: 3px 4px 6px #bababa;
        -moz-box-shadow: 3px 4px 6px #bababa;
    }
    .post-item .post-item-img {
        display: inline-block;
        box-sizing: border-box;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        width: 100%;
        height: 280px;
        background: #efefef;
    }
    .post-item-title {
        text-align: center;
        height: 30px;
        line-height: 30px;
        font-size: 12px;
        color: #888;
        display: inline-block;
        width: 100%;
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
    }
    .post-item-info {
        height: 20px;
        line-height: 20px;
    }
    .post-item-creator {
        color: #bbb;
    }
    .post-item-read {
        float: right;
        color: #bbb;
    }
</style>