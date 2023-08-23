from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Title')
    description = forms.CharField(label="description", widget=forms.Textarea)