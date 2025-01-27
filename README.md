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

## Setup Environment

### Prasyarat
1. Python 3.13
2. MySQL/MariaDB
3. Visual Studio Code
4. Git

### Setup VSCode

1. Install ekstensi yang diperlukan:
   - Python (ms-python.python)
   - Django (batisteo.vscode-django)
   - MySQL (cweijan.vscode-mysql-client2)
   - Git (eamodio.gitlens)
   - Live Server (ritwickdey.liveserver)

2. Konfigurasi ekstensi Python:
   ```json
   {
     "python.linting.enabled": true,
     "python.linting.pylintEnabled": true,
     "python.formatting.provider": "black",
     "python.formatting.blackArgs": ["--line-length", "100"],
     "editor.formatOnSave": true,
     "[python]": {
       "editor.defaultFormatter": "ms-python.python"
     }
   }
   ```

3. Setup Git di VSCode:
   - Login ke GitHub
   - Konfigurasi user.name dan user.email
   - Setup SSH key jika diperlukan

### Setup Database
1. Buat database baru:
```sql
CREATE DATABASE bukutamu_django;
CREATE USER 'arvino'@'localhost' IDENTIFIED BY 'arvino1345';
GRANT ALL PRIVILEGES ON bukutamu_django.* TO 'arvino'@'localhost';
FLUSH PRIVILEGES;
```

## Setup Aplikasi

1. Clone repositori:
```bash
git clone https://github.com/arvino/bukutamu-django.git
cd bukutamu-django
```

2. Buat virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependensi:
```bash
pip install -r requirements.txt
```

