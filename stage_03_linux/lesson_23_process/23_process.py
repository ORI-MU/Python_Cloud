# ============================================================
# Python 云计算运维 — 第23课：进程管理 ps / top / kill
# ============================================================
# 第三阶段：Linux 基础
# 目标：理解 Linux 进程管理，用 Python 查看/监控/终止进程
# ============================================================
# 注意：Windows 上 signal/kill 部分受限，完整功能需在 Linux 上验证
# ============================================================


# ============================================================
# 知识点1：进程基础概念
# ============================================================
# PID   → 进程ID，唯一标识一个进程
# PPID  → 父进程ID，谁创建了它
# 进程状态：
#   R = Running（运行中）
#   S = Sleeping（等待中，最常见）
#   D = 不可中断睡眠（等IO）
#   Z = Zombie（僵尸进程，已死但父进程未回收）
#   T = Stopped（暂停）
#
# Linux 进程信息在 /proc 目录下：
#   /proc/[pid]/status   → 进程状态
#   /proc/[pid]/cmdline  → 启动命令
#   /proc/[pid]/cwd      → 工作目录
#   /proc/[pid]/fd/      → 打开的文件描述符
#
# Python 获取自身进程信息：
#   os.getpid()    → 当前进程 PID
#   os.getppid()   → 父进程 PID
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import os
#
# print(f"当前进程 PID:  {os.getpid()}")
# print(f"父进程 PPID:   {os.getppid()}")
#
# # 模拟在 /proc 中查看进程信息（仅 Linux）
# pid = os.getpid()
# proc_status = f"/proc/{pid}/status"
# try:
#     with open(proc_status) as f:
#         for line in f:
#             if line.startswith("Name:") or line.startswith("State:"):
#                 print(line.strip())
# except FileNotFoundError:
#     print("Windows 没有 /proc，请切换到 Linux 运行此示例")


# ============================================================
# 知识点2：subprocess 执行 ps 命令查看进程
# ============================================================
# Linux 常用 ps 命令：
#   ps aux          → 查看所有进程
#   ps -ef          → 另一种格式查看所有进程
#   ps -u ori       → 查看某个用户的进程
#   ps -C nginx     → 按进程名查找
#   ps aux | grep python → 查找 Python 进程
#
# Windows 等价命令：
#   tasklist        → 查看所有进程
#   tasklist /FI "IMAGENAME eq python.exe"  → 按名称过滤
#   tasklist /FI "PID eq 1234"              → 按PID过滤
#
# 用 Python subprocess 调用：
#   subprocess.run(["ps", "aux"], capture_output=True, text=True)
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import subprocess
# import platform
# import os
#
# print(f"当前系统: {platform.system()}")
#
# if platform.system() == "Windows":
#     # Windows 用 tasklist
#     result = subprocess.run(
#         ["tasklist", "/FI", f"PID eq {os.getpid()}"],
#         capture_output=True, text=True
#     )
# else:
#     # Linux 用 ps
#     result = subprocess.run(
#         ["ps", "-p", str(os.getpid()), "-o", "pid,ppid,user,comm"],
#         capture_output=True, text=True
#     )
#
# print("当前进程信息:")
# print(result.stdout)


