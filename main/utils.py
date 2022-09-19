import json

PATH = "../posts.json"

def load_jon(path):
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def search_by_word(word):
    result = [post for post in load_jon(PATH) if word.lower() in post["content"].lower()]
    return result

# print(load_jon(PATH))
# print(search_by_word("Ага"))
