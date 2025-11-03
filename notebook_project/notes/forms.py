from django import forms

class NoteForm(forms.Form):
    title = forms.CharField(max_length=20, required=True)
    content = forms.CharField(max_length=500)