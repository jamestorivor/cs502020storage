import requests
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    try:
        number = float(sys.argv[1])

    except ValueError:
        sys.exit("Command-line argument is not a number")
try:
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    txt = response.json()
    total = number * float(txt['bpi']['USD']['rate_float'])
    print(f"${total:,.4f}")

except requests.RequestException:
    print("no")