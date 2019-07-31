from flask import Flask, render_template, url_for
from forms import ContactForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '0720814bd3ac890547f87b8345a6ca8e'


@app.route("/")
@app.route("/main")
def main():
    return render_template("home.html")


@app.route("/portfolio")
def portfolio():
    return render_template("portfolio.html", title='Portfolio')


@app.route("/blog")
def blog():
    return render_template("blog.html", title='Blog')


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    return render_template("contact.html", title='Contact', form=form)
