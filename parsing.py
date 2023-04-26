import requests
from config import API_KEY

HEADERS = {
    "apikey": API_KEY
}


def get_currency_info():
    response = requests.get(url='https://api.apilayer.com/exchangerates_data/latest?base=USD', headers=HEADERS)
    return response.json().get('rates')


def get_currency_name():
    response = requests.get(url='https://api.apilayer.com/exchangerates_data/symbols', headers=HEADERS)
    return response.json().get('symbols')


def get_full_currency_info():
    names = get_currency_name()
    rates = get_currency_info()
    currency_info = []
    for k, v in names.items():
        currency_info.append((k, v, rates[k]))
    return currency_info
