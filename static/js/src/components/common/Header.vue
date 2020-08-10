<template>
    <div>
        <div class="header card margin-bottom20">
            <el-row>
            <el-col :span="4">
                <div class="logo">
                    Forum System
                </div>
            </el-col>
            <el-col :span="16" >
                <el-menu  class="menu" mode="horizontal">
                    <el-menu-item index="1">首页</el-menu-item>
                    <el-menu-item index="2">资源中心</el-menu-item>
                    <el-menu-item index="3">积分充值</el-menu-item>
                </el-menu>
            </el-col>
            <el-col :span="3">
                <span class="user">
                    <el-avatar class="avatar" icon="el-icon-user-solid" :size="30"></el-avatar>
                    <el-dropdown class="user-info" trigger="click">
                      <span class="el-dropdown-link">
                        Lands_LJK<i class="el-icon-arrow-down el-icon-caret-bottom" style="color: #aaa;font-size: 12px;margin-left: 5px;"></i>
                      </span>
                      <el-dropdown-menu slot="dropdown">
                        <el-dropdown-item class="header-drop-item">积分：<span class="points">15</span></el-dropdown-item>
                        <el-dropdown-item class="header-drop-item">金币：<span class="coins">200</span></el-dropdown-item>
                      </el-dropdown-menu>
                    </el-dropdown>
                </span>
            </el-col>
            <el-col :span="1">
                <font-awesome-icon :icon="['fas', 'sign-out-alt']" style="color: #888;font-size: 12px;" />
            </el-col>
        </el-row>
        </div>
        <div class="banner">
        </div>
    </div>
</template>

<script>
    export default {
        name: "HeaderBox"
    }
</script>

<style scoped>
    .header {
        height: 60px;
        line-height: 60px;
        background: #fff;
    }
    .header .logo {
        text-align: center;
        font-size: 20px;
        color: #666;
    }
    .header .menu {
        height: 60px;
    }
    .header .user {
        height: 60px;
        line-height: 60px;
    }
    .header .user .avatar {
        vertical-align: middle;
        margin-right: 10px;
    }
    .user-info {
        font-size: 14px;
        cursor: pointer;
    }
    .header-drop-item {
        font-size: 12px !important;
        line-height: 25px;
    }
    .header-drop-item .coins {
        color: #ebb563;
        font-weight: 700;
    }
    .header-drop-item .points {
        color: #F56C6C;
        font-weight: 700;
    }
    .banner {
        border: 1px solid #eaeaea;
        height: 120px;
        background: #fff;
    }
</style>