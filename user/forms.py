from django import forms
 
class UserForm(forms.Form):
    login = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","id":"login"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","id":"pass"}))