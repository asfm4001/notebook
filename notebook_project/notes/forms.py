from django import forms
from django.contrib.auth.models import User
from notes.models import *

# class NoteForm(forms.Form):
#     title = forms.CharField(max_length=20, required=True)
#     content = forms.CharField(max_length=500, )

class NoteForm(forms.ModelForm):
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if not title:
            raise forms.ValidationError('Title 不可空白!!!')
        note = Note.objects.filter(title=title).first()
        if note:
            raise forms.ValidationError('Title 已存在!!!')
        return title
    def clean_category(self):
        category = self.cleaned_data.get('category')
        if not category:
            raise forms.ValidationError("Category不可空白")
        return category
    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) < 11:
            raise forms.ValidationError('Content 需大於10個字元!!!')
        return content
    def clean(self):
        clean_date = super().clean()
        title = self.cleaned_data.get('title')
        content = self.cleaned_data.get('content')
        if title and content and title in content:
            raise forms.ValidationError('內容不可包含Title!!!')
        return clean_date
    class Meta:
        model = Note
        # fields = '__all__'
        fields = ['title', 'category', 'content']