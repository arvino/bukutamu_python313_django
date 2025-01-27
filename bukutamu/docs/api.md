# Dokumentasi API Buku Tamu

## Autentikasi

Semua endpoint API memerlukan autentikasi JWT (JSON Web Token).

### Mendapatkan Token

```http
POST /api/token/
```

**Request Body:**
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

**Response:**
```json
{
    "access": "access_token_here",
    "refresh": "refresh_token_here"
}
```

### Refresh Token

```http
POST /api/token/refresh/
```

**Request Body:**
```json
{
    "refresh": "your_refresh_token"
}
```

## Endpoints

### List Buku Tamu

```http
GET /api/bukutamu/
```

**Headers:**
```
Authorization: Bearer your_access_token
```

**Response:**
```json
[
    {
        "id": 1,
        "member": {
            "username": "user1",
            "email": "user1@example.com"
        },
        "messages": "Pesan buku tamu",
        "gambar": "url_to_image",
        "timestamp": "2024-01-20T10:00:00Z"
    }
]
```

### Detail Buku Tamu

```http
GET /api/bukutamu/{id}/
```

### Tambah Buku Tamu

```http
POST /api/bukutamu/
```

**Request Body:**
```json
{
    "messages": "Pesan baru",
    "gambar": "file_upload"
}
```

### Update Buku Tamu

```http
PUT /api/bukutamu/{id}/
```

### Hapus Buku Tamu

```http
DELETE /api/bukutamu/{id}/
```

### List Member (Admin Only)

```http
GET /api/members/
```

## Status Codes

- 200: Success
- 201: Created
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Server Error 