import requests
import os
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv('EXCHANGES_API')
BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'


def get_exchange_rate(amount, from_currency, to_currency='RUB'):
    """Получает курс валюты через Exchange Rates Data API."""
    url = f'{BASE_URL}?to={to_currency}&from={from_currency}&amount={amount}'
    headers = {'apikey': API_KEY}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        return data['result']

    except requests.RequestException as e:
        print(f"Ошибка при получении курса валют: {e}")
        return None
