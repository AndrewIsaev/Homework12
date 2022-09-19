from flask import Blueprint, render_template, request

from loader.utils import add_post_to_json

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="../loader/templates")


@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def add_post():
    content = request.form["content"]
    picture = request.files.get("picture")
    filename = picture.filename
    upload_path = "./uploads/images/"
    picture.save(upload_path + filename)
    post = {
        "pic": "/uploads/images/" + filename,
        "content": content
    }
    add_post_to_json(post)
    return render_template("post_uploaded.html", post=post)