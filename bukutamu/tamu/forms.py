from django import forms
from .models import Tamu

class TamuForm(forms.ModelForm):
    class Meta:
        model = Tamu
        fields = ['nama', 'email', 'pesan']
        widgets = {
            'nama': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan nama lengkap'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Masukkan alamat email'
            }),
            'pesan': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tulis pesan Anda di sini',
                'rows': 4
            })
        }
        labels = {
            'nama': 'Nama Lengkap',
            'email': 'Alamat Email',
            'pesan': 'Pesan'
        } 