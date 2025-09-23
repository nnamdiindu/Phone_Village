import os
from flask import Flask, render_template

app = Flask(__name__)

app.secret_key = os.environ.get("SECRET_KEY")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run(debug=True)