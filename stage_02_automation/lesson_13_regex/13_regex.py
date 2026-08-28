# ============================================================
# Python 云计算实战 — 第13课：正则表达式 re 模块
# ============================================================
# 知识点：
#   re.search(r"pattern", text)：搜索第一个匹配，返回 Match 对象
#   re.findall(r"pattern", text)：找出所有匹配，返回列表
#   re.sub(r"pattern", "替换", text)：替换所有匹配
#   \d   = 数字 (0-9)
#   \d+  = 1个或多个数字
#   \d*  = 0个或多个数字
#   \w   = 字母、数字、下划线
#   \s   = 空白字符（空格、tab、换行）
#   {n}  = 正好 n 个
#   {n,m}= n 到 m 个
#   示例：
#     import re
#     result = re.search(r"\d+", "abc123def")
#     print(result.group())   # 123
# ============================================================

# ---- 题目1 ----
# 从日志中提取日期
# 日志内容： "ERROR 2024-01-15 Server timeout"
# 提取出日期 "2024-01-15" 并打印
# 提示：用 re.search(r"\d{4}-\d{2}-\d{2}", text)

# 请在下方写下你的答案：
import re

text = "ERROR 2024-01-15 Server timeout"
result = re.search(r"\d{4}-\d{2}-\d{2}",text)
print(result.group())

# ---- 题目2 ----
# 找出所有 IP 地址
# 文本： "服务器 IP: 192.168.1.1, 备用 IP: 10.0.0.1"
# 用 re.findall() 找出所有 IP 地址，打印结果列表
# 提示：IP 正则 r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"

# 请在下方写下你的答案：
import re

text = "服务器 IP: 192.168.1.1, 备用 IP: 10.0.0.1"
result = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",text)
for ip in result:
    print(ip)


# ---- 题目3 ----
# 替换敏感信息
# 文本： "User password is 123456"
# 把数字替换成 "******"，打印替换后的结果
# 提示：用 re.sub(r"\d+", "******", text)

# 请在下方写下你的答案：
import re

text = "User password is 123456"
result = re.sub(r"\d+","******",text)
print(result)