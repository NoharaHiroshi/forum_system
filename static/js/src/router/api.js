var root = '/';

export default{
  user: {
    checkUserName:{
      router:root+'/user/checkUserNameValid',
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
    }
  }
}
