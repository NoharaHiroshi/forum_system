<template>
    <div class="context">
        <el-row :gutter="20" class="margin-bottom20">
            <el-col :span="12">
                <el-carousel trigger="click" class="carousel card" height="280px">
                  <el-carousel-item v-for="item in 4" :key="item">
                    <h3 class="small">{{ item }}</h3>
                  </el-carousel-item>
                </el-carousel>
            </el-col>
            <el-col :span="12">
                 <el-tabs v-model="activeName" type="border-card" class="topic" @tab-click="handleClick">
                    <el-tab-pane label="最新帖子" name="first">
                        <ul class="topic-list">
                            <li v-for="item in 8" :key="item">
                                <div class="title">{{ item }}. 标题</div>
                                <div class="date">2020-08-07</div>
                            </li>
                        </ul>
                    </el-tab-pane>
                    <el-tab-pane label="最热帖子" name="second">最热帖子</el-tab-pane>
                    <el-tab-pane label="精华帖子" name="third">精华帖子</el-tab-pane>
                  </el-tabs>
            </el-col>
        </el-row>
        <div class="website-info margin-bottom20 card">
            <font-awesome-icon :icon="['fas', 'chart-bar']" style="color: #888;font-size: 14px;margin-right: 5px;" />
            <div class="website-info-title">今日: <span style="color: #333;">366</span></div><span class="pipe">|</span>
            <div class="website-info-title">昨日: <span style="color: #333;">172</span></div><span class="pipe">|</span>
            <div class="website-info-title">帖子: <span style="color: #333;">18269</span></div><span class="pipe">|</span>
            <div class="website-info-title">会员: <span style="color: #333;">46948</span></div>
        </div>
        <div class="board margin-bottom20 card" v-for="forum in forum_list" :key="forum.id">
            <div class="title">
                {{forum.name}}
            </div>
            <div class="board-context">
                <div class="category-item"  v-for="sub_forum in forum.sub_forums" :key="sub_forum.id">
                    <div class="category-item-img"></div>
                    <div class="category-item-title"><span style="margin-right: 3px;">{{sub_forum.name}}</span><span class="new-add">(16)</span></div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  	name: 'Index',
    data() {
      return {
          activeName: 'first',
          forum_list: null
      }
    },
    created() {
  	  this.index();
    },
    methods: {
        handleClick(tab, event) {
            console.log(tab, event);
        },
        index() {
            let v = this;
            v.$util.getAjax(v, v.$api.website.index, {}, function (result) {
                if (result.response === "success") {
                    v.forum_list = result.forum_list;
                } else {
                    v.$message.error(result.info);
                }
            });
        }
    }
}
</script>

<style>
	.context {
        width: 95%;
        margin: 0 auto;
    }
    .carousel {
        background: #fff;
        border: 2px solid #fff;
        box-sizing: border-box;
    }
    .carousel .el-carousel__item h3 {
        color: #475669;
        font-size: 14px;
        opacity: 0.75;
        line-height: 280px;
        margin: 0;
        text-align: center;
    }
    .carousel .el-carousel__item:nth-child(2n) {
        background-color: #99a9bf;
    }

    .carousel .el-carousel__item:nth-child(2n+1) {
        background-color: #d3dce6;
    }
    .topic {
        background: #fff;
        height: 280px;
    }
    .topic-list {
        padding: 0 5px;
    }
    .topic-list li {
        height: 26px;
        line-height: 26px;
        font-size: 14px;
        position: relative;
    }
    .topic-list li .title {
        width: 450px;
        display: inline-block;
    }
    .topic-list li .date {
        position: absolute;
        right: 0;
        display: inline-block;
        font-size: 13px;
        color: #aaa;
    }
    .board {
        background: #fff;
    }
    .board .title {
        text-align: left;
        padding: 15px 20px;
        font-size: 18px;
        font-weight: 700;
        border-bottom: 1px solid #eaeaea;
        box-sizing: border-box;
    }
    .board .category-item {
        width: 32.9%;
        box-sizing: border-box;
        display: inline-block;
        padding: 20px;
        height: 140px;
    }
    .category-item-img {
        display: inline-block;
        width: 60%;
        height: 100%;
        border: 1px solid #eaeaea;
        margin-right: 5px;
    }
    .category-item-title {
        font-size: 16px;
        vertical-align:top;
        display: inline-block;
        width: 35%;
        color: #333;
        font-weight: normal;
        overflow: hidden;
    }
    .new-add {
        display: inline-block;
        font-size: 12px;
        color: #F26C4F;
    }
    .website-info {
        height: 20px;
        line-height: 20px;
        padding: 15px 20px;
        background:  #fff;
    }
    .website-info-title {
        display: inline-block;
        color: #aaa;
        padding: 0 5px;
    }
    .pipe {
        margin: 0 5px;
        color: #CCC;
    }
</style>
