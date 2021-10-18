from requests import get, utils
from decimal import Decimal

def currency_rates(currency):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    data = response.text
    currency_out = None
    start = data.find(f"<CharCode>{currency.upper()}</CharCode>")
    if start != -1:
        start_val = data.find('<Value>', start)
        end_val = data.find('</Value>', start)
        currency_out = data[start_val + len('<Value>'):end_val].replace(',','.')
        currency_out = Decimal(float(currency_out))

    return currency_out
    
def convert_value(data):
    if data:
        data = f"{data:.2f}"
        
    return data