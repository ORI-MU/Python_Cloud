# ============================================================
# Python 云计算实战 — 第20课：综合实战 — 自动化运维脚本
# ============================================================
# 整合第11~19课所有知识点，写一个完整的运维工具
# 场景：批量巡检服务器 — ping 检测 + HTTP 健康检查 + 生成报告
# ============================================================


# ============================================================
# 项目说明
# ============================================================
# 你要写一个「服务器巡检脚本」，功能如下：
#
# 1. 读取 servers.yaml 配置文件（服务器列表）
# 2. 并发 ping 所有服务器（asyncio）
# 3. 并发 HTTP 健康检查（aiohttp）
# 4. 用 logging 记录日志（同时输出到文件和控制台）
# 5. 解析 ping 输出中的延迟（re 正则）
# 6. 生成带时间戳的巡检报告（datetime + 文件写入）
# 7. 配置文件用 yaml 格式（config）
#
# 涉及知识点：
#   L11 subprocess    — 执行 ping 命令
#   L12 os/filesystem — 创建目录、写文件
#   L13 regex         — 解析 ping 结果
#   L14 datetime      — 报告时间戳
#   L15 requests      — HTTP 健康检查（用 aiohttp 替代）
#   L16 logging       — 日志记录
#   L17 config        — YAML 配置文件
#   L18 concurrency   — （升级为 asyncio）
#   L19 asyncio       — 并发 ping + 并发 HTTP
# ============================================================


# ============================================================
# 准备工作：创建配置文件
# ============================================================
# 在 lesson_20_project 目录下创建 servers.yaml：
# ============================================================

# ==== 运行示例：创建 servers.yaml（取消注释即可运行）====
# import yaml
# import os
#
# config = {
#     "servers": [
#         {"name": "web-01", "ip": "10.0.1.1", "port": 80},
#         {"name": "web-02", "ip": "10.0.1.2", "port": 80},
#         {"name": "db-01",  "ip": "10.0.1.100", "port": 3306},
#         {"name": "cache-01", "ip": "10.0.1.200", "port": 6379},
#     ],
#     "ping": {"count": 2, "timeout": 3},
#     "http": {"timeout": 5},
#     "report": {"dir": "reports"},
# }
#
# config_path = os.path.join(os.path.dirname(__file__), "servers.yaml")
# with open(config_path, "w", encoding="utf-8") as f:
#     yaml.dump(config, f, allow_unicode=True, default_flow_style=False)
# print(f"配置文件已创建: {config_path}")


# ============================================================
# 知识点回顾1：subprocess 执行 ping
# ============================================================
# 语法：
#   result = subprocess.run(["ping", "-n", "2", ip],
#                            capture_output=True, text=True, timeout=3)
#   result.stdout  → ping 输出文本
#   result.returncode → 0 表示成功
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import subprocess
# import sys
#
# ip = "127.0.0.1"
# param = "-n" if sys.platform == "win32" else "-c"
# result = subprocess.run(
#     ["ping", param, "2", ip],
#     capture_output=True, text=True, timeout=3
# )
# if result.returncode == 0:
#     print(f"{ip} 可达")
#     print(result.stdout)
# else:
#     print(f"{ip} 不可达")


# ============================================================
# 知识点回顾2：re 正则解析 ping 延迟
# ============================================================
# Windows ping 输出示例：
#   来自 10.0.1.1 的回复: 字节=32 时间=1ms TTL=64
# 正则：
#   r"时间[=<]\s*(\d+)ms"  → 提取延迟毫秒数
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import re
# import subprocess
# import sys
#
# ip = "127.0.0.1"
# param = "-n" if sys.platform == "win32" else "-c"
# result = subprocess.run(
#     ["ping", param, "2", ip],
#     capture_output=True, text=True, timeout=3
# )
# if result.returncode == 0:
#     # Windows: "时间=1ms" 或 "时间<1ms"
#     # Linux: "time=1.23 ms"
#     match = re.search(r"时间[=<]\s*(\d+)ms", result.stdout)
#     if match:
#         delay = int(match.group(1))
#         print(f"{ip} 延迟: {delay}ms")
#     else:
#         # 尝试 Linux 格式
#         match = re.search(r"time=(\d+\.?\d*)\s*ms", result.stdout)
#         if match:
#             print(f"{ip} 延迟: {match.group(1)}ms")


# ============================================================
# 知识点回顾3：logging 日志输出到文件 + 控制台
# ============================================================
# 语法：
#   logging.basicConfig(level=..., format=..., handlers=[...])
#   logging.info("xxx")
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import logging
# import os
#
# log_dir = os.path.join(os.path.dirname(__file__), "logs")
# os.makedirs(log_dir, exist_ok=True)
#
# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s [%(levelname)s] %(message)s",
#     handlers=[
#         logging.FileHandler(os.path.join(log_dir, "check.log"), encoding="utf-8"),
#         logging.StreamHandler(),
#     ]
# )
# logging.info("日志系统初始化完成")
# logging.warning("这是一条警告")
# logging.error("这是一条错误")


# ============================================================
# 知识点回顾4：datetime 生成时间戳
# ============================================================
# 语法：
#   datetime.now().strftime("%Y-%m-%d %H:%M:%S")  → "2026-08-24 10:30:00"
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from datetime import datetime
#
# now = datetime.now()
# print(f"报告时间: {now.strftime("%Y-%m-%d %H:%M:%S")}")
# print(f"文件名时间戳: {now.strftime("%Y%m%d_%H%M%S")}")


