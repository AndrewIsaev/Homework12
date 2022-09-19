import json
from typing import Dict, List

from main.utils import load_json, PATH


def add_post_to_json(post: Dict) -> None:
    """
    Add post to json
    Rewrite json
    :param post: new post
    :return: None
    """
    posts: List = load_json(PATH)
    posts.append(post)
    write_to_json(posts)


def write_to_json(posts: List) -> None:
    """
    Rewrite json file
    :param posts: list with all posts
    :return: None
    """
    with open(PATH, "w", encoding="utf-8") as file:
        json.dump(posts, file, ensure_ascii=False)


def check_extension(filename: str) -> bool:
    """
    Check is extension is available
    :param filename: Name of check file
    :return: True if available False if not
    """
    if filename.split(".")[1] not in ("jpeg", "png"):
        return False
    return True
