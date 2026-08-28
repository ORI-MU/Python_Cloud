# ============================================================
# Python 云计算实战 — 第11课：执行系统命令 subprocess
# ============================================================
# 知识点：
#   subprocess.run()：执行系统命令，等命令完成
#   capture_output=True：捕获命令的输出
#   text=True：输出以字符串形式返回（而不是 bytes）
#   shell=True：允许用 shell 语法（如管道 |）
#   示例：
#     import subprocess
#     result = subprocess.run(["echo", "Hello"], capture_output=True, text=True)
#     print(result.stdout)   # Hello
# ============================================================

# ---- 题目1 ----
# 用 subprocess 执行 "dir"（Windows）列出当前目录的文件
# 捕获输出并打印
# 提示：Windows 用 ["cmd", "/c", "dir"]，或直接用 ["dir"] + shell=True

# 请在下方写下你的答案：
import subprocess
result = subprocess.run(["echo", "/c","dir"],capture_output=True,text=True)
print(result.stdout)


# ---- 题目2 ----
# 用 subprocess 执行 "ping baidu.com -n 3"（Windows，ping 3次）
# 捕获输出，判断是否成功（returncode == 0 表示成功）
# 打印 "Ping successful!" 或 "Ping failed!"

# 请在下方写下你的答案：
import subprocess
result = subprocess.run(["ping","baidu.com","-n","3"],capture_output=True,text=True)
print(result.stdout)


# ---- 题目3 ----
# 模拟一个运维场景：有一个服务器列表
# 写一个函数 ping_server(host)，ping 一次该主机，返回 True/False
# 然后遍历列表，打印每个主机的连通状态
# 提示：Windows 用 ["ping", host, "-n", "1"]

# servers = ["baidu.com", "google.com", "bing.com"]

# 请在下方写下你的答案：
import subprocess
host = "localhost"
def pingServer(host):
    result = subprocess.run(["ping",host,"-n","1"],capture_output=True,text=True)
    return result
print(result.stdout)