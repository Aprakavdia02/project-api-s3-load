import requests

# Define the CoinGecko API URL
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"

# Send the GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Convert response to JSON
    for coin in data[:5]:  # Print first 5 coins for a preview
        print(f"Name: {coin['name']}, Price: ${coin['current_price']}, Market Cap: {coin['market_cap']}")
else:
    print("Failed to fetch data:", response.status_code)