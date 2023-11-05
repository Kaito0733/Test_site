from flask import Blueprint
import os

base_url = os.getenv("BASE_URL", "http://localhost:5000")

views = Blueprint("views", __name__)

#in brackets the URL for homepage:
@views.route(f"{base_url}/")
def home():
    return f'''
    <h1><form action="{base_url}/sign-up" method="post"><h1>
    <h1><label for="firstname">First Name:</label><h1>
    <h1><input type="text" id="firstname" name="fname" placeholder="firstname"><h1>
    <h1><label for="lastname">Last Name:</label><h1>
    <h1><input type="text" id="lastname" name="lname" placeholder="lastname"><h1>
    <h1><button type="submit">Login</button><h1>
    '''
        
    
    return '''
    <html
    <head <title This is a test from KNS</title></head>
    <body>
        <h1><a href='https://othernamedisplayer.onrender.com/sign-up'>Go to Signup</a><h1>
        <h1><a href='https://othernamedisplayer.onrender.com/login'>Go to Login</a><h1>
    </body>
    </html>
    '''