var root = '/api';

export default{
  user: {
    checkUserName:{
      router:root+'/user/checkUserNameValid',
      checklogin: false
    },
    checkUserEmail:{
      router:root+'/user/checkUserEmailValid',
      checklogin: false
    },
    login: {
      router: root + '/user/login',
      checklogin: false
    },
    logout: {
      router: root + '/user/logout',
      checklogin: true
    },
    register: {
      router: root + '/user/register',
      checklogin: false
    },
    getCaptcha: {
      router: root + '/user/getCaptcha',
      checklogin: false
    }
  },
  website: {
    index: {
      router: root + '/index',
      checklogin: false
    },
    forum: {
      router: root + '/forum',
      checklogin: false
    },
    submitPost: {
      router: root + '/submit_post',
      checklogin: true,
    },
    getPost: {
      router: root + '/edit_post',
      checklogin: true,
    }
  }
}
