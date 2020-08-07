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
        position: absolute;
        bottom: 0;
        left: 0;
        width: 100%;
        padding: 0;
        height: 120px;
    }
    .card {
        border: 0 solid #eee;
        border-radius: 0;
        -webkit-box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        box-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }
</style>
