from django import forms
from .models import Message
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV2Checkbox
class MessageForm(forms.ModelForm):
    # user = forms.CharField(max_length=100, widget= forms.TextInput (attrs={'placeholder':'Name', 'class': "question__input", 'id': 'name'}))
    # text = forms.CharField(max_length=1000, widget= forms.Textarea (attrs={'placeholder':'Message', 'class': "question__input", 'id': 'message'}))
    
    class Meta:
        model = Message
        fields = ['user', 'text']
  
class CapatchaForm(forms.Form):
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox)
