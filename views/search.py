from flask import Blueprint, render_template
from forms.search import Search

search_blueprint = Blueprint("search", __name__, template_folder="templates")


@search_blueprint.route("/search", methods=["GET", "POST"])
def search():
    form = Search()
    if form.validate_on_submit():
        search_query = form.search_post.data
        pass
        # TODO: build api url and made the api call
        # TODO: elastic search code goes here
        # TODO: send search results to the template
    return render_template("search.html", form=form, title="Search Posts")
