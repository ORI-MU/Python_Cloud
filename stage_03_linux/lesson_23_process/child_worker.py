# child_worker.py — 模拟工作进程，运行3秒后自动退出
# 供 23_process.py 题目2 使用
import time
import sys
import os

print(f"子进程 PID={os.getpid()} 开始工作...")
sys.stdout.flush()

for i in range(3):
    print(f"  工作中... {i+1}/3")
    sys.stdout.flush()
    time.sleep(1)

print("工作完成，退出")
sys.exit(0)