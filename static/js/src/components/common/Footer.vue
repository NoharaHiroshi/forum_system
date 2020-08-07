<template>
    <div class="footer">
        <el-row :gutter="20">
            <el-col :span="6">
                <ul class="bottom-info">
                    <li class="title">常见问题</li>
                    <li>帮助中心</li>
                    <li>免责说明</li>
                </ul>
            </el-col>
            <el-col :span="6">
                <ul class="bottom-info">
                    <li class="title">关于我们</li>
                    <li>联系我们</li>
                    <li>用户协议</li>
                </ul>
            </el-col>
            <el-col :span="6">
            </el-col>
            <el-col :span="6">
            </el-col>
        </el-row>
    </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style>
    .footer {
        position: absolute;
        width: 100%;
        margin: 0 auto;
        font-size: 14px;
        background: #212529;
    }
    .footer .bottom-info {
        color: #fff;
        text-align: center;
        box-sizing: border-box;
        padding: 15px 0;
    }
    .bottom-info .title {
        font-size: 16px;
        margin-bottom: 10px;
        color: #fff;
    }
    .bottom-info li {
        font-size: 12px;
        height: 30px;
        line-height: 30px;
        color: #dee2e6;
    }

</style>