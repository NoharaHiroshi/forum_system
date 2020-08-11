export default{
	checkLogin(v){
		let user = v.$cookies.get('user');
		return typeof(user) !== 'undefined';
	},
	postAjax(v, url, postdata, callback){
		if(url.checklogin === true){
		    if(!this.checkLogin(v)){
                v.$router.push({name: 'login'});
                return;
            }
        }
		v.axios.post(url.router, postdata).then(function (response) {
            let data = response.data;
            if(data.code === "-99"){
                v.$notify({
                  title: '温馨提示',
                  message: data.msg,
                  type: 'warning'
                });
                v.$router.push({name: 'login'});
            }else{
                callback(response.data);
            }
		}).catch(function (error) {
		    console.log(error); 
            v.$notify.error({
                title: '请求失败',
                message: '请联系管理员'
            });
		});
	},
	getAjax(v, url, params, callback){
        if(url.checklogin === true){
            if(!this.checkLogin(v)){
                v.$router.push({name: 'login'});
                return;
            }
        }
		v.axios.get(url.router,{params:params}).then(function (response) {
            callback(response.data);
		}).catch(function (error) {
		    console.log(error); 
            v.$notify.error({
                title: '登录失败',
                message: '网络错误，请检查网络连接'
            });
		});

	},
    checkIdentityCodeValid(code){
        let city={11:"北京",12:"天津",13:"河北",14:"山西",15:"内蒙古",21:"辽宁",22:"吉林",23:"黑龙江 ",31:"上海",32:"江苏",33:"浙江",34:"安徽",35:"福建",36:"江西",37:"山东",41:"河南",42:"湖北 ",43:"湖南",44:"广东",45:"广西",46:"海南",50:"重庆",51:"四川",52:"贵州",53:"云南",54:"西藏 ",61:"陕西",62:"甘肃",63:"青海",64:"宁夏",65:"新疆",71:"台湾",81:"香港",82:"澳门",91:"国外 "};
        let tip = "";
        let pass= true;
  
        if(!code || !/^\d{6}(18|19|20)?\d{2}(0[1-9]|1[012])(0[1-9]|[12]\d|3[01])\d{3}(\d|X)$/i.test(code)){
            tip = "身份证号格式错误";
            pass = false;
        }
  
        else if(!city[code.substr(0,2)]){
            tip = "地址编码错误";
            pass = false;
        }else{
            //18位身份证需要验证最后一位校验位
            if(code.length === 18){
                code = code.split('');
                //∑(ai×Wi)(mod 11)
                //加权因子
                let factor = [ 7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2 ];
                //校验位
                let parity = [ 1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2 ];
                let sum = 0;
                let ai = 0;
                let wi = 0;
                for (let i = 0; i < 17; i++)
                {
                    ai = code[i];
                    wi = factor[i];
                    sum += ai * wi;
                }
                let last = parity[sum % 11];
                if(parity[sum % 11] !== code[17]){
                    tip = "校验位错误";
                    pass = false;
                }
            }
        }
        return pass;
    },
  
    // 检查合规字符：只能由大小写字母，数字，中文，下滑线组成
    /**
     * @return {boolean}
     */
    checkCommonCharValid(value){
        let reg = "^[0-9a-zA-Z\u4e00-\u9fa5_]+$";
        let re = new RegExp(reg);
        return re.test(value);
    },
  
    // 检查密码合规字符：不能由空格，中文字符
    /**
     * @return {boolean}
     */
    checkCommonPasswordValid(value){
        let reg = "[\u0391-\uFFE5]+";
        let re = new RegExp(reg);
        if(!re.test(value)){
            let reg1 = "^[0-9a-zA-Z_\\S]+$";
            let re1 = new RegExp(reg1);
            return re1.test(value);
        }else{
            return false;
        }
    }
}
