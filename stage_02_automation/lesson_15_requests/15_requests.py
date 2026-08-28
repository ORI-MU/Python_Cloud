# ============================================================
# Python 云计算实战 — 第15课：网络请求 requests 库
# ============================================================
# 知识点：
#   requests.get(url)：发送 GET 请求
#   requests.post(url, json=data)：发送 POST 请求，带 JSON 数据
#   response.status_code：HTTP 状态码（200 = 成功，404 = 未找到）
#   response.json()：把返回的 JSON 转成 Python 字典
#   response.text：返回纯文本内容
#   示例：
#     import requests
#     r = requests.get("https://httpbin.org/get")
#     print(r.status_code)   # 200
#     print(r.json())        # 返回的 JSON 数据
# ============================================================

# ---- 题目1 ----
# 向 https://httpbin.org/get 发送 GET 请求，打印状态码
# 提示：requests.get(url).status_code

# 请在下方写下你的答案：
import requests

r = requests.get("https://httpbin.org/get")
print(r.status_code)


# ---- 题目2 ----
# 向 https://httpbin.org/get?name=Alice 发送带参数的 GET 请求
# 打印返回的 JSON 数据
# 提示：requests.get(url).json()

# 请在下方写下你的答案：
import requests
r = requests.get("https://httpbin.org/get?name=Alice")
print(r.json())


# ---- 题目3 ----
# 模拟调用云 API：向 https://httpbin.org/post 发送 POST 请求
# 携带 JSON 数据：{"action": "start", "server": "web-01"}
# 打印返回的 JSON 数据
# 提示：requests.post(url, json={"action": "start", "server": "web-01"})

# 请在下方写下你的答案：
import requests

res = requests.post("https://httpbin.org/post",json={"action": "start", "server": "web-01"})
print(res.json())