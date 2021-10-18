from requests import get, utils
from xml.dom import minidom
from decimal import Decimal

def currency_rates(currency_type):
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
            print(name.firstChild.data)
            val = str(value.firstChild.data)
            cr_value = Decimal.(val)

    return cr_value


print(currency_rates('USD'))
print(currency_rates('eur'))
