import requests
from config import API_KEY


def update_currency_info():
    headers = {
        "apikey": API_KEY
    }
    response = requests.get(url='https://api.apilayer.com/exchangerates_data/latest?base=USD', headers=headers)
    return response.json().get('rates')

def