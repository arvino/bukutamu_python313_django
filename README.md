# Aplikasi Buku Tamu Django

Aplikasi buku tamu berbasis web menggunakan Django dan MySQL dengan fitur member dan admin.

## Overview Aplikasi

Aplikasi Buku Tamu ini memiliki beberapa fitur utama:

### Fitur Publik
- Halaman publik untuk melihat daftar pesan tamu
- Tampilan responsif dengan Bootstrap 5
- Dukungan upload gambar untuk setiap pesan

### Fitur Member
- Sistem autentikasi (login/register)
- Dashboard khusus member
- Pembatasan posting (1x sehari)
- Edit dan hapus pesan sendiri
- Update profil member

### Fitur Admin
- Dashboard admin untuk manajemen data
- Export data ke CSV, Excel dan PDF
- Manajemen member dan pesan
- Statistik penggunaan

### Fitur Notifikasi
- Notifikasi email untuk member baru
- Notifikasi Telegram untuk pesan baru
- Email notifikasi ke admin

### API & Integrasi
- REST API dengan JWT auth
- Integrasi Telegram Bot
- Upload gambar dengan preview

## Teknologi yang Digunakan

- Python 3.13
- Django 4.2
- MySQL/MariaDB
- Bootstrap 5
- jQuery 3.7.1
- REST Framework
- JWT Authentication
- Bootstrap Icons

## Langkah-langkah Instalasi

### 1. Setup Environment

```bash
# Buat direktori proyek
mkdir bukutamu_django
cd bukutamu_django

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 2. Install Dependencies

```bash
# Install Django
pip install Django==4.2.0

# Install semua dependencies
pip install -r requirements.txt
```

### 3. Setup Database MySQL

```sql
CREATE DATABASE bukutamu_django;
CREATE USER 'arvino'@'localhost' IDENTIFIED BY 'arvino1345';
GRANT ALL PRIVILEGES ON bukutamu_django.* TO 'arvino'@'localhost';
FLUSH PRIVILEGES;
```

### 4. Konfigurasi Proyek

1. Buat file `.env` di root proyek:
```env
SECRET_KEY=your-secret-key-here
DEBUG=True
DB_NAME=bukutamu_django
DB_USER=arvino
DB_PASSWORD=arvino1345
DB_HOST=localhost
DB_PORT=3306
TELEGRAM_BOT_TOKEN=your_bot_token
TELEGRAM_CHAT_ID=your_chat_id
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

2. Jalankan migrasi database:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Buat superuser:
```bash
python manage.py createsuperuser
```

4. Jalankan development server:
```bash
python manage.py runserver
```

## Struktur URL

- `/` - Halaman publik
- `/login/` - Halaman login
- `/register/` - Halaman registrasi
- `/member/` - Dashboard member
- `/admin-dashboard/` - Dashboard admin
- `/profile/` - Halaman profil
- `/submit/` - Form submit pesan
- `/edit/<id>/` - Form edit pesan

## API Endpoints

- `POST /api/token/` - Get JWT token
- `POST /api/token/refresh/` - Refresh JWT token
- `GET /api/bukutamu/` - List semua pesan
- `POST /api/bukutamu/` - Tambah pesan baru
- `GET /api/bukutamu/{id}/` - Detail pesan
- `PUT /api/bukutamu/{id}/` - Update pesan
- `DELETE /api/bukutamu/{id}/` - Hapus pesan

## Troubleshooting

### Error Database
```bash
# Reset database
python manage.py flush

# Recreate migrations
python manage.py makemigrations
python manage.py migrate
```

### Error Dependencies
```bash
# Update pip
python -m pip install --upgrade pip

# Install dependencies satu per satu
pip install Django==4.2.0
pip install mysqlclient==2.2.0
pip install djangorestframework==3.14.0
pip install Pillow
```

### Error Static Files
```bash
python manage.py collectstatic
```

## Keamanan

- Gunakan HTTPS di production
- Ganti SECRET_KEY
- Nonaktifkan DEBUG di production
- Batasi upload file
- Validasi input user
- Rate limiting API

## Maintenance

- Backup database secara berkala
- Monitor error logs
- Update dependencies
- Bersihkan file media yang tidak terpakai
- Optimalkan query database

## Kontribusi

Silakan berkontribusi dengan membuat pull request atau melaporkan issue.



## Dibuat Oleh
- Developer Name : Arvino Zulka
- Email: arvinozulka@gmail.com 
- Website: https://www.arvino.my.id/
- GitHub: https://github.com/arvino
