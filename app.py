from flask import Flask, render_template, request
import sqlite3
from werkzeug.security import check_password_hash

app = Flask(__name__)

DEMO_USERNAME = "admin"
DEMO_PASSWORD_HASH = "scrypt:32768:8:1$JZigo4i8dobm3cp9$c1ddc52fc9da36fc9248c58fe070f676da9ba778b135777db377bd3464cad20ef99a752462449d5bde60fb854cbd3e5f2516d07436ebefc304371c40cd83a4a3"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "")
    return render_template("search.html", query=query)

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == "admin" and password == "admin123":
            return "Login successful - CTF authentication challenge"

        return "Login failed"

    return render_template("login.html")

@app.route("/database")
def database():
    username = request.args.get("username", "")
    conn = sqlite3.connect("ctf_lab.db")
    cursor = conn.cursor()

    query = "SELECT id, username, role FROM users WHERE username = ?"
    cursor.execute(query, (username,))
    user = cursor.fetchone()

    conn.close()

    return render_template("database.html", username=username, user=user)

@app.route("/secure-login", methods=["GET", "POST"])
def secure_login():
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        if username == DEMO_USERNAME and check_password_hash(DEMO_PASSWORD_HASH, password):
            return "Secure login successful - password verified using hashing"

        return "Secure login failed"

    return render_template("secure_login.html")

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
