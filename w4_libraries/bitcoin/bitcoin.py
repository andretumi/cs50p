import requests
import sys


try:
    usd_amount = float(sys.argv[1])
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    btc_data = response.json()
    price_usd_btc = btc_data["bpi"]["USD"]["rate_float"]

except ValueError:
    sys.exit("Command-line argument is not a number ")
except IndexError:
    sys.exit("Missing command-line argument ")
except requests.RequestException as e:
    sys.exit(f"Error: Failed to retrieve BTC exchange rate. Details: {e}")


conversion = usd_amount * price_usd_btc
print(f"${conversion:,.4f}")
