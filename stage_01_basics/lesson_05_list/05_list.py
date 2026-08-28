# ============================================================
# Python 从零开始 — 第5课：列表 List
# ============================================================
# 知识点：
#   list 用方括号 [] 创建，可以放多个元素，用逗号分隔
#   索引从 0 开始，用 [] 访问元素
#   常用操作：append(), remove(), len(), pop()
#   示例：
#     fruits = ["apple", "banana", "orange"]
#     print(fruits[0])      # apple
#     print(len(fruits))    # 3
#     fruits.append("grape")  # 添加
#     fruits.remove("banana") # 删除
# ============================================================

# ---- 题目1 ----
# 创建一个列表，包含5个你喜欢的食物名称
# 然后：
#   1. 打印整个列表
#   2. 打印第一个食物
#   3. 打印最后一个食物
#   4. 打印列表的长度

# 请在下方写下你的答案：
fruits = ["apple","orange","peach","pear","durain"]
print(fruits[0])
print(fruits[4])
print(len(fruits))


# ---- 题目2 ----
# 创建一个空列表 numbers = []
# 然后依次完成以下操作：
#   1. 添加 10
#   2. 添加 20
#   3. 添加 30
#   4. 打印列表
#   5. 删除 20
#   6. 打印列表
#   7. 打印列表长度

# 请在下方写下你的答案：
numbers = []
numbers.append(10)
numbers.append(20)
numbers.append(30)
print(numbers)
numbers.remove(20)
print(numbers)
print(len(numbers))
