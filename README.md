# 🚀 Trade Opportunities API

<p align="center">
  <b>Sector-Based Trade Analysis API with Authentication & Rate Limiting</b><br>
  Built using FastAPI 🚀
</p>

<p align="center">
  <img src="https://img.shields.io/badge/FastAPI-0.110-green?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/Python-3.13-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/API-Secured-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Rate%20Limited-Yes-orange?style=for-the-badge">
</p>

---

## 📌 Overview

This project is a backend API that generates **trade opportunity reports** for different sectors (e.g., Technology in India).

It includes:

* 🔐 Authentication (Bearer Token)
* ⏱️ Rate Limiting
* 🧠 AI-based analysis (with fallback support)
* 📊 Structured sector insights

---

## ✨ Features

* 🔐 Secure API using Bearer Authentication
* ⏱️ Built-in Rate Limiting (HTTP 429)
* 🧠 AI-powered Market Analysis
* ⚡ FastAPI + Swagger UI
* 📦 Clean Modular Architecture

---

## 🛠️ Tech Stack

| Technology | Usage                            |
| ---------- | -------------------------------- |
| Python     | Core language                    |
| FastAPI    | API framework                    |
| Uvicorn    | Server                           |
| OpenAI     | AI analysis (fallback supported) |
| dotenv     | Environment variables            |

---

## ▶️ Getting Started

```bash
git clone https://github.com/PAURUSH077/trade-opportunities-api.git
cd trade-opportunities-api

python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt
uvicorn app.main:app --reload
```

---

## 🌐 API Docs

👉 http://127.0.0.1:8000/docs

---

## 🔐 Authentication Flow

### ❌ Without Token (401 Unauthorized)

![Unauthorized](./screenshots/unauthorized.png)

```json
{
  "detail": "Not authenticated"
}
```

---

### 🔑 Provide Bearer Token

![Authorization](./screenshots/auth.png)

* Click **Authorize**
* Enter token
* Access secured endpoints

---

## 📊 Endpoint

### `GET /analyze/{sector}`

Example:

```
/analyze/technology
```

---

## ✅ Successful Response (200 OK)

![Success](./screenshots/success.png)

```
# Trade Opportunities Report: Technology (India)

## 🧠 Market Analysis
The technology sector in India is showing stable growth...

## 📌 Summary
AI-generated insights for trading opportunities...
```

---

## ⏱️ Rate Limiting (429)

![Rate Limit](./screenshots/rate-limit.png)

```json
{
  "detail": "Too many requests. Try again later."
}
```

---

## 🧠 AI Integration

* Uses OpenAI for generating insights
* Includes fallback mechanism if quota is exceeded
* Ensures uninterrupted API response

---

## 📁 Project Structure

```
app/
 ├── main.py
 ├── routes.py
 ├── auth.py
 ├── rate_limiter.py
 ├── services/
 │    ├── ai_analyzer.py
 │    ├── data_collector.py
 │    └── report_generator.py
 └── utils/
      └── validators.py
```

---

## 🏁 Conclusion

This project demonstrates:

* Backend API design
* Secure authentication
* Rate limiting implementation
* AI integration with fallback

---

## 👤 Author

**Paurush Mishra**
