# ============================================================
# Python 云计算实战 — 第18课：并发编程 threading / multiprocessing
# ============================================================
# 运维场景：同时 ping 多台服务器、批量重启服务、并发下载日志
# ============================================================

# ============================================================
# 知识点1：threading.Thread — 创建和启动线程
# ============================================================
# 语法：
#   t = threading.Thread(target=函数名, args=(参数1, 参数2, ...))
#   t.start()   # 启动线程（异步执行，不阻塞主线程）
#   t.join()    # 等待线程结束（阻塞主线程直到该线程跑完）
#
# 关键：所有线程先 start()，再统一 join() → 实现并发
#       如果 start 一个就 join 一个 → 退化成串行
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import time
# import threading
#
# def check_server(name, ip):
#     """模拟检查一台服务器，耗时 2 秒"""
#     print(f"  [开始] 检查 {name} ({ip})...")
#     time.sleep(2)
#     print(f"  [完成] {name} is UP")
#
# print("=== 串行：6秒 ===")
# start = time.time()
# check_server("web-01", "10.0.1.1")  # 等2秒
# check_server("web-02", "10.0.1.2")  # 等2秒
# check_server("db-01",  "10.0.1.100")  # 等2秒
# print(f"串行耗时: {time.time() - start:.2f}s\n")
#
# print("=== 并发：2秒 ===")
# start = time.time()
# t1 = threading.Thread(target=check_server, args=("web-01", "10.0.1.1"))
# t2 = threading.Thread(target=check_server, args=("web-02", "10.0.1.2"))
# t3 = threading.Thread(target=check_server, args=("db-01",  "10.0.1.100"))
# t1.start(); t2.start(); t3.start()   # 三个同时启动
# t1.join();  t2.join();  t3.join()    # 等三个都结束
# print(f"并发耗时: {time.time() - start:.2f}s")


# ============================================================
# 知识点2：线程间共享数据 — 用列表收集返回值
# ============================================================
# 线程不能 return 值，只能通过共享变量（列表、字典）传递结果
# 每个线程写入不同位置，避免数据竞争
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import time
# import threading
#
# def calc_sum(start, end, results, index):
#     results[index] = sum(range(start, end + 1))
#
# results = [0, 0]  # 两个线程各写一个位置
# t1 = threading.Thread(target=calc_sum, args=(1, 5000000, results, 0))
# t2 = threading.Thread(target=calc_sum, args=(5000001, 10000000, results, 1))
# start = time.time()
# t1.start(); t2.start()
# t1.join(); t2.join()
# total = results[0] + results[1]
# print(f"1~1000万的和 = {total}，耗时: {time.time() - start:.2f}s")


# ============================================================
# 知识点3：multiprocessing.Process — 多进程绕开 GIL
# ============================================================
# 线程 vs 进程：
#   线程：共享内存，受 GIL 限制，CPU 计算不能真正并行 → 适合 IO 密集型
#   进程：独立内存，不受 GIL 限制，真正利用多核 → 适合 CPU 密集型
#
# 语法和 Thread 几乎一样：
#   p = Process(target=函数名, args=(参数1, 参数2, ...))
#   p.start()   # 启动进程
#   p.join()    # 等待进程结束
#
# 注意：进程间不共享内存，传结果需用 Manager().list()
#       Windows 下必须在 if __name__ == "__main__" 中执行
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import time
# from multiprocessing import Process, Manager
#
# def fib(n):
#     return n if n <= 1 else fib(n - 1) + fib(n - 2)
#
# def fib_worker(results, index):
#     results[index] = fib(35)
#
# if __name__ == "__main__":
#     # 单进程：串行算 4 次
#     start = time.time()
#     single = [fib(35) for _ in range(4)]
#     single_time = time.time() - start
#     print(f"单进程: {single}, 耗时: {single_time:.2f}s")
#
#     # 多进程：4 个进程并行
#     manager = Manager()
#     results = manager.list([0, 0, 0, 0])
#     processes = []
#     start = time.time()
#     for i in range(4):
#         p = Process(target=fib_worker, args=(results, i))
#         p.start()
#         processes.append(p)
#     for p in processes:
#         p.join()
#     mp_time = time.time() - start
#     print(f"多进程: {list(results)}, 耗时: {mp_time:.2f}s")
#     print(f"加速比: {single_time / mp_time:.1f}倍")


