# ============================================================
# Python 自动化运维 — 第12课：文件系统操作 os / pathlib
# ============================================================
# 知识点：
#   os.path.exists(path)：检查文件/目录是否存在
#   os.path.isfile(path)：检查是否为文件
#   os.path.isdir(path)：检查是否为目录
#   os.listdir(path)：列出目录内容
#   os.mkdir(path)：创建目录
#   os.remove(path)：删除文件
#   os.path.getsize(path)：获取文件大小（字节）
#   os.path.join(path, name)：拼接路径
#   示例：
#     import os
#     if os.path.exists("data.txt"):
#         print("文件存在")
# ============================================================

# ---- 题目1 ----
# 写一个脚本，检查当前目录下是否存在 "numbers.txt" 文件
#   存在 → 打印 "numbers.txt exists, size: XXX bytes"
#   不存在 → 打印 "numbers.txt not found"
# 提示：用 os.path.exists() 和 os.path.getsize()

# 请在下方写下你的答案：
import os

fileName = "numbers.txt"
if os.path.exists(fileName):
    print(f"numbers.txt exists, size: {os.path.getsize(fileName)} bytes")
else:
    print("numbers.txt not found")


# ---- 题目2 ----
# 写一个脚本，遍历当前目录下所有 .py 文件
# 打印每个文件名和文件大小
# 提示：用 os.listdir() 获取所有文件，用 endswith(".py") 过滤

# 请在下方写下你的答案：
import os

for filename in os.listdir("."):
    if filename.endswith(".py"):
        print(f"The filename is {filename}, and the size is {os.path.getsize(filename)}")

# ---- 题目3 ----
# 模拟一个运维场景：检查日志目录
#   1. 创建目录 "logs"（如果不存在），用 os.mkdir()
#      注意：os.mkdir() 如果目录已存在会报错，所以要先检查
#   2. 在 "logs" 目录下创建 "app.log"，写入 "Server started successfully"
#   3. 读取并打印 "logs/app.log" 的内容
# 提示：路径用 os.path.join("logs", "app.log")

# 请在下方写下你的答案：
import os

log_dir = "logs"
filename = os.path.join("logs","app.log")

if not os.path.exists(log_dir):
    os.mkdir(log_dir)

with open(filename,"w") as f:
    f.write("Server started successfully")

with open(filename,"r") as f:
    print(f.read())