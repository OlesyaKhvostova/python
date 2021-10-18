from requests import get, utils
from decimal import Decimal
from datetime import date, datetime

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

    date_out = date
    start = data.find(f"Date=""")
    if start != -1:
        end = data.find(f"\"", start + len(f"Date=""") + 1)
        date_out = data[start+ len(f"Date=""") + 1:end]
        date_out = datetime.strptime(date_out, "%d.%m.%Y")
        
    return currency_out,date_out.date()


def convert_value(data):
    output = str()
    if data[0]:
        output += f"{data[0]:.2f}"
    else:
        output += f"{data[0]}"
        
    output +=  f"({str(data[1])})"
    return output


print(f"Usd = {convert_value(currency_rates('USD'))}")
print(f"Eur = {convert_value(currency_rates('eur'))}")
print(f"Xyz = {convert_value(currency_rates('xyz'))}")