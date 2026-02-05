## requests.post函数
# 说明：发送POST请求

"""
参数：
    url: 请求的URL
    data: 表单数据
    json: JSON数据
    *,
    params: 查询参数
    headers: 请求头
    cookies: cookie
    files:
    auth:
    timeout:
    allow_redirects:
    proxies:
    hooks:
    stream:
    verify:
    cert:

"""

import requests

def example_post():
    domain="https://www.example.com"
    url = f"{domain}/api/user"

    # 设置请求头
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        "Content-Type": "application/json",         # 发送的是 JSON 数据
        "Accept": "application/json",               # 接受 JSON 响应
    }

    auth = ("username", "password")  # 基本认证

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

    # 发送POST请求
    response = requests.post(url, headers=headers, json=data, cookies=cookies, auth=auth)
    print(response.status_code)
    print(response.text)
    print(response.json())
    print(response.content)
