from flask import Blueprint, render_template, request

from main.utils import search_by_word

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="./templates")

@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search/")
def page_search():
    search_key = request.args.get("s")
    posts = search_by_word(search_key)
    return render_template("post_list.html", posts=posts, key=search_key)