# ============================================================
# 知识点3：psutil 库 — 跨平台进程管理
# ============================================================
# psutil 是 Python 进程管理的瑞士军刀，跨平台（Windows/Linux/macOS）
# 安装：py -m pip install psutil
#
# 常用 API：
#   psutil.pids()                    → 所有进程 PID 列表
#   psutil.Process(pid)              → 获取某个进程对象
#   p.name()                         → 进程名
#   p.exe()                          → 可执行文件路径
#   p.cmdline()                      → 启动命令行
#   p.cpu_percent(interval=1)        → CPU 使用率
#   p.memory_info().rss              → 内存占用（字节）
#   p.memory_percent()               → 内存占用百分比
#   p.status()                       → 进程状态
#   p.create_time()                  → 创建时间
#   p.parent()                       → 父进程
#   p.children()                     → 子进程列表
#   p.terminate()                    → 发送 SIGTERM（优雅退出）
#   p.kill()                         → 发送 SIGKILL（强制杀死）
#   p.wait(timeout=3)                → 等待进程结束
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import psutil
# import os
#
# # 获取当前进程信息
# p = psutil.Process(os.getpid())
# print(f"PID: {p.pid}")
# print(f"名称: {p.name()}")
# print(f"状态: {p.status()}")
# print(f"命令行: {p.cmdline()}")
# print(f"内存: {p.memory_info().rss / 1024 / 1024:.2f} MB")
# print(f"创建时间: {p.create_time()}")
#
# # 查看父进程
# parent = p.parent()
# if parent:
#     print(f"父进程: {parent.name()} (PID={parent.pid})")


# ============================================================
# 知识点4：信号与进程终止 — kill / terminate
# ============================================================
# Linux 常用信号：
#   SIGTERM (15) → 终止（可被捕获，优雅退出）
#   SIGKILL  (9) → 强制杀死（不可捕获，终极手段）
#   SIGINT   (2) → 中断（Ctrl+C）
#   SIGHUP   (1) → 挂起（常用来重载配置）
#   SIGSTOP (19) → 暂停进程
#   SIGCONT (18) → 继续进程
#
# 口诀：TERM 优雅，KILL 暴力，HUP 重载配
#
# Python 终止进程：
#   os.kill(pid, signal.SIGTERM)    → Linux only
#   subprocess.Popen 对象:
#       proc.terminate()  → 等价 SIGTERM
#       proc.kill()       → 等价 SIGKILL
#   psutil 对象:
#       p.terminate()     → 等价 SIGTERM
#       p.kill()          → 等价 SIGKILL
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import subprocess
# import time
# import os
# import signal
#
# # 启动一个子进程（长时间运行）
# if os.name == "nt":
#     proc = subprocess.Popen(["ping", "-n", "30", "127.0.0.1"],
#         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
# else:
#     proc = subprocess.Popen(["sleep", "30"])
#
# print(f"子进程 PID: {proc.pid}")
# print(f"进程状态: {'运行中' if proc.poll() is None else '已结束'}")
#
# time.sleep(1)
#
# # 优雅终止
# proc.terminate()
# print("已发送 terminate()")
# time.sleep(0.5)
# print(f"进程状态: {'运行中' if proc.poll() is None else f'已结束(退出码={proc.returncode})'}")
#
# # 如果还没死，强制 kill
# if proc.poll() is None:
#     proc.kill()
#     print("已发送 kill()")
#     proc.wait()
#     print(f"进程已强制结束(退出码={proc.returncode})")


# ============================================================
# 知识点5：subprocess.Popen 进程生命周期管理
# ============================================================
# 语法：
#   proc = subprocess.Popen(
#       ["命令", "参数1", "参数2"],
#       stdout=subprocess.PIPE,    # 捕获标准输出
#       stderr=subprocess.PIPE,    # 捕获标准错误
#       text=True,                 # 以文本模式返回
#       cwd="/path/to/dir",        # 指定工作目录
#   )
#
# 关键方法：
#   proc.poll()     → 检查进程是否结束（返回 None=运行中, 数字=退出码）
#   proc.wait()     → 阻塞等待进程结束
#   proc.terminate()→ 发送 SIGTERM
#   proc.kill()     → 发送 SIGKILL
#   proc.communicate(timeout=5) → 等待结束并获取输出（带超时）
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import subprocess
# import time
#
# # 启动进程并获取输出
# if os.name == "nt":
#     proc = subprocess.Popen(
#         ["ping", "-n", "2", "127.0.0.1"],
#         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
#     )
# else:
#     proc = subprocess.Popen(
#         ["ping", "-c", "2", "127.0.0.1"],
#         stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
#     )
#
# print(f"PID={proc.pid} 运行中...")
#
# # 等待完成（带超时）
# try:
#     stdout, stderr = proc.communicate(timeout=10)
#     print(f"退出码: {proc.returncode}")
#     print(f"输出: {stdout[:200]}")
# except subprocess.TimeoutExpired:
#     print("超时！强制终止")
#     proc.kill()
#     stdout, stderr = proc.communicate()


