from flask import Blueprint, render_template, request
from json import JSONDecodeError
from main.utils import search_by_word
from functions import loger

main_blueprint = Blueprint("main_blueprint", __name__, template_folder="templates")


@main_blueprint.route("/")
def main_page():
    return render_template("index.html")


@main_blueprint.route("/search/")
def page_search():
    search_key = request.args.get("s")
    try:
        posts = search_by_word(search_key)
        loger.info(f"Search by {search_key}")
    except FileNotFoundError:
        return "File Not Found"
    except JSONDecodeError:
        return "Can`t be convert to JSON"
    else:
        return render_template("post_list.html", posts=posts, key=search_key)
