from flask import Flask, render_template, redirect
import stripe

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

@app.route("/cancel")
def cancel():
    return render_template("cancel.html")


stripe.api_key = "sk_test_51O9WGMKnUl3LeHiq6xitimUjDwOkeop6iHlJBbQCGlRaU8ZmbxFnLJW2Y6zngeNZhROfzPAqmjHbcHEa8nyVL65i00Ah7Bz5qh"

@app.route("/about", methods = ["POST"])
def about():
    try:
        checkout_session = stripe.checkout.Session.create(line_items = [{"price": "price_1O9WTBKnUl3LeHiqcJwEsJT1", "quantity": 1}], mode = "subscription", success_url = "https://kns-website-test357.onrender.com/success", cancel_url = "https://kns-website-test357.onrender.com/cancel")

    except Exception as e:
        return str(e)
    
    redirect(checkout_session.url, code=302)

 
    return render_template("about.html")

if __name__ == "__main__":
    app.run()

    

    
