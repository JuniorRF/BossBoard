from django import forms
from .models import Call

class CallForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['date', 'full_name', 'question', 'telephone', 'result']
        widgets = {
            'date': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'full_name': forms.TextInput(attrs={'class': 'form-control'}),
            'question': forms.Textarea(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'result': forms.Textarea(attrs={'class': 'form-control'}),
        }
