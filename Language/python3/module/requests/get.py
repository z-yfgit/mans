import requests
"""
requests.get()
发送GET请求
"""

def example_get():
    domain="https://www.example.com"
    url = f"{domain}/api/user"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {
        "key1": "value1",
        "key2": "value2"
    }
    data = {
        "key1": "value1",
        "key2": "value2"
    }
    cookies = {
        "cookie1": "value1",
        "cookie2": "value2"
    }
    response = requests.get(url, headers=headers, params=params, data=data, cookies=cookies)
    print(response.status_code)
    print(response.text)
    print(response.json())
    print(response.content)

