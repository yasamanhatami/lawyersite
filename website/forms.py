from django import forms
from website.models import Cantact
from captcha.fields import CaptchaField

class NameForm(forms.Form):
    name = forms.CharField(max_length=225)
    email = forms.EmailField()
    subject = forms.CharField(max_length=225)
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    captcha = CaptchaField()
    class Meta:
        model = Cantact
        fields = '__all__'
