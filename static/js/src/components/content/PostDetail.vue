<template>
    <div class="context" style="width: 95%;margin: 0 auto;">
        <el-breadcrumb separator-class="el-icon-arrow-right" class="margin-bottom20" style="font-size: 12px;" v-if="!is_loading">
            <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
            <el-breadcrumb-item :to="{ name: 'forum', params: {sub_forum_id: sub_forum.id} }">{{sub_forum.name}}</el-breadcrumb-item>
            <el-breadcrumb-item>{{post.title}}</el-breadcrumb-item>
        </el-breadcrumb>
        <div class="margin-bottom20 card post-detail-context" v-loading="is_loading">
            <div class="post-context-detail" v-if="!is_loading">
                <div class="post-user-context">
                    <div class="post-user-info">
                        <div class="post-user-name">{{user.name}}</div>
                        <div class="post-user-avatar"></div>
                        <div class="other-post">
                            <div class="other-post-title">Ta的其他帖子</div>
                            <router-link class="other-post-item" to="/">蜡笔小新[臼井仪人] 全50册 高清</router-link>
                            <router-link class="other-post-item" to="/">幽游白书 高清单行本 15卷</router-link>
                            <router-link class="other-post-item" to="/">彼氏彼女的故事（男女跷跷板） 津田雅美 全21卷 经典爱情故事</router-link>
                        </div>
                    </div>
                </div>
                <div class="post-detail-content">
                    <div class="post-detail-title">{{post.title}}</div>
                    <div class="post-detail">
                        <div class="post-detail-cover">封面图片:</div>
                        <div class="post-detail-cover-image">
                            <img :src="cover_image_url">
                        </div>
                        <div class="post-detail-cover">帖子内容:</div>
                        <div class="post-detail-data" v-html="post.content"></div>
                        <div class="post-detail-cover">隐藏内容:</div>
                        <div class="post-hidden-content">
                            <div class="hidden-message">
                                <span class="locked"><img src="http://localhost:5000/static/img/locked.gif"></span>
                                <strong style="color: #FF6B00">{{current_user.name}}</strong>, 本付费内容需要支付 <strong style="color: #FF6B00">{{post.cost}}金币</strong> 才能浏览。
                                <span @click="pay()" class="pay">支付</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: "PostDetail",
        data() {
            return {
                is_loading: true,
                post: null,
                cover_image_url: null,
                user: null,
                sub_forum: null
            }
        },
        created() {
          this.get_post()
        },
        computed: {
            current_user: function () {
                return this.$store.state.user;
            }
        },
        methods: {
            get_post() {
                let v = this;
                let params = {
                    post_id: v.$route.params["post_id"],
                };
                v.$util.getAjax(v, v.$api.website.getPost, params, function (result) {
                    if (result.response === "success") {
                        if(result.data){
                            v.post = result.data.post;
                            v.cover_image_url = v.$config.image_url +  result.data.cover_image_url;
                            v.user = result.data.user;
                            v.sub_forum = result.data.sub_forum;
                            v.is_loading = false;
                        }
                    } else {
                        v.$message.error("获取帖子内容失败");
                    }
                });
            },
            pay() {
                let v = this;
                this.$confirm('购买此资源将消耗<strong style="color: #FF6B00;">' + this.post.cost + '金币</strong>，是否确定购买?', '提示', {
                    dangerouslyUseHTMLString: true,
                    confirmButtonText: '确定',
                    cancelButtonText: '取消',
                    type: 'warning'
                }).then(() => {
                    let params = {
                        post_id: v.$route.params["post_id"],
                    };
                    v.$util.postAjax(v, v.$api.website.pay, params, function (result) {
                        if (result.response === "success") {
                            if(result.data){
                                v.$message({
                                    type: 'success',
                                    message: '购买成功!'
                                });
                            }
                        } else {
                            v.$message({
                                type: 'error',
                                message: '购买失败！' + result.info
                            });
                        }
                    });
                });
            }
        }
    }
</script>

<style>
    .post-detail-context {
        background: #fff;
        padding: 10px;
    }
    .post-context-detail {
        padding: 5px;
    }
    .post-user-context {
        border: 1px solid #eaeaea;
        background: #fafafa;
        display: inline-block;
        width: 200px;
        margin-right: 10px;
    }
    .post-user-info {
        height: 100%;
    }
    .post-user-name {
        text-align: left;
        height: 40px;
        line-height: 40px;
        font-size: 12px;
        border-bottom: 1px dashed #CDCDCD;
        color: #333;
        font-weight: 700;
        padding: 0 15px;
        box-sizing: border-box;
        margin-bottom: 15px;
    }
    .post-user-avatar {
        padding: 10px 15px;
        width: 170px;
        height: 170px;
        margin: 0 auto;
        background: #eee;
        border: 1px solid #eaeaea;
        box-sizing: border-box;
    }
    .other-post {
        padding: 10px 15px;
    }
    .other-post-title {
        margin-bottom: 10px;
    }
    .post-detail {
        padding: 0 15px;
    }
    .other-post-item {
        display: block;
        height: 25px;
        line-height: 25px;
        margin-bottom: 2px;
        border-bottom: 1px solid #eaeaea;
        white-space:nowrap;
        overflow:hidden;
        text-overflow:ellipsis;
    }
    .post-detail-content {
        display: inline-block;
        vertical-align: top;
        min-height: 400px;
        width: calc(100% - 220px);
        border: 1px solid #eaeaea;
    }
    .post-detail-title {
        text-align: left;
        font-size: 16px;
        height: 40px;
        line-height: 40px;
        color: #444;
        font-weight: 700;
        padding: 0 15px;
        border-bottom: 1px dashed #CDCDCD;
    }
    .post-detail-cover {
        font-size: 14px;
        height: 50px;
        line-height: 50px;
        color: #444;
        font-weight: 700;
    }
    .post-detail-cover-image {
        margin: 10px auto;
        text-align: center;
    }
    .post-detail-cover-image img {
        width: 400px;
        height: 100%;
    }
    .post-detail-data {
        margin: 0 auto;
    }
    .post-detail-data img {
        width: 90%;
        text-align: center;
    }
    .hidden-message {
        margin: 10px 0 20px;
        padding: 0 24px;
        height: 50px;
        line-height: 50px;
        border: 2px solid #FF6B00;
        font-size: 14px;
    }
    .locked {
        width: 16px;
        height: 16px;
        display: inline-block;
    }
    .pay {
        color: #FF6B00;
        text-decoration:underline;
        cursor: pointer;
        font-weight: 700;
    }
    .pay:hover {
        color: #409EFF;
        transition: 1s;
    }
</style>