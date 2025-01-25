from django.db import models

class Tamu(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    pesan = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama 