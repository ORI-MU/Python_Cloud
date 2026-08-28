# ============================================================
# Python 云计算实战 — 第19课：异步编程 asyncio / aiohttp
# ============================================================
# 运维场景：同时 ping 100 台服务器、并发调用云 API、批量下载日志
# asyncio 比 threading 更轻量，适合大量 IO 密集型任务
# ============================================================


# ============================================================
# 知识点1：async / await — 定义和运行异步函数
# ============================================================
# 语法：
#   async def 函数名():        # async 定义协程函数
#       await 异步操作()        # await 等待异步操作完成（不阻塞）
#
#   asyncio.run(协程函数())     # 运行异步函数（Python 3.7+）
#
# 关键：await 期间，程序可以切换到其他任务，不会傻等
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import asyncio
#
# async def check_server(name, ip):
#     """异步检查服务器，模拟 2 秒延迟"""
#     print(f"  [开始] 检查 {name} ({ip})...")
#     await asyncio.sleep(2)          # 异步等待，不阻塞其他任务
#     print(f"  [完成] {name} is UP")
#
# async def main():
#     print("=== 并发检查 3 台服务器 ===")
#     start = time.time()
#     # asyncio.gather() 同时运行多个协程
#     await asyncio.gather(
#         check_server("web-01", "10.0.1.1"),
#         check_server("web-02", "10.0.1.2"),
#         check_server("db-01",  "10.0.1.100"),
#     )
#     print(f"耗时: {time.time() - start:.2f}s（3台同时 ≈ 2秒）")
#
# if __name__ == "__main__":
#     import time
#     asyncio.run(main())


# ============================================================
# 知识点2：asyncio.create_task — 动态创建并发任务
# ============================================================
# asyncio.gather() 适合固定数量的任务
# asyncio.create_task() 适合动态创建（如服务器列表可变）
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import asyncio
# import time
#
# async def ping(name, ip):
#     print(f"  Pinging {name} ({ip})...")
#     await asyncio.sleep(1)
#     print(f"  {name} is reachable")
#     return f"{name}: OK"
#
# async def main():
#     servers = [
#         ("web-01", "10.0.1.1"),
#         ("web-02", "10.0.1.2"),
#         ("web-03", "10.0.1.3"),
#         ("db-01",  "10.0.1.100"),
#         ("cache-01", "10.0.1.200"),
#     ]
#     start = time.time()
#     tasks = [asyncio.create_task(ping(name, ip)) for name, ip in servers]
#     results = await asyncio.gather(*tasks)   # *tasks 解包列表
#     print(f"结果: {results}")
#     print(f"耗时: {time.time() - start:.2f}s（5台同时 ≈ 1秒）")
#
# if __name__ == "__main__":
#     asyncio.run(main())


# ============================================================
# 知识点3：aiohttp — 异步 HTTP 请求（并发调用云 API）
# ============================================================
# aiohttp 是异步版 requests，可以同时发大量 HTTP 请求
# 需要安装：pip install aiohttp
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import asyncio
# import time
# import aiohttp
#
# async def fetch_status(session, url):
#     """异步获取 URL 状态码"""
#     async with session.get(url) as resp:
#         return url, resp.status
#
# async def main():
#     urls = [
#         "https://httpbin.org/delay/1",  # 模拟延迟 1 秒
#         "https://httpbin.org/delay/1",
#         "https://httpbin.org/delay/1",
#     ]
#     start = time.time()
#     async with aiohttp.ClientSession() as session:
#         tasks = [fetch_status(session, url) for url in urls]
#         results = await asyncio.gather(*tasks)
#     for url, status in results:
#         print(f"  {url} → {status}")
#     print(f"耗时: {time.time() - start:.2f}s（3个请求同时 ≈ 1秒）")
#
# if __name__ == "__main__":
#     asyncio.run(main())


# ============================================================
# ---- 题目1 ----
# 用 asyncio 并发 ping 8 台服务器（不能用 threading）
# 函数 ping_server(name, ip)：
#   - print(f"Pinging {name} ({ip})...")
#   - await asyncio.sleep(1) 模拟 ping
#   - print(f"{name} is reachable")
# 8 台服务器：
#   web-01~web-05 (10.0.1.1~10.0.1.5)
#   db-01 (10.0.1.100)
#   cache-01 (10.0.1.200)
#   lb-01 (10.0.1.250)
# 要求：并发执行，总耗时约 1 秒（不是 8 秒）
# 提示：参考知识点2，用 asyncio.create_task + asyncio.gather
# ============================================================

# 请在下方写下你的答案：
import asyncio
import time
async def ping_server(name, ip):
    print(f"Pinging {name} ({ip})...")
    await asyncio.sleep(1)
    print(f"{name} is reachable")

async def main():
    servers = [("web-01","10.0.1.1"),("web-02","10.0.1.2"),
               ("web-03","10.0.1.3"),("web-04","10.0.1.4"),
               ("web-05","10.0.1.5"),("db-01","10.0.1.100"),
               ("cache-01","10.0.1.200"),("lb-01","10.0.1.250")
               ]
    start = time.time()
    tasks = [asyncio.create_task(ping_server(name, ip)) for name, ip in servers]
    results = await asyncio.gather(*tasks)
    print(f"结果: {results}")
    print(f"耗时: {time.time()-start:4.2f}s")

if __name__ == "__main__":
    asyncio.run(main())
    

# ============================================================
# ---- 题目2 ----
# 用 asyncio 异步下载 3 个网页，打印状态码和耗时
# 网页：
#   https://httpbin.org/delay/1
#   https://httpbin.org/delay/2
#   https://httpbin.org/delay/3
# 提示：参考知识点3，需要 pip install aiohttp
# 要求打印：
#   https://httpbin.org/delay/1 → 200
#   https://httpbin.org/delay/2 → 200
#   https://httpbin.org/delay/3 → 200
#   总耗时: x.xxs（并发 ≈ 3秒，不是 6秒）
# ============================================================

# 请在下方写下你的答案：
import asyncio
import time
import aiohttp

async def fetchStatus(session, url):
    async with session.get(url) as res:
        return url, res.status

async def main():
    urls = ["https://httpbin.org/delay/1","https://httpbin.org/delay/2","https://httpbin.org/delay/3"]

    start = time.time()
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetchStatus(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
    for url, status in results:
        print(f"{url} -> {status}")
    print(f"总耗时: {time.time()-start:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())


# ============================================================
# ---- 题目3 ----
# 用 asyncio + aiohttp 并发调用 JSONPlaceholder API
# 同时获取 5 个用户的 Todo 列表：
#   https://jsonplaceholder.typicode.com/todos/1
#   https://jsonplaceholder.typicode.com/todos/2
#   https://jsonplaceholder.typicode.com/todos/3
#   https://jsonplaceholder.typicode.com/todos/4
#   https://jsonplaceholder.typicode.com/todos/5
# 要求：解析 JSON，打印每个 Todo 的 title 和 completed 状态
# 提示：resp.json() 返回 dict，await resp.json() 是异步版
# 要求打印：
#   Todo 1: "delectus aut autem" (completed: False)
#   Todo 2: "quis ut nam facilis..." (completed: False)
#   ...
#   总耗时: x.xxs
# ============================================================

# 请在下方写下你的答案：
import asyncio
import aiohttp
import time

async def fetchTodos(session, url):
    async with session.get(url) as res:
        data = await res.json()
    return url, data

async def main():
    urls = ["https://jsonplaceholder.typicode.com/todos/1",
            "https://jsonplaceholder.typicode.com/todos/2",
            "https://jsonplaceholder.typicode.com/todos/3",
            "https://jsonplaceholder.typicode.com/todos/4",
            "https://jsonplaceholder.typicode.com/todos/5"
            ]

    start = time.time() 
    async with aiohttp.ClientSession() as session:
        tasks = [asyncio.create_task(fetchTodos(session, url)) for url in urls]
        results = await asyncio.gather(*tasks)
    for url, data in results:
        print(f"Todo {data['id']}: \"{data['title']}\" (completed: {data['completed']})")
    print(f"总耗时: {time.time()-start:.2f}s")

if __name__ == "__main__":
    asyncio.run(main())