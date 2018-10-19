from django import forms
from user.models import UserModel


# 用户注册表单验证
# class UserRegisterForm(forms.Form):
#     username = forms.CharField(max_length=10)
#     password = forms.CharField(max_length=10)
#     email = forms.EmailField()

class UserRegisterModelForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = '__all__'

