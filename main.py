from flask import Flask
from creating_roots_view import views
from creatingroots_authentication import auth

def create_app():
    app = Flask(__name__)
    app.register_blueprint(views)
    app.register_blueprint(auth)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=False)

