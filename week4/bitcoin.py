import sys
import requests  # dont forget to run $pip install requests

try:
    quantity = float(sys.argv[1])
except:
    if len(sys.argv) == 1:
        sys.exit("Missing command-line argument")
    else:
        sys.exit("Command-line argument is not a number")
# API
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
response = r.json()
usd = response["bpi"]["USD"]["rate"]
# remove " , "
usd = usd.replace(",", "")
total = float(usd) * quantity
print(f"${total:,.4f}")
