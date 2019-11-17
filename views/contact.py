from flask import Blueprint, flash, redirect, url_for, render_template
from forms.contact import ContactForm
from utilities.send_email import send_email

contact_blueprint = Blueprint("contact", __name__, template_folder="templates")


@contact_blueprint.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_email(
            form.username.data,
            form.email.data,
            form.subject.data,
            form.message.data,
        )
        flash("Thanks! I will be in touch soon.")
        return redirect(url_for("contact.contact"))

    return render_template("contact.html", title="Contact", form=form)
