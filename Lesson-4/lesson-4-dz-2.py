from requests import get, utils
from xml.dom import minidom
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


def currency_rates_xml(currency_type):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    #print(response.status_code)
    #print(response.text)

    doc = minidom.parseString(response.text)
    currency_list = doc.getElementsByTagName("Valute")
    cr_value = None
    for currency in currency_list:
        charcode = currency.getElementsByTagName("CharCode")[0]
        name = currency.getElementsByTagName("Name")[0]
        value = currency.getElementsByTagName("Value")[0]
        if (charcode.firstChild.data == currency_type.upper()):
            #print(charcode.firstChild.data)
            #print(name.firstChild.data)
            value_str = value.firstChild.data.replace(',','.')
            cr_value = Decimal(float(value_str))

    return cr_value


def convert_value(data):
    if data:
        data = f"{data:.2f}"
        
    return data


print(f"Usd = {convert_value(currency_rates('USD'))}")
print(f"Eur = {convert_value(currency_rates('eur'))}")
print(f"Xyz = {convert_value(currency_rates('xyz'))}")

print(f"Usd = {convert_value(currency_rates_xml('USD'))} by Xml")
print(f"Eur = {convert_value(currency_rates_xml('eur'))} by Xml")
print(f"xyz = {convert_value(currency_rates_xml('xyz'))} by Xml")