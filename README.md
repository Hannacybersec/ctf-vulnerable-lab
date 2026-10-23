# 🧪 CTF-Style Vulnerable Lab

A local cybersecurity training lab built with Python Flask and SQLite.

This project demonstrates common web security weaknesses in a controlled local environment and shows secure remediation techniques.

## 🎯 Challenges

### 1. Search Input Security — XSS

- Demonstrates unsafe HTML rendering in a controlled lab
- Shows how user input can become executable HTML
- Remediated using Jinja2 auto-escaping

### 2. Authentication Security

**Vulnerable version**
- Demonstrates weak hard-coded credential comparison

**Secure version**
- Uses Werkzeug password hashing
- Uses `check_password_hash()` for password verification
- Avoids storing plaintext passwords

### 3. Database Security

- Uses a local SQLite database
- Demonstrates user lookup functionality
- Uses parameterized SQL queries
- Helps prevent SQL injection

## 🛠️ Technologies

- Python
- Flask
- SQLite
- HTML/CSS
- Jinja2
- Werkzeug Security

## 🔐 Security Concepts

- Cross-Site Scripting (XSS)
- Input handling
- Authentication security
- Password hashing
- SQL injection prevention
- Parameterized queries
- Secure coding practices

## ▶️ Run the Lab

```bash
git clone <repository-url>
cd ctf-vulnerable-lab

python3 -m venv venv
source venv/bin/activate

pip install flask

python3 app.py