# ============================================================
# ---- 题目1 ----
# 用 threading 创建 5 个线程，模拟同时 ping 5 台服务器
# 函数 ping_server(name, ip)：
#   - print(f"Pinging {name} ({ip})...")
#   - time.sleep(1) 模拟 ping 耗时
#   - print(f"{name} ({ip}) is reachable")
# 5 台服务器：
#   web-01   10.0.1.1
#   web-02   10.0.1.2
#   web-03   10.0.1.3
#   db-01    10.0.1.100
#   cache-01 10.0.1.200
# 要求：并发执行，总耗时约 1 秒（不是 5 秒）
# 提示：参考知识点1，start() 启动所有线程，join() 等待所有线程
# ============================================================

# 请在下方写下你的答案：
import threading, time

def ping_server(name, ip):
    print(f"Pinging {name} ({ip})...")
    time.sleep(1)
    print(f"{name} ({ip}) is reachable")

if __name__ == "__main__":
    start = time.time()

    t1 = threading.Thread(target=ping_server,args=("web-01","10.0.1.1"))
    t2 = threading.Thread(target=ping_server,args=("web-02","10.0.1.2"))
    t3 = threading.Thread(target=ping_server,args=("web-03","10.0.1.3"))
    t4 = threading.Thread(target=ping_server,args=("db-01","10.0.1.100"))
    t5 = threading.Thread(target=ping_server,args=("cache-01","10.0.1.200"))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

    print(f"并发耗时: {time.time()-start:.2f}sec")


# ============================================================
# ---- 题目2 ----
# 用 4 个线程分段计算 1 到 20_000_000 的和，对比单线程耗时
# 提示：参考知识点2，用列表 results 收集各线程结果
# 4 段：1~5M, 5M+1~10M, 10M+1~15M, 15M+1~20M
# 要求打印：
#   单线程结果: xxx, 耗时: x.xxs
#   多线程结果: xxx, 耗时: x.xxs
# ============================================================

# 请在下方写下你的答案：
import threading,time

numbers = [[1,5000001],[5000001,10000001],[10000001,15000001],[15000001,20000001]]
results = [0,0,0,0]

def calSum(numbers,results,index):
    results[index] = sum(range(numbers[index][0], numbers[index][1]))

if __name__ == "__main__":
    singleStart = time.time()
    print(f"单线程结果: {sum(range(1,20000001))}, 耗时: {time.time()-singleStart:.02f}s")

    t1 = threading.Thread(target=calSum,args=(numbers,results,0))
    t2 = threading.Thread(target=calSum,args=(numbers,results,1))
    t3 = threading.Thread(target=calSum,args=(numbers,results,2))
    t4 = threading.Thread(target=calSum,args=(numbers,results,3))

    multiStart = time.time()

    t1.start();t2.start();t3.start();t4.start();
    t1.join();t2.join();t3.join();t4.join();

    print(f"多线程结果: {results[0]+results[1]+results[2]+results[3]}, 耗时: {time.time()-multiStart:.02f}s")

# ============================================================
# ---- 题目3 ----
# 用 multiprocessing 创建 4 个进程，每个计算 fib(35)
# 对比单进程串行 vs 多进程并行的耗时
# 提示：参考知识点3，Process 用法和 Thread 一样
#       结果收集用 Manager().list()
# 要求打印：
#   单进程结果: [xxx, xxx, xxx, xxx], 耗时: x.xxs
#   多进程结果: [xxx, xxx, xxx, xxx], 耗时: x.xxs
# ============================================================

# 请在下方写下你的答案：
import time
from multiprocessing import Process,Manager

def fib(num):
    return num if num <= 1 else fib(num-1) + fib(num-2)

def fibWorks(results,index):
    results[index] = fib(35)

if __name__ == "__main__":

    singleStart = time.time()
    single = [fib(35) for _ in range(4)]
    print(f"单进程结果: {single}, 耗时:{time.time()-singleStart:.02f}s")

    manager = Manager()
    results = manager.list([0,0,0,0])
    multiStart = time.time()
    processes = []
    for i in range(4):
        p = Process(target=fibWorks,args=(results,i))
        p.start()
        processes.append(p)
    for p in processes:
        p.join()
    print(f"多进程结果: {results}, 耗时:{time.time()-multiStart:.02f}s")