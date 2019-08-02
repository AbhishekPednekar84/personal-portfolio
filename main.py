from flask import Flask, render_template, url_for, flash, redirect
from forms import ContactForm
from send_email import send_email

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
    if form.validate_on_submit():
        send_email(form.username.data, form.email.data,
                   form.subject.data, form.message.data)
        flash('Thanks! I will be in touch soon.')
        return redirect(url_for('contact'))

    return render_template("contact.html", title='Contact', form=form)
