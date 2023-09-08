import requests

# API endpoint
url = "https://api.taapi.io/rsi"

# API parameters
params = {
    "secret": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjbHVlIjoiNjRkYThkM2Q0OThkNzVkYTM2MzU1ZTBjIiwiaWF0IjoxNjkyMDQ0NzE2LCJleHAiOjMzMTk2NTA4NzE2fQ.3rLKAJmqPWv8gNkkgnXIiHotR_o5-nWay-iWrZoGjME",
    "exchange": "binance",
    "symbol": "SOL/USDT",
    "interval": "15m"
}

# Send GET request for 15-minute interval RSI
response_15m = requests.get(url, params=params)

# Check if the request was successful
if response_15m.status_code == 200:
    data_15m = response_15m.json()
    rsi_15m = data_15m.get("value")
else:
    print("Error fetching 15m interval RSI. Status code:", response_15m.status_code)
    rsi_15m = None

# Update interval parameter for 1-minute interval
params["interval"] = "1m"

# Send GET request for 1-minute interval RSI
response_1m = requests.get(url, params=params)

# Check if the request was successful
if response_1m.status_code == 200:
    data_1m = response_1m.json()
    rsi_1m = data_1m.get("value")
else:
    print("Error fetching 1m interval RSI. Status code:", response_1m.status_code)
    rsi_1m = None

# Print table header
print("{:<12} {:<20} {:<20}".format("Name", "15m RSI", "1m RSI"))
print("-" * 50)

# Print RSI values in table format
if rsi_15m is not None and rsi_1m is not None:
    print("{:<12} {:<20} {:<20}".format("SOL/USDT", rsi_15m, rsi_1m))
else:
    print("{:<12} {:<20} {:<20}".format("SOL/USDT", "N/A", "N/A"))