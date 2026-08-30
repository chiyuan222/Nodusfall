from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="邮箱", required=True)
    nickname = forms.CharField(label="昵称", max_length=50, required=False)

    class Meta:
        model = User
        fields = ["username", "email", "nickname", "password1", "password2"]
        help_texts = {
            "username": "用于登录的用户名",
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("该邮箱已被注册")
        return email
