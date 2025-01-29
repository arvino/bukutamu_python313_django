from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Member, BukuTamu

class MemberRegistrationForm(UserCreationForm):
    class Meta:
        model = Member
        fields = ('email', 'username', 'phone', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Member.objects.filter(email=email).exists():
            raise forms.ValidationError('Email sudah terdaftar')
        return email

class BukuTamuForm(forms.ModelForm):
    class Meta:
        model = BukuTamu
        fields = ['messages', 'gambar']
        widgets = {
            'messages': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Tulis pesan Anda di sini'
            }),
            'gambar': forms.FileInput(attrs={
                'class': 'form-control'
            })
        }

class MemberUpdateForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['username', 'phone']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'})
        } 