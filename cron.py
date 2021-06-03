import os

from utils import MongoController, get_api_authkey, get_dbinfo

AUTHKEY = get_api_authkey('config/apikey.json')

db = MongoController('config/database.json', 'exchange')
db.update_exchange(AUTHKEY)