# ============================================================
# 知识点回顾5：asyncio 并发执行 subprocess
# ============================================================
# 语法：
#   proc = await asyncio.create_subprocess_exec(
#       "ping", param, "2", ip,
#       stdout=asyncio.subprocess.PIPE,
#       stderr=asyncio.subprocess.PIPE,
#   )
#   stdout, stderr = await proc.communicate()
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import asyncio
# import sys
#
# async def async_ping(ip):
#     param = "-n" if sys.platform == "win32" else "-c"
#     proc = await asyncio.create_subprocess_exec(
#         "ping", param, "2", ip,
#         stdout=asyncio.subprocess.PIPE,
#         stderr=asyncio.subprocess.PIPE,
#     )
#     stdout, stderr = await proc.communicate()
#     return proc.returncode == 0, stdout.decode()
#
# async def main():
#     ok, output = await async_ping("127.0.0.1")
#     print(f"可达: {ok}")
#     print(output[:200])
#
# if __name__ == "__main__":
#     asyncio.run(main())


# ============================================================
# ---- 题目：服务器巡检脚本 ----
# ============================================================
# 要求：
# 1. 创建 servers.yaml 配置文件（用上面的示例）
# 2. 读 YAML 获取服务器列表
# 3. 用 asyncio 并发 ping 所有服务器（subprocess 异步版）
# 4. 用 re 正则从 ping 输出中提取延迟
# 5. 用 logging 记录日志（文件 + 控制台）
# 6. 用 datetime 生成报告文件名：reports/report_20260824_103000.txt
# 7. 写入报告文件，内容包含：
#     每台服务器的 ping 结果（可达/不可达、延迟）
#     巡检时间
#     总结（几台可达，几台不可达）
#
# 预期输出（控制台）：
#   [INFO] 开始巡检 4 台服务器...
#   [INFO] web-01 (10.0.1.1) 可达, 延迟: 1ms
#   [INFO] web-02 (10.0.1.2) 可达, 延迟: 1ms
#   [INFO] db-01 (10.0.1.100) 不可达
#   [INFO] cache-01 (10.0.1.200) 不可达
#   [INFO] 巡检完成: 2/4 可达, 报告已保存到 reports/report_xxx.txt
#
# 提示：
#   - 用 yaml.safe_load() 读取配置文件
#   - 用 asyncio.create_subprocess_exec 异步执行 ping
#   - 用 re.search 提取延迟
#   - 用 os.makedirs 创建 reports 目录
#   - 跨平台: sys.platform == "win32" → "-n", else → "-c"
# ============================================================

# 请在下方写下你的答案：
import yaml
import os
import re
import subprocess
import asyncio
import logging
from datetime import datetime

# ---- 异步 ping 函数 ----
async def ping(ip):
    import sys
    param = "-n" if sys.platform == "win32" else "-c"
    try:
        # asyncio.to_thread 把同步 subprocess.run 扔到线程池里执行，不阻塞主线程
        result = await asyncio.to_thread(
            subprocess.run,
            ["ping", param, "2", ip],
            capture_output=True, text=True, timeout=3)
        return result.returncode, result.stdout
    except:
        return -1, ""   # 超时或异常 → 当作不可达

# ---- 主流程 ----
async def main():
    # 1. 读取 YAML 配置
    BASE_DIR = os.path.dirname(__file__)
    serverData = yaml.safe_load(open(os.path.join(BASE_DIR, "servers.yaml"), encoding="utf-8"))

    # 2. 初始化日志（文件 + 控制台）
    filehandler = logging.FileHandler(os.path.join(BASE_DIR, "server.log"), encoding="utf-8")
    consolehandler = logging.StreamHandler()
    logging.basicConfig(level=logging.INFO, handlers=[filehandler, consolehandler])

    # 3. 并发 ping 所有服务器
    total = len(serverData["servers"])
    reachable = 0
    results = []

    logging.info(f"开始巡检 {total} 台服务器...")

    for server in serverData["servers"]:
        ok, output = await ping(server["ip"])
        if ok == 0:
            match = re.search(r"时间[=<]\s*(\d+)ms", output)
            delay = match.group(1) if match else "?"
            logging.info(f"{server['name']} ({server['ip']}) 可达, 延迟: {delay}ms")
            results.append(f"{server['name']} ({server['ip']}) 可达, 延迟: {delay}ms")
            reachable += 1
        else:
            logging.info(f"{server['name']} ({server['ip']}) 不可达")
            results.append(f"{server['name']} ({server['ip']}) 不可达")

    # 4. 生成带时间戳的巡检报告
    report_dir = os.path.join(BASE_DIR, "reports")
    os.makedirs(report_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(report_dir, f"report_{timestamp}.txt")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"服务器巡检报告\n")
        f.write(f"{'=' * 40}\n")
        f.write(f"巡检时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"巡检结果: {reachable}/{total} 可达\n")
        f.write(f"{'=' * 40}\n")
        for line in results:
            f.write(line + "\n")

    logging.info(f"巡检完成: {reachable}/{total} 可达, 报告已保存到 {report_path}")

if __name__ == "__main__":
    asyncio.run(main())