import requests

# Gate.io API URL
url = "https://api.gateio.ws/api2/1/tickers"

# 发送 GET 请求
response = requests.get(url)

# 检查响应状态
if response.status_code == 200:
    # 解析 JSON 数据
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

import requests
import time
import hmac
import hashlib

# 设置你的 API 密钥和密钥对
API_KEY = 'your_api_key'
API_SECRET = 'your_api_secret'

# Gate.io API URL
url = "https://api.gateio.ws/api2/1/private/balances"

# 创建请求参数
nonce = str(int(time.time() * 1000))  # 当前时间戳（毫秒）
params = {
    'nonce': nonce
}

# 创建签名
query_string = '&'.join([f"{key}={value}" for key, value in sorted(params.items())])
signature = hmac.new(API_SECRET.encode(), query_string.encode(), hashlib.sha512).hexdigest()

# 设置请求头
headers = {
    'Key': API_KEY,
    'Sign': signature
}

# 发送 GET 请求
response = requests.get(url, headers=headers, params=params)

# 检查响应状态
if response.status_code == 200:
    # 解析 JSON 数据
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")