# ============================================================
# ---- 题目1：进程列表查看器 ----
# ============================================================
# 场景：运维需要快速查看当前系统中 Python 相关的进程
# 写一个脚本，列出所有进程，筛选出 Python 相关进程，显示关键信息
#
# 要求：
# 1. 用 psutil 获取所有进程
# 2. 筛选名称包含 "python" 的进程（不区分大小写）
# 3. 对每个进程显示：PID、名称、内存(MB)、状态
# 4. 按内存占用降序排列
# 5. 统计总数和总内存占用
#
# 预期输出：
#    PID   名称              内存(MB)   状态
#    ----  ----------------  ---------  ------
#    1234   python.exe        45.23      running
#    5678   python.exe        12.10      running
#    ---
#    共 2 个 Python 进程, 总内存: 57.33 MB
#
# 提示：
#   - 用 psutil.process_iter() 遍历所有进程
#   - 用 p.info 获取 name/pid/memory_info
#   - 用 try/except 处理无权限访问的进程
# ============================================================

# 请在下方写下你的答案：
import os
import psutil

procs = []
for proc in psutil.process_iter(["pid","name","memory_info","status"]):
    try:
        info = proc.info
        if "python" in info["name"].lower():
            memory = info["memory_info"].rss / 1024 /1024
            procs.append({
                "pid": info["pid"],
                "name": info["name"],
                "memory": memory,
                "status": info["status"]
            })
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

procs.sort(key=lambda p: p["memory"], reverse=True)

print("      PID   名称              内存(MB)   状态")
print("   ----  ----------------  ---------  ------")
for p in procs:
    print(f"{p['pid']:>6}  {p['name']:<20} {p['memory']:>10.2f}  {p['status']}")
print(f"{'---':>6}")
total_mem = sum(p['memory'] for p in procs)
print(f"共 {len(procs)} 个 Python 进程, 总内存: {total_mem:.2f} MB")

# ============================================================
# ---- 题目2：进程守护者 — 自动重启崩溃进程 ----
# ============================================================
# 场景：运维需要监控某个关键进程，如果它挂了就自动重启
# 写一个脚本，模拟启动一个子进程，监控它，挂了就自动重启
#
# 要求：
# 1. 创建一个模拟脚本 child_worker.py（见下方），它会运行3秒后退出
# 2. 用 subprocess.Popen 启动 child_worker.py
# 3. 循环监控：每1秒检查一次进程是否存活
# 4. 如果进程退出，打印重启信息并重新启动
# 5. 最多重启 3 次，超过则放弃
# 6. 打印每次重启的时间戳
#
# 预期输出：
#   [14:30:01] 启动子进程 PID=12345
#   [14:30:04] 进程退出(退出码=0)，准备重启...
#   [14:30:04] 重启子进程 PID=12346 (第1次重启)
#   [14:30:07] 进程退出(退出码=0)，准备重启...
#   [14:30:07] 重启子进程 PID=12347 (第2次重启)
#   [14:30:10] 进程退出(退出码=0)，准备重启...
#   [14:30:10] 重启子进程 PID=12348 (第3次重启)
#   [14:30:13] 进程退出(退出码=0)，已达最大重启次数，放弃
#
# 提示：
#   - 用 time.strftime("%H:%M:%S") 格式化时间
#   - 用 proc.poll() 检查进程是否存活
#   - 用 proc.wait() 等待进程结束获取退出码
# ============================================================

# 请在下方写下你的答案：
import subprocess
import time
from pathlib import Path

worker = Path(__file__).parent / "child_worker.py"
proc = subprocess.Popen(["py", worker])
restart_counter = 0
max_restart = 3

