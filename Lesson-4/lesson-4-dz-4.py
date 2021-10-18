from utils import currency_rates,convert_value

print(f"Usd = {convert_value(currency_rates('USD'))}")
print(f"Eur = {convert_value(currency_rates('eur'))}")
print(f"Xyz = {convert_value(currency_rates('xyz'))}")