from flask import Blueprint, render_template, request
from functions import loger

from loader.utils import add_post_to_json, check_extension

loader_blueprint = Blueprint("loader_blueprint", __name__, template_folder="templates")


@loader_blueprint.route("/post")
def post_page():
    return render_template("post_form.html")


@loader_blueprint.route("/post", methods=["POST"])
def add_post():
    content: str = request.form["content"]
    picture = request.files.get("picture")

    filename = picture.filename

    if not check_extension(filename):
        loger.info(f"{filename} is not a picture")
        return "Not available file format,<br>Please upload JPEG or PNG"

    upload_path = "./uploads/images/"

    try:
        picture.save(upload_path + filename)
    except Exception:
        loger.error(f"Error with uploading file {filename}")
        return "Error with uploading file"

    post = {
        "pic": "/uploads/images/" + filename,
        "content": content
    }
    add_post_to_json(post)

    return render_template("post_uploaded.html", post=post)
