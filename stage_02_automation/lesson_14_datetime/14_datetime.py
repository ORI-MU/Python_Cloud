# ============================================================
# Python 云计算实战 — 第14课：时间日期 datetime / time
# ============================================================
# 知识点：
#   datetime.now()：获取当前日期时间
#   .strftime("格式")：把时间格式化成字符串
#   time.sleep(秒)：暂停执行
#   datetime.strptime("字符串", "格式")：把字符串解析成时间
#   timedelta：时间差，用于计算日期偏移
#   常用格式符：
#     %Y = 4位年份    %m = 月份    %d = 日期
#     %H = 小时       %M = 分钟    %S = 秒
#   示例：
#     from datetime import datetime
#     now = datetime.now()
#     print(now.strftime("%Y-%m-%d %H:%M:%S"))  # 2024-01-15 14:30:00
# ============================================================

# ---- 题目1 ----
# 打印当前时间，格式为 "2024-01-15 14:30:00"
# 提示：datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# 请在下方写下你的答案：
from datetime import datetime

now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(now)


# ---- 题目2 ----
# 模拟定时检查：每隔 2 秒打印一次 "Checking server..."，共检查 3 次
# 提示：import time + for 循环 + time.sleep(2)

# 请在下方写下你的答案：
import time

sleeptime = 2
times = 0
while sleeptime == 2 and times != 3:
    time.sleep(sleeptime)
    print("Checking server...")
    times += 1 


# ---- 题目3 ----
# 计算两个日期相差多少天：2024-01-01 到 2024-12-31
# 提示：用 datetime.strptime() 解析，相减得到 timedelta，用 .days 取天数

# 请在下方写下你的答案：
from datetime import datetime

print(abs((datetime.strptime("2024-01-01","%Y-%m-%d")-datetime.strptime("2024-12-31","%Y-%m-%d")).days))