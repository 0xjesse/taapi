import requests

# API endpoint
url = "https://api.taapi.io/rsi"

# API parameters
params = {
    "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjRkYThkM2Q0OThkNzVkYTM2MzU1ZTBjIiwiaWF0IjoxNjkyMDQ0NzE2LCJleHAiOjMzMTk2NTA4NzE2fQ.3rLKAJmqPWv8gNkkgnXIiHotR_o5-nWay-iWrZoGjME",
    "exchange": "binance",
    "symbol": "SOL/USDT", ## can change this to other currencies, replace SOL. must be caps
    "interval": "15m"
}

# Send GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    rsi_value = data.get("value")

    if rsi_value is not None:
        print(f"RSI value for SOL/USDT on 15m interval: {rsi_value}")
    else:
        print("No RSI value found.")
else:
    print("Error fetching RSI value. Status code:", response.status_code)