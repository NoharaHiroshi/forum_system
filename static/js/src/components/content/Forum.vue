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
        <div class="margin-bottom20 card post-context">

        </div>
    </div>
</template>

<script>
    export default {
        name: "Forum",
        data() {
            return {
                category_list: null
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
        padding: 10px 20px;
    }
</style>