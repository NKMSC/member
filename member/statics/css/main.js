function checkInput(){


	


	var input_text = $('input[type="text"]');
	var gender = $('input[name="gender"]');
	var joinus = $('input[name="joinus"');
	var password = $('#password');
	var passwd_repeat = $('#passwd_repeat');
	
	for(var i = 0; i < input_text.length; i++){
		if(input_text[i].value == ""){
			errF(input_text[i].name);
			return false;
		}
	}
	if(password.val() == "" || passwd_repeat.val() == ""){
		errF('password');
		return false;
	}
	if(password.val() != passwd_repeat.val()){
		errF("passwd_repeat");
		return false;
	}
	if(gender.val() == null){
		errF('gender');
		return false;
	}
	return true;
}

function errF(msg){
	var err = '请填写正确的';
	switch (msg){
		case 'email':
			err += '邮箱';
		break;
		case 'student_id':
			err += '学号';
		break;
		case 'mobile':
			err += '手机号';
		break;
		case 'gender':
			err += '性别';
		break;
		case 'name':
			err += '昵称';
		break;
		case 'real_name':
			err += '真实姓名';
		break;
		case 'password':
			err += '密码';
		break;
		case 'passwd_repeat':
			err = '两次密码不一致';
		break;
	}
	alert(err);
	
}