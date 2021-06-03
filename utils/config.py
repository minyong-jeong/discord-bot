import json


def get_discord_key(key_file):
    with open(key_file, "r") as f:
        key = json.load(f)['key']
        return key


def get_api_authkey(key_file):
    with open(key_file, "r") as f:
        key = json.load(f)['key']
        return key


def get_dbinfo(dbinfo_file):
    with open(dbinfo_file, "r") as f:
        dbinfo = json.load(f)
        return dbinfo
