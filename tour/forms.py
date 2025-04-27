from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Ismingizni kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control p-4', 'placeholder': 'Email manzilingizni kiriting'}),
            'subject': forms.TextInput(attrs={'class': 'form-control p-4', 'placeholder': 'Mavzuni kiriting'}),
            'message': forms.Textarea(attrs={'class': 'form-control py-3 px-4', 'rows': 5, 'placeholder': 'Xabaringizni yozing'}),
        }
        labels = {
            'name': 'Ism',
            'email': 'Email',
            'subject': 'Mavzu',
            'message': 'Xabar',
        }
