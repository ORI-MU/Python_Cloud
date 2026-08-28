# ============================================================
# Python 从零开始 — 第10课：综合实战 + 异常处理 + 模块
# ============================================================
# 新知识点：
#   try/except：捕获错误，防止程序崩溃
#   import：导入模块（Python 自带或第三方）
#   json 模块：读写 JSON 数据
#   示例：
#     try:
#         num = int(input("Number: "))
#     except ValueError:
#         print("That's not a number!")
#
#     import json
#     data = {"name": "Alice", "age": 20}
#     json.dumps(data)   # 转成 JSON 字符串
# ============================================================

# ---- 题目1 ----
# 写一个程序，让用户输入一个数字
# 如果用户输入的不是数字（比如 "abc"），捕获错误并提示 "Invalid input!"
# 如果输入正确，打印 "You entered: 数字"
# 提示：用 try/except ValueError

# 请在下方写下你的答案：
try:
    num = int(input("number:"))
except ValueError:
    print("That's not a number")

# ---- 题目2 ----
# 写一个程序，读取 "numbers.txt"（第9课创建的）
# 把每一行转成整数，计算所有数字的总和，打印结果
# 如果文件不存在，捕获错误并提示 "File not found!"
# 效果：Sum of numbers: 36

# 请在下方写下你的答案：
summary = 0
try:
    with open("numbers.txt", "r") as f:
        for i in f.readlines():
            summary += int(i)
    print("Sum of numbers: ", summary)
except FileExistsError:
    print("File not found!")


# ---- 题目3 ----
# 用 json 模块创建一个字典 data = {"name":"ORI","skills":["Python","TS","Java"]}
# 写入文件 "data.json"
# 然后读取这个 JSON 文件，打印内容

# 请在下方写下你的答案：
import json
data = {"name":"ORI","skills":["Python","TS","Java"]}
with open("data.json", "w") as f:
    f.write(json.dumps(data))
with open("data.json", "r") as f:
    print(f.read())
