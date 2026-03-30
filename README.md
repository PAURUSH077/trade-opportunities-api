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
---

## 📚 Learnings

During this project, I gained practical experience in:

* Building REST APIs using FastAPI
* Implementing authentication using Bearer tokens
* Designing rate limiting to handle API traffic efficiently
* Structuring backend projects using modular architecture
* Integrating external AI services with fallback mechanisms
* Handling environment variables securely using `.env`

---

## 🚧 Challenges Faced

### 1. OpenAI API Quota Issue

* Faced `429 insufficient_quota` error during AI analysis
* Since API keys cannot be shared, evaluator would also face this issue

✅ **Solution:**
Implemented a fallback mechanism to return predefined analysis when API fails

---

### 2. Securing API Keys

* Risk of exposing sensitive API keys while pushing to GitHub

✅ **Solution:**
Used `.gitignore` to exclude `.env` and followed secure key handling practices

---

### 3. Authentication Handling

* Ensuring only authorized users can access endpoints

✅ **Solution:**
Implemented Bearer token authentication and validated requests

---

### 4. Rate Limiting

* Preventing excessive API requests

✅ **Solution:**
Implemented rate limiting to return HTTP 429 after threshold

---

### 5. Git & Deployment Issues

* Faced issues with secret detection and push rejection

✅ **Solution:**
Removed sensitive data from commit history and restructured repository

---

## 💡 Key Takeaways

* Always design APIs to work even if external services fail
* Security (API keys, authentication) is critical in backend systems
* Proper error handling improves reliability and user experience
* Clean project structure improves maintainability
* Real-world backend systems must handle edge cases gracefully

---


## 👤 Author

**Paurush Mishra**
