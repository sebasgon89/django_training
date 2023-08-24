from django import forms

class CreateNewTask(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'class':'input'}))
    description = forms.CharField(label="description", widget=forms.Textarea(attrs={'class':'input'}))

class CreateNewProject(forms.Form):
    name = forms.CharField(label='name', widget=forms.TextInput(attrs={'class':'input'}))