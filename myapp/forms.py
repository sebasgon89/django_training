from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Title')
    description = forms.CharField(label="description", widget=forms.Textarea)

class CreateNewProject(forms.Form):
    name = forms.CharField(label='name')