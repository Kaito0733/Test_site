from flask import Blueprint

views = Blueprint("views", __name__)

#in brackets the URL for homepage:
@views.route("/")
def home():
    return "<h1>Test<h1>"




