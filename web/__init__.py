from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "phwbu5101111015ubwhp357"
    
    #import all the blueprints into app
    from .creating_roots_view import views
    from .creatingroots_authentication import auth

    #registering blueprints with url's (to acces them)
    app.register_blueprint(views, urlprefix="/")
    app.register_blueprint(auth, urlprefix="/")

    return app