# ============================================================
# Python 从零开始 — 第6课：循环 for / while
# ============================================================
# 知识点：
#   for 循环：遍历列表或范围，逐个取出元素
#   while 循环：只要条件成立就重复执行
#   range(n)：生成 0 到 n-1 的数字序列
#   注意：冒号 : 和缩进，和 if 一样！
#   示例：
#     for i in range(5):
#         print(i)          # 输出 0 1 2 3 4
#
#     count = 0
#     while count < 3:
#         print(count)
#         count = count + 1  # 输出 0 1 2
# ============================================================

# ---- 题目1 ----
# 用 for 循环打印 1 到 10，每个数字一行
# 提示：range(1, 11) 生成 1 到 10

# 请在下方写下你的答案：
for i in range(1,11):
    print(i)


# ---- 题目2 ----
# 创建一个列表 fruits = ["apple", "banana", "orange", "grape"]
# 用 for 循环遍历列表，逐个打印每个水果
# 效果：
#   apple
#   banana
#   orange
#   grape

# 请在下方写下你的答案：
fruits = ["apple", "banana", "orange", "grape"]
for i in fruits:
    print(i)

# ---- 题目3 ----
# 用 while 循环，从 5 倒数到 1，打印每个数字
# 效果：
#   5
#   4
#   3
#   2
#   1

# 请在下方写下你的答案：
i = 5
while i >=1:
    print(i)
    i = i-1