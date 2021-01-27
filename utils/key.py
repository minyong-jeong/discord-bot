def get_discord_key():
    f = open("data/key")
    key = f.readline()
    f.close()
    return key
