from django import forms
from .models import ClientRequest

class ClientRequestForm(forms.ModelForm):
    class Meta:
        model = ClientRequest
        fields = ['description', 'status']
        widgets = {
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите проблему...',
                'rows': 3
            }),
            'status': forms.Select(attrs={'class': 'form-control'})
        }