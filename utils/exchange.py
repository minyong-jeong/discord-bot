import requests
import datetime
import os


def get_time_now():
    kst = datetime.timezone(datetime.timedelta(hours=9))
    now = datetime.datetime.now(kst)
    now_datetime = now.strftime('%y%m%d%H%M%S')
    return now_datetime


def get_exchange_data_from_api(authkey):
    datatype = "AP01"
    url = "https://www.koreaexim.go.kr/site/program/financial/exchangeJSON?authkey=%s&data=%s" % (
        authkey, datatype)

    try:
        res = requests.get(url)
    except Exception as e:
        print(e)
        raise

    return res.json()


def create_exchange_data(authkey):
    data = get_exchange_data_from_api(authkey)

    exchange = {
        "name": "exchange",
        "time": get_time_now(),
        "exchange": {}
    }
    for item in data:
        exchange["exchange"][item["cur_unit"]] = int(
            item["bkpr"].replace(',', ''))

    return exchange
