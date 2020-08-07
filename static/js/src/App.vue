<template>
  <div id="app" style="position:absolute; left:0; top:0; width:100%;height:100%;">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
html {
  padding: 0;
  margin: 0;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
}
body {
  font: 100% Helvetica, sans-serif;
  font-family: "Helvetica Neue",Helvetica,"PingFang SC","Hiragino Sans GB","Microsoft YaHei","微软雅黑",Arial,sans-serif;
  color: #606266;
  padding: 0;
  margin: 0;
  background-color: #F5F5F5;
  font-size: 12px;
}

a {
  text-decoration: none;
  color: #409EFF;
}

a:hover {
  color: #dc4100;
  -webkit-transition: all 0.5s;
  -moz-transition: all 0.5s;
  -o-transition: all 0.5s;
  transition: all 0.5s;
}
</style>
