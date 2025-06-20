# 🐍 Flask Microservice

Bu proje, Flask ile geliştirilmiş bir RESTful API servisidir. Kullanıcı yönetimi (register/login), JWT ile kimlik doğrulama, dummy veriler üzerinden albüm CRUD işlemleri gibi özellikler içerir. SQLite veritabanı kullanılarak hızlı ve sade bir backend API ortamı sağlanır.

## 🚀 Başlangıç

### Ortam Değişkenleri (.env)
.env.example dosyasının ismini `.env` dosyası olarak değiştirin:

```env
FLASK_ENV=development
FLASK_DEBUG=True
FLASK_PORT=5050
SECRET_KEY=super-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```

### Kurulum
İşte proje ortamını kurmak için **Mac/Linux** ve **Windows** için ayrı ayrı açıklanmış kurulum adımları:

---

### 🚀 Kurulum Adımları

#### 🐧 Mac / Linux

```bash
# 1. Sanal ortam oluştur
python3 -m venv venv

# 2. Ortamı aktif et
source venv/bin/activate

# 3. Gereksinimleri yükle
pip install -r requirements.txt
```

#### 🪟 Windows (CMD)

```cmd
:: 1. Sanal ortam oluştur
python -m venv venv

:: 2. Ortamı aktif et
venv\Scripts\activate.bat

:: 3. Gereksinimleri yükle
pip install -r requirements.txt
```

#### 🪟 Windows (PowerShell)

```powershell
# 1. Sanal ortam oluştur
python -m venv venv

# 2. Ortamı aktif et
venv\Scripts\Activate.ps1

# 3. Gereksinimleri yükle
pip install -r requirements.txt
```


### Sunucuyu Başlat
```bash
python run.py
```

## 🔐 Auth İşlemleri

### Kullanıcı Oluştur (Register)
```bash
curl -X POST http://localhost:5050/api/auth/register -H "Content-Type: application/json" -d '{"name": "John", "email": "john@example.com", "password": "123456"}'
```

### Giriş Yap (Login)
```bash
curl -X POST http://localhost:5050/api/auth/login -H "Content-Type: application/json" -d '{"email": "john@example.com", "password": "123456"}'
```

## 🎵 Albüm İşlemleri (Token gerekli)

### Albümleri JSONPlaceholder'dan çek ve kaydet
```bash
curl -X POST http://localhost:5050/api/albums/fetch -H "Authorization: Bearer <JWT_TOKEN>"
```

### Albüm Listele
```bash
curl -X GET http://localhost:5050/api/albums -H "Authorization: Bearer <JWT_TOKEN>"
```

### Albüm Oluştur
```bash
curl -X POST http://localhost:5050/api/albums -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json" -d '{"title": "My Album"}'
```

### Albüm Güncelle
```bash
curl -X PUT http://localhost:5050/api/albums/1 -H "Authorization: Bearer <JWT_TOKEN>" -H "Content-Type: application/json" -d '{"title": "Updated Album"}'
```

### Albüm Sil
```bash
curl -X DELETE http://localhost:5050/api/albums/1 -H "Authorization: Bearer <JWT_TOKEN>"
```

## 📁 Proje Yapısı

```
flask-microservice/
├── app/
│   ├── routes/
│   ├── models/
│   ├── services/
│   ├── schemas/
│   ├── extensions.py
│   └── main.py
├── config.py
├── run.py
├── requirements.txt
└── README.md
```
