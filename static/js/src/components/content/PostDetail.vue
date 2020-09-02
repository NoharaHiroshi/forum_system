<template>
    <div class="context" style="width: 95%;margin: 0 auto;">
         <el-breadcrumb separator-class="el-icon-arrow-right" class="margin-bottom20" style="font-size: 12px;">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item>漫画资源</el-breadcrumb-item>
             <el-breadcrumb-item>漫画资源</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="margin-bottom20 card post-detail-context">
            <div class="post-context">
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "PostDetail"
    }
</script>

<style>
    .post-detail-context {
        background: #fff;
        padding: 10px;
    }
</style>