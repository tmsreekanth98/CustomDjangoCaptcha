from django import forms
from .models import Info

class InputForm(forms.Form):
	Name = forms.CharField(max_length=100)
	Roll_No = forms.CharField(max_length=100)


class Captcha_InputForm(forms.Form):
	Name = forms.CharField(max_length=100)
	Roll_No = forms.CharField(max_length=100)
	Captcha = forms.CharField(max_length=100)