# ============================================================
# Python 从零开始 — 第8课：函数 Function
# ============================================================
# 知识点：
#   def 定义函数，函数是一段可重复使用的代码
#   return 返回值，没有 return 默认返回 None
#   参数：函数接收的输入
#   示例：
#     def greet(name):
#         return "Hello, " + name
#
#     print(greet("Alice"))    # Hello, Alice
# ============================================================

# ---- 题目1 ----
# 写一个函数 add(a, b)，接收两个数字，返回它们的和
# 然后调用它，分别传入 (3, 5) 和 (10, 20)，打印结果

# 请在下方写下你的答案：
def add(a, b):
    return a + b
print(add(3, 5), "\n", add(10, 20))

# ---- 题目2 ----
# 写一个函数 is_even(n)，判断一个数字是不是偶数
# 如果是偶数返回 True，否则返回 False
# 然后分别测试 4 和 7，打印结果

# 请在下方写下你的答案：
def isEven(n):
    if(n%2 == 0):
        return print("True")
    else:
        return print("False")
isEven(4)
isEven(7)

# ---- 题目3 ----
# 写一个函数 max_of_three(a, b, c)，接收三个数字，返回最大的那个
# 然后测试 (3, 7, 5) 和 (10, 2, 8)，打印结果
# 提示：用 if 比较

# 请在下方写下你的答案：
def maxOfThree(a, b, c):
    return print(max(a,b,c))
maxOfThree(3, 7, 5)
maxOfThree(10, 2, 8)