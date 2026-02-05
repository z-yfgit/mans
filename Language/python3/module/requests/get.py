## requests.get函数
# 说明：发送GET请求

"""
参数：
    url: 请求的URL
    params: 查询参数
    *,
    data: 请求体
    headers: 请求头
    cookies: Cookie
    files:
    auth:
    timeout:
    allow_redirects:
    proxies:
    hooks:
    stream:
    verify:
    cert:
    json:

"""

import requests

def example_get():
    domain="https://www.example.com"
    url = f"{domain}/api/user"

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }

    # 设置查询参数
    params = {
        "key1": "value1",
        "key2": "value2"
    }

    # 设置请求体
    data = {
        "key1": "value1",
        "key2": "value2"
    }

    # 设置Cookie
    cookies = {
        "cookie1": "value1",
        "cookie2": "value2"
    }

    # 发送GET请求
    response = requests.get(url, headers=headers, params=params, data=data, cookies=cookies)
    print(response.status_code)
    print(response.text)
    print(response.json())
    print(response.content)
