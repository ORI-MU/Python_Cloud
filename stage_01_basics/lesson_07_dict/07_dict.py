# ============================================================
# Python 从零开始 — 第7课：字典 Dict
# ============================================================
# 知识点：
#   dict 用花括号 {} 创建，存放"键值对" key: value
#   通过 key 来访问 value，就像查字典
#   常用操作：keys(), values(), items(), 添加/修改/删除
#   示例：
#     student = {"name": "Alice", "age": 20, "score": 95}
#     print(student["name"])      # Alice
#     student["age"] = 21         # 修改
#     student["city"] = "NYC"     # 添加新的
#     del student["score"]        # 删除
# ============================================================

# ---- 题目1 ----
# 创建一个字典 person，包含以下信息：
#   name   → 你的名字
#   age    → 你的年龄
#   city   → 你所在的城市
# 然后打印整个字典，再逐个打印每个值

# 请在下方写下你的答案：
person = {"name":"ORI", "age":21, "city":"wuxi"}
print(person)
for i in person:
    print(person[i])


# ---- 题目2 ----
# 基于上面的 person 字典，完成以下操作：
#   1. 修改 age 的值（加1岁）
#   2. 添加一个新的键值对 hobby → 你的爱好
#   3. 删除 city
#   4. 打印修改后的字典

# 请在下方写下你的答案：
person["age"] = person["age"] + 1
person["hobby"] = "cycling"
del person["city"]
print(person)

# ---- 题目3 ----
# 创建一个字典 scores，存放三个学生的成绩：
#   Alice → 85, Bob → 92, Charlie → 78
# 用 for 循环遍历字典，打印每个学生的名字和成绩
# 效果：
#   Alice: 85
#   Bob: 92
#   Charlie: 78

# 请在下方写下你的答案：
scores  = {"Alice": 85, "Bob": 92, "Charlie": 78}
for key, value in scores.items():
    print(key, value)