$(function(){

    var user_error = false;
    var password_error = false;

    $('.name_input').blur(function () {
        //$(this)表示当前操作的input标签
        if($(this).val()== ''){
            $('.user_error').html('请输入用户名').show();
            user_error = true;
        }else{
            //隐藏错误信息
            $('.user_error').hide();
            user_error = false;
        }
    });

    $('.pass_input').blur(function () {
        if($(this).val()== ''){
            $('.pwd_error').html('请输入密码').show();
            password_error = true;
        }else{
            $('.pwd_error').hide();
            password_error = false;
        }
    });

    $('form').submit(function () {
        username = $('.name_input').val();
        password = $('.pass_input').val();
        if(username==''){
            user_error = true;
        }
        if(password==''){
            password_error = true;
        }
        if(user_error==false && password_error==false){
            return true;
        }else{
            return false;
        }
    });


});

