# ============================================================
# Python 从零开始 — 第3课：用户输入 input()
# ============================================================
# 知识点：
#   input() 让用户在键盘上输入内容，返回的是字符串 str
#   input("提示文字") 可以在括号里写提示
#   注意：input() 拿到的永远是字符串，做数学运算需要转换
#   示例：
#     name = input("What's your name? ")
#     print("Hello, " + name)
# ============================================================

# ---- 题目1 ----
# 写一个程序，询问用户的名字，然后打印一句问候
# 运行效果：
#   What's your name? Ori
#   Hello, Ori!

# 请在下方写下你的答案：
name = input("What's your name?\n")
print("Hello," + name)

# ---- 题目2 ----
# 写一个程序，让用户输入两个数字，然后输出它们的和
# 提示：input() 拿到的字符串不能直接做加法，要用 int() 或 float() 转换！
# 运行效果：
#   Enter first number: 5
#   Enter second number: 3
#   Sum: 8

# 请在下方写下你的答案：
FNun = input("Enter first number\n")
SNun = input("Enter second number\n")
print("Sum = ", float(float(FNun) + float(SNun)))