import json
from typing import List, Dict

PATH = "posts.json"


def load_json(path: str) -> List[Dict]:
    """
    Load data from json
    :param path: json path
    :return: List with posts
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def search_by_word(word: str) -> List[Dict]:
    """
    Search posts by search_key
    :param word: User word
    :return: List with find posts
    """
    result = [post for post in load_json(PATH) if word.lower() in post["content"].lower()]
    return result
