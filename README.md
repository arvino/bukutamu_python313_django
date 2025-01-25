# Aplikasi Buku Tamu Django

Aplikasi buku tamu sederhana yang dibuat menggunakan Django, MySQL, Bootstrap 5, dan jQuery.

## Persyaratan Sistem

- Python 3.13
- Django
- MySQL
- mysqlclient

## Teknologi yang Digunakan

- Django - Web framework
- MySQL - Database
- Bootstrap 5 - Frontend framework
- jQuery 3.7.1 - JavaScript library
- Bootstrap Icons - Icon library

## Instalasi

1. Clone repositori ini
2. Buat virtual environment (opsional tapi direkomendasikan):
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependensi:
```bash
pip install django mysqlclient
```

4. Buat database MySQL:
```sql
CREATE DATABASE bukutamu_django;
```

5. Sesuaikan konfigurasi database di `bukutamu/settings.py` jika diperlukan:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'bukutamu_django',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

6. Jalankan migrasi:
```bash
python manage.py makemigrations
python manage.py migrate
```

7. Jalankan server development:
```bash
python manage.py runserver
```

## Penggunaan

Buka browser dan akses:
- http://localhost:8000/ - untuk melihat daftar tamu
- http://localhost:8000/tambah/ - untuk menambah tamu baru

## Fitur

- Menampilkan daftar tamu dalam layout card responsif
- Form input tamu dengan validasi
- Pencatatan waktu otomatis
- Tampilan modern dengan Bootstrap 5
- Animasi dan efek visual dengan jQuery
- Navigasi responsif
- Validasi form client-side
- Feedback visual untuk interaksi pengguna
- Icon untuk meningkatkan UX

## Struktur Proyek

```
bukutamu/
├── bukutamu/           # Konfigurasi utama proyek
│   ├── settings.py     # Pengaturan proyek
│   └── urls.py         # URL routing
└── tamu/               # Aplikasi tamu
    ├── models.py       # Model database
    ├── views.py        # Logic aplikasi
    ├── forms.py        # Form input
    └── templates/      # Template HTML
        └── tamu/
            ├── base.html         # Template dasar
            ├── daftar_tamu.html  # Halaman daftar
            └── tambah_tamu.html  # Form tambah
```

## Komponen Frontend

- **Bootstrap 5**: Framework CSS untuk tampilan responsif
- **jQuery**: Library JavaScript untuk manipulasi DOM dan animasi
- **Bootstrap Icons**: Library icon untuk UI
- **Custom CSS**: Styling tambahan untuk penyesuaian tampilan
- **Custom JavaScript**: Validasi form dan animasi

## Pengembangan Selanjutnya

Beberapa fitur yang bisa ditambahkan:
- Autentikasi pengguna
- Validasi form yang lebih lengkap
- Fitur edit dan hapus data
- Pencarian dan filter data
- Pagination untuk daftar tamu
- Export data ke PDF/Excel
- API endpoint
- Unit testing
- Dark mode theme
- Integrasi dengan layanan email
- Captcha untuk keamanan form

## Kontribusi

Silakan berkontribusi dengan:
1. Fork repositori
2. Buat branch fitur (`git checkout -b fitur-baru`)
3. Commit perubahan (`git commit -am 'Menambah fitur baru'`)
4. Push ke branch (`git push origin fitur-baru`)
5. Buat Pull Request

## Lisensi

[MIT License](LICENSE)

## Kredit

- [Bootstrap](https://getbootstrap.com/)
- [jQuery](https://jquery.com/)
- [Bootstrap Icons](https://icons.getbootstrap.com/)
- [Django](https://www.djangoproject.com/)