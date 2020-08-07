<template>
  <el-container>
    <!--<el-header>-->
      <HeaderBox></HeaderBox>
    <!--</el-header>-->
    <el-main class="common-main">
      <router-view/>
    </el-main>
    <el-footer class="index-footer">
      <FooterBox></FooterBox>
    </el-footer>
  </el-container>
</template>

<script>
import HeaderBox from './Header'
import FooterBox from './Footer'

export default {
  name: 'Layout',
  components: {HeaderBox, FooterBox}
}
</script>

<style>
    body {
        padding: 0;
        margin: 0;
        box-sizing: border-box;
    }
    ul, li {
        padding:0;
        margin:0;
        list-style: none
    }
    .common-main {
        width: 100%;
    }
    .index-footer {
        position: relative;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 0;
        height: 120px;
    }
    .card {
        border: 0 solid #eee;
        border-radius: 0;
        -webkit-box-shadow: 0 2px 4px 0 rgba(0,0,0,.12), 0 0 6px 0 rgba(0,0,0,.04);
        box-shadow: 0 2px 4px 0 rgba(0,0,0,.12), 0 0 6px 0 rgba(0,0,0,.04)
    }
    .margin-bottom20 {
        margin-bottom: 20px;
    }
</style>
