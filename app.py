from flask import Flask, render_template
from products import PRODUCTS
from services import SERVICES

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/contacts')
def contacts():
    return render_template("contacts.html",
                           address="м. Київ, вул. Тестова, 1",
                           email="eshop@gmail.com",
                           facebook_url="https://www.facebook.com/ssternenko",
                           telegram_url="https://t.me/ssternenko")

@app.route('/services')
def services():
    return render_template("services.html", services=SERVICES)

@app.route('/software')
def software():
    return render_template("software.html", products=PRODUCTS)


if __name__ == '__main__':
    is_debug = app.config["FLASK_DEBUG"]
    if is_debug:
        app.jinja_env.auto_reload = True
        app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run()
