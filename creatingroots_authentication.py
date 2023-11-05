from flask import Blueprint, request

auth = Blueprint("auth", __name__)

@auth.route("https://othernamedisplayer.onrender.com/login")
def login():
    return "<a href='/'>Home</a>"
    return "<p>Login</p>"

@auth.route("https://othernamedisplayer.onrender.com/logout")
def logout():
    return "<a href='/'>Home</a>"
    return "<p>Logout</p>"

@auth.route("https://othernamedisplayer.onrender.com/sign-up", methods=['GET', 'POST'])
def signup():
    fn = request.form.get("fname")
    ln = request.form.get("lname")
    return f"""
    <h1><a href='/'>Home</a><h1>
    Your name is {fn} {ln}
    """
    return "<p>Sign up</p>"

