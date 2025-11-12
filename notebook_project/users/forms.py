from django import forms
from django.contrib.auth.models import User
class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            "password": forms.PasswordInput(attrs={
                'placeholder': '密碼長度區間6-20個字元',
            }),
        }
    def clean_username(self):
        username = self.cleaned_data.get("username")
        user = User.objects.filter(username=username).first()
        if user:
            raise forms.ValidationError("此帳號已被使用，請重新輸入")
        return username
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user