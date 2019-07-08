from django import forms

class ProfileForm(forms.Form):
	post = forms.CharField()