print(f"{time.strftime('%H:%M:%S')}启动子进程 PID={proc.pid}")
while restart_counter <= max_restart:
    time.sleep(1)
    if proc.poll() is not None:
        exit_code = proc.wait()
        if restart_counter < max_restart:
            restart_counter += 1
            print(f"[{time.strftime('%H:%M:%S')}] 进程退出(退出码={exit_code})，准备重启...")
            proc = subprocess.Popen(["py", worker])
            print(f"[{time.strftime('%H:%M:%S')}] 重启子进程 PID={proc.pid} (第{restart_counter}次重启)")
        else:
             print(f"[{time.strftime('%H:%M:%S')}] 进程退出(退出码={exit_code})，已达最大重启次数，放弃")
             break




# ============================================================
# ---- 题目3：简易进程监控仪表盘 ----
# ============================================================
# 场景：运维需要快速了解系统资源 Top 消耗者
# 写一个脚本，显示 CPU 和内存占用最高的前 5 个进程
#
# 要求：
# 1. 用 psutil 获取所有进程
# 2. 分别找出 CPU 占用 Top 5 和 内存占用 Top 5
# 3. 显示格式：PID、名称、CPU%、内存%
# 4. 先显示 CPU Top 5，再显示内存 Top 5
# 5. 处理无权限进程（跳过）
#
# 预期输出：
#   === CPU 占用 Top 5 ===
#   PID    名称                  CPU%    内存%
#   ------ -------------------- -------- --------
#   1234    chrome.exe           25.30%   12.50%
#   5678    python.exe           15.20%    3.20%
#   ...
#
#   === 内存占用 Top 5 ===
#   PID    名称                  内存(MB)
#   ------ -------------------- ---------
#   9012    chrome.exe            1024.50
#   3456    java.exe               512.30
#   ...
#
# 提示：
#   - cpu_percent() 第一次调用返回 0，需要先调用一次再 sleep 后获取
#   - 或者直接遍历进程，用 p.cpu_percent(interval=0.1)
#   - 用 sorted(processes, key=lambda x: x["cpu"], reverse=True)[:5]
# ============================================================

# 请在下方写下你的答案（已写好，读一遍即可）：
import psutil
import time

def get_top_cpu(limit=5):
    procs = []
    for p in psutil.process_iter(["pid", "name"]):
        try:
            p.cpu_percent()  # 第一轮空跑，打时间戳
            procs.append(p)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    time.sleep(0.5)  # 等一会再取真实值

    result = []
    for p in procs:
        try:
            cpu = p.cpu_percent()  # 第二轮拿真实值
            mem = p.memory_percent()
            result.append({"pid": p.pid, "name": p.info["name"], "cpu": cpu, "mem": mem})
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    result.sort(key=lambda x: x["cpu"], reverse=True)
    return result[:limit]


def get_top_mem(limit=5):
    result = []
    for p in psutil.process_iter(["pid", "name", "memory_info"]):
        try:
            mem_mb = p.info["memory_info"].rss / 1024 / 1024
            result.append({"pid": p.pid, "name": p.info["name"], "mem": mem_mb})
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    result.sort(key=lambda x: x["mem"], reverse=True)
    return result[:limit]


print("=== CPU 占用 Top 5 ===")
print(f"{'PID':>6}  {'名称':<20} {'CPU%':>8}  {'内存%'}")
print(f"{'------':>6}  {'--------------------':<20} {'--------':>8}  {'------'}")
for p in get_top_cpu():
    print(f"{p['pid']:>6}  {p['name']:<20} {p['cpu']:>7.2f}%  {p['mem']:.2f}%")

print()
print("=== 内存占用 Top 5 ===")
print(f"{'PID':>6}  {'名称':<20} {'内存(MB)':>10}")
print(f"{'------':>6}  {'--------------------':<20} {'---------':>10}")
for p in get_top_mem():
    print(f"{p['pid']:>6}  {p['name']:<20} {p['mem']:>10.2f}")