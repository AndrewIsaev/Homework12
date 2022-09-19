import json

from main.utils import load_json, PATH


def add_post_to_json(post):
    posts = load_json(PATH)
    posts.append(post)
    write_to_json(posts)


def write_to_json(posts):
    with open(PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)



