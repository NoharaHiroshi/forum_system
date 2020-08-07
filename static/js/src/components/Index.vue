<template>
    <div class="context">
        <el-row :gutter="20">
            <el-col :span="12">
                <el-carousel trigger="click" class="carousel" height="280px">
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
    </div>
</template>

<script>
export default {
  	name: 'Index',
    data() {
      return {
        activeName: 'first'
      };
    },
    methods: {
      handleClick(tab, event) {
        console.log(tab, event);
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
</style>
