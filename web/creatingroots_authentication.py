from flask import Blueprint, request
import os


auth = Blueprint("auth", __name__)
#views = Blueprint("views", __name__)

@auth.route("/login")
def login():
    return "<a href='/'>Home</a>"
    return "<p>Login</p>"

@auth.route("/logout")
def logout():
    return "<a href='/'>Home</a>"
    return "<p>Logout</p>"

@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    fn = request.form.get("fname")
    ln = request.form.get("lname")
    return f"""
    <h1><a href='/'>Home</a><h1>
    Your name is {fn} {ln}
    """
    return "<p>Sign up</p>"

