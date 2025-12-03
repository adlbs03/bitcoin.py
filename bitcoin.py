import sys
import requests


price_btc = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=1092342a2882ddd58812baa5f24fa7f83b5d3f60fc5c2d0087311c8f0cdcb6fb").json()
price_btc = float(price_btc["data"]["priceUsd"])
try:
    user_btc = float(sys.argv[1])

except (IndexError, requests.RequestException, ValueError):
    if len(sys.argv) < 2:
        print("Missing command-line argument")
    elif ValueError:
        print("Command-line argument is not a number")

amount = price_btc * user_btc

print(f"${amount:,.4f}")