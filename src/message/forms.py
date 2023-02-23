from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    # user = forms.CharField(max_length=100, widget= forms.TextInput (attrs={'placeholder':'Name', 'class': "question__input", 'id': 'name'}))
    # text = forms.CharField(max_length=1000, widget= forms.Textarea (attrs={'placeholder':'Message', 'class': "question__input", 'id': 'message'}))
    
    class Meta:
        model = Message
        fields = ['user', 'text']
