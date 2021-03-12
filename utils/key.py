import json


def get_discord_key():
    with open("data/key.json", "r") as f:
        key = json.load(f)['key']
        return key
