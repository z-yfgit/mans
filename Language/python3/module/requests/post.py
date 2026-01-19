import requests
"""
requests.post()
发送POST请求
"""

def example_post():
    domain="https://www.example.com"
    url = f"{domain}/api/user"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json",         # 表示发送的是 JSON 数据
        "Accept": "application/json",               # 表示接受 JSON 响应
        "Authorization": "Bearer token123",         # Bearer 认证
    }
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    cookies = {
        "cookie1": "value1",
        "cookie2": "value2"
    }
    response = requests.post(url, headers=headers, json=data, cookies=cookies)
    print(response.status_code)
    print(response.text)
    print(response.json())
    print(response.content)