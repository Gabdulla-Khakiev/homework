import requests


API_KEY = 'EXCHANGES_API'
BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'

def get_exchange(amount, from_currency, to_currency='RUB'):
    params = {
        'from': from_currency,
        'to': to_currency,
        'amount': amount,
    }
    headers = {'apikey': API_KEY}
    response = requests.get(BASE_URL, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get('result', 0)
    else:
        raise Exception(f"Error fetching exchange rate: {response.status_code}")
