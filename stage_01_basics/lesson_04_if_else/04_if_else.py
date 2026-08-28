# ============================================================
# Python 从零开始 — 第4课：条件判断 if / elif / else
# ============================================================
# 知识点：
#   if 条件:        → 如果条件成立，执行下面的代码
#   elif 条件:      → 否则如果另一个条件成立
#   else:           → 否则（以上都不成立）
#   注意：冒号 : 不能忘，缩进必须一致（4个空格或1个Tab）
#
#   比较运算符：== 等于, != 不等于, > 大于, < 小于, >= 大于等于, <= 小于等于
#   示例：
#     age = 18
#     if age >= 18:
#         print("Adult")
#     else:
#         print("Child")
# ============================================================

# ---- 题目1 ----
# 让用户输入一个数字，判断它是正数、负数还是零
# 运行效果：
#   Enter a number: 5
#   Positive
#   Enter a number: -3
#   Negative
#   Enter a number: 0
#   Zero

# 请在下方写下你的答案：
num = int(input("Enter a number:\n"))
if num>0:
    print("Positive");
elif num<0:
    print("Negative");
else:
    print("Zero")

# ---- 题目2 ----
# 让用户输入年龄，输出对应的票价：
#   0-12岁  → "Free"
#   13-17岁 → "Half price"
#   18-59岁 → "Full price"
#   60岁以上 → "Senior discount"
# 运行效果：
#   Enter age: 15
#   Half price

# 请在下方写下你的答案：
age = int(input("Enter your age\n"))
if age<=12:
    print("Free")
elif age>12 and age<=18:
    print("Half Price")
elif age>18 and age<=60:
    print("Full Price")
else:
    print("Senior discount")