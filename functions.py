from datetime import datetime
import requests
def get_date():
    date = datetime.now()
    current_date = date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date
def file_writing(rate, amount, currency):
    text = f"\n|date: {get_date()} | currency: {currency} | rate: {rate} | amount: {amount}      | pln_value : {rate * amount}|"
    writing_file = open('history.txt', 'a', encoding='utf-8')
    writing_file.write(text)

def get_exchange_rate(currency):
    try:
        response = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/C/{currency}/?format=json')
        data = response.json()
        return data['rates'][0]['ask']
    except Exception as e:
        print(e)
        return None

def get_hight_and_low_value(currency, date_from, date_to):
    try:
        response = requests.get(f'http://api.nbp.pl/api/exchangerates/rates/a/{currency}/{date_from}/{date_to}/?format=json')
        data = response.json()
        rates = data['rates']
        max_rate = None
        min_rate = None
        for rate in rates:
            mid = rate['mid']
            if max_rate is None or mid > max_rate:
                max_rate = mid
            if min_rate is None or mid < min_rate:
                min_rate = mid
        return min_rate, max_rate, currency
    except Exception as e:
        print(e)
        return None