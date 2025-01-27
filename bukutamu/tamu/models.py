from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.utils import timezone

class Member(AbstractUser):
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Nomor telepon harus dalam format: '+999999999'. Maksimal 15 digit."
    )
    
    phone = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    role = models.CharField(max_length=10, choices=[('member', 'Member'), ('admin', 'Admin')], default='member')
    
    def __str__(self):
        return self.email

class BukuTamu(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    messages = models.TextField()
    gambar = models.ImageField(upload_to='bukutamu_images/')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.member.email} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"

    def can_submit_today(self):
        today = timezone.now().date()
        return not BukuTamu.objects.filter(
            member=self.member,
            timestamp__date=today
        ).exists()

class Tamu(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    pesan = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama 