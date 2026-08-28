         # ============================================================
# Python 云计算实战 — 第16课：日志模块 logging
# ============================================================
# 知识点：
#   logging.basicConfig(level=..., format=...)：配置日志级别和格式
#   logging.debug("msg")：调试信息（最详细）
#   logging.info("msg")：一般信息
#   logging.warning("msg")：警告信息
#   logging.error("msg")：错误信息
#   logging.FileHandler()：将日志输出到文件
#   日志级别从低到高：DEBUG < INFO < WARNING < ERROR < CRITICAL
#   示例：
#     import logging
#     logging.basicConfig(level=logging.INFO)
#     logging.info("Server started")   # 2024-01-15 14:30:00,000 INFO Server started
# ============================================================

# ---- 题目1 ----
# 配置日志，用 logging.info() 打印 "Server started"
# 提示：先 basicConfig(level=logging.INFO)，再 logging.info()

# 请在下方写下你的答案：
import logging

logging.basicConfig(level=logging.INFO)
logging.info("server started")


# ---- 题目2 ----
# 模拟运维场景，用不同级别打印日志：
#   DEBUG    → "Connecting to database..."
#   INFO     → "Connection successful"
#   WARNING  → "Disk usage 80%"
#   ERROR    → "Failed to backup database"
# 观察哪些级别会输出，哪些不会
# 提示：basicConfig 设置 level=logging.DEBUG 才能看到全部

# 请在下方写下你的答案：
import logging

logging.basicConfig(level=logging.DEBUG)
logging.debug("Connecting to database")
logging.info("Connecting successful")
logging.warning("Disk usage 80%")
logging.error("Failed to backup database")


# ---- 题目3 ----
# 将日志同时输出到文件 server.log 和控制台
# 提示：用 logging.basicConfig(handlers=[...]) 配合 FileHandler 和 StreamHandler

# 请在下方写下你的答案：
import logging

fileHandler = logging.FileHandler("server.log")
consoleHander = logging.StreamHandler()

logging.basicConfig(level=logging.INFO,format="%(asctime)s-%(levelname)s-%(message)s-%(filename)s-%(name)s",handlers=[consoleHander,fileHandler])
logging.info("Connection successful")
logging.error("Failed to backup database")