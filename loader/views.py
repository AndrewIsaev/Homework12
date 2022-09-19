from flask import Blueprint, render_template

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="../loader/templates")


@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")