4. Setup environment variables (.env):
```
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

5. Jalankan migrasi:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Buat superuser:
```bash
python manage.py createsuperuser
```

7. Jalankan server:
```bash
python manage.py runserver
```

## Flow Aplikasi

### 1. Flow Pengunjung
- Mengakses halaman utama (/)
- Melihat daftar pesan tamu
- Melihat detail pesan dan gambar
- Opsi untuk register/login

### 2. Flow Member
- Register akun baru
  - Isi form registrasi
  - Terima email selamat datang
  - Login dengan akun baru
- Login ke dashboard member
  - Lihat riwayat pesan
  - Submit pesan baru (1x sehari)
  - Upload gambar dengan preview
  - Edit/hapus pesan sendiri
- Update profil
  - Edit informasi pribadi
  - Ganti password

### 3. Flow Admin
- Login sebagai admin
- Akses dashboard admin
  - Lihat semua pesan
  - Filter dan cari pesan
  - Export data (CSV/Excel/PDF)
- Manajemen member
  - Lihat daftar member
  - Aktifkan/nonaktifkan member
  - Reset password member
- Terima notifikasi
  - Email untuk member baru
  - Telegram untuk pesan baru

### 4. Flow API
- Autentikasi dengan JWT
- Akses endpoint CRUD
- Upload file via API
- Refresh token

## Struktur Database

### Tabel Member
- nama (CharField)
- phone (CharField)
- email (EmailField)
- password (CharField)
- role (CharField)

### Tabel BukuTamu
- member_id (ForeignKey)
- messages (TextField)
- gambar (ImageField)
- timestamp (DateTimeField)

## API Endpoints

- `POST /api/token/` - Mendapatkan token JWT
- `POST /api/token/refresh/` - Refresh token JWT
- `GET /api/bukutamu/` - List semua pesan
- `POST /api/bukutamu/` - Tambah pesan baru
- `GET /api/bukutamu/{id}/` - Detail pesan
- `PUT /api/bukutamu/{id}/` - Update pesan
- `DELETE /api/bukutamu/{id}/` - Hapus pesan
- `GET /api/members/` - List member (admin only)

## Pengembangan Selanjutnya

- Implementasi email verification
- Fitur lupa password
- Export data ke PDF/Excel
- Integrasi dengan media sosial
- Sistem komentar
- Notifikasi real-time
- Unit testing
- Deployment guide


## Struktur File Proyek

```
bukutamu/
├── bukutamu/                  # Project root
│   ├── __init__.py
│   ├── settings.py           # Konfigurasi proyek
│   ├── urls.py              # URL router utama
│   ├── asgi.py             # ASGI config
│   └── wsgi.py             # WSGI config
│
├── tamu/                     # Aplikasi utama
│   ├── migrations/          # Database migrations
│   ├── templates/          # Template HTML
│   │   ├── tamu/
│   │   │   ├── base.html              # Template dasar
│   │   │   ├── public_list.html       # Halaman publik
│   │   │   ├── register.html          # Form registrasi
│   │   │   ├── member_dashboard.html  # Dashboard member
│   │   │   ├── admin_dashboard.html   # Dashboard admin
│   │   │   ├── submit_entry.html      # Form input pesan
│   │   │   ├── edit_entry.html        # Form edit pesan
│   │   │   └── profile.html           # Halaman profil
│   │   ├── registration/
│   │   │   └── login.html             # Form login
│   │   └── emails/
│   │       ├── welcome.html           # Template email welcome
│   │       └── new_entry.html         # Template notifikasi
│   │
│   ├── static/             # File statis
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   │
│   ├── __init__.py
│   ├── admin.py           # Konfigurasi admin
│   ├── apps.py           # Konfigurasi aplikasi
│   ├── forms.py          # Form definitions
│   ├── models.py         # Model database
│   ├── views.py          # View handlers
│   ├── urls.py           # URL patterns
│   ├── api_urls.py       # API endpoints
│   ├── permissions.py    # Custom permissions
│   ├── serializers.py    # API serializers
│   ├── middleware.py     # Custom middleware
│   ├── utils.py          # Utility functions
│   ├── notifications.py  # Notification handlers
│   └── context_processors.py  # Template context
│
├── media/                # Upload files
│   └── bukutamu/        # Gambar pesan
│
├── static/              # Project static files
│   ├── css/
│   ├── js/
│   └── img/
│
├── docs/               # Dokumentasi
│   └── api.md         # Dokumentasi API
│
├── requirements.txt    # Dependencies
├── manage.py          # Django CLI
├── .env              # Environment variables
├── .gitignore       # Git ignore rules
└── README.md        # Dokumentasi proyek
```

Struktur file di atas menunjukkan organisasi kode dalam proyek:

- `bukutamu/`: Root proyek Django
- `tamu/`: Aplikasi utama yang berisi logika bisnis
- `templates/`: File-file template HTML
- `static/`: File statis (CSS, JavaScript, gambar)
- `media/`: File yang diupload user
- `docs/`: Dokumentasi proyek
- File konfigurasi lainnya di root proyek

### Penjelasan File Utama

1. **Settings & URLs**
   - `settings.py`: Konfigurasi utama Django
   - `urls.py`: Routing URL utama
   - `api_urls.py`: Routing untuk API endpoints

2. **Models & Forms**
   - `models.py`: Definisi model database
   - `forms.py`: Form untuk input data
   - `serializers.py`: Serializer untuk API

3. **Views & Templates**
   - `views.py`: Logic untuk handle request
   - `templates/*.html`: Template untuk UI
   - `static/*`: Asset statis (CSS/JS)

4. **Utilities**
   - `utils.py`: Fungsi helper
   - `notifications.py`: Handler notifikasi
   - `permissions.py`: Custom permissions
   - `middleware.py`: Custom middleware

5. **Configuration**
   - `.env`: Environment variables
   - `requirements.txt`: Dependencies
   - `.gitignore`: File yang diabaikan Git


## Kontribusi

Silakan berkontribusi dengan membuat pull request atau melaporkan issue.

## Lisensi

[MIT License](LICENSE)

## Dibuat Oleh
- Developer Name : Arvino Zulka
- Email: arvinozulka@gmail.com 
- Website: https://www.arvino.my.id/
- GitHub: https://github.com/arvino
