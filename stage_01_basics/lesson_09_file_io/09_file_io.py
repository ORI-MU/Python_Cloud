# ============================================================
# Python 从零开始 — 第9课：文件读写
# ============================================================
# 知识点：
#   open() 打开文件，"r" 读 / "w" 写 / "a" 追加
#   用 with open(...) as f 自动关闭文件（推荐）
#   read() 读全部, readlines() 读所有行, write() 写入
#   示例：
#     # 写入
#     with open("test.txt", "w") as f:
#         f.write("Hello, File!")
#
#     # 读取
#     with open("test.txt", "r") as f:
#         content = f.read()
#         print(content)
# ============================================================

# ---- 题目1 ----
# 写一个程序，创建一个文件 "greeting.txt"
# 写入以下内容：
#   Hello, World!
#   This is my first file.
# 然后读取这个文件，打印内容

# 请在下方写下你的答案：
with open("greeting.txt", "w") as f:
    f.write("Hello, World!\n" \
    "This is my first file.\n")
with open("greeting.txt", "r") as f:
    content = f.read()
    print(content)

# ---- 题目2 ----
# 创建一个文件 "numbers.txt"，写入 1 到 5，每个数字一行
# 然后用 readlines() 读取所有行，用 for 循环打印每一行
# 效果：
#   1
#   2
#   3
#   4
#   5

# 请在下方写下你的答案：
with open("numbers.txt", "w") as f:
    f.write("1\n2\n3\n4\n5\n")
with open("numbers.txt", "r") as f:
    for i in f.readlines():
        print(i.strip())



# ---- 题目3 ----
# 用追加模式 "a" 打开 "numbers.txt"，追加数字 6, 7, 8
# 然后读取整个文件，打印内容

# 请在下方写下你的答案：
with open("numbers.txt", "a") as f:
    f.write("6\n7\n8\n")
with open("numbers.txt", "r") as f:
    print(f.read())