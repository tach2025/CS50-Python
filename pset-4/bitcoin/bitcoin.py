import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    n = float(sys.argv[1])
except:
    sys.exit("Command-line argument is not a number")

API = "https://api.coindesk.com/v1/bpi/currentprice.json"

try:
    response = requests.get(API)
    price = response.json()["bpi"]["USD"]["rate_float"]
    print(f"${price * n:,.4f}")
except requests.RequestException:
    sys.exit("Faulty response from API")
