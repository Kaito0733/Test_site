from flask import Blueprint, request
import os

base_url = os.getenv("BASE_URL", "http://localhost:5000")
base_url1 = os.getenv("BASE_URL1", "http://localhost:5000")

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "<a href='/'>Home</a>"
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<a href='/'>Home</a>"
    return "<p>Logout</p>"

@auth.route(base_url1, methods=['GET', 'POST'])
def signup():
    fn = request.form.get("fname")
    ln = request.form.get("lname")
    return f"""
    <h1><a href='/'>Home</a><h1>
    Your name is {fn} {ln}
    """
    return "<p>Sign up</p>"
