# Secure Student Portal API

A simple FastAPI project where students can register, log in, and view their grades securely.

## 🚀 Features
- Register students (`POST /register/`)
- Secure login with HTTP Basic Auth (`POST /login/`)
- View grades (protected, requires login) (`GET /grades/`)
- Passwords stored as **hashed values**
- Data saved in `students.json`

