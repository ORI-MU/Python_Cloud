# ============================================================
# Python 云计算运维 — 第24课：Shell 脚本入门 bash
# ============================================================
# 第三阶段：Linux 基础
# 目标：理解 Bash Shell 脚本语法，能用 Python 生成/调用/解析 Shell 脚本
# ============================================================
# 注意：本机有 bash (Cygwin)，脚本在 Windows 上也能运行
# ============================================================


# ============================================================
# 知识点1：Shell 脚本基础 — shebang 与运行方式
# ============================================================
# Shell 脚本 = 一系列 Shell 命令的集合，第一行 shebang 指定解释器
#
# 创建步骤：
# 1. 写 .sh 文件，第一行 #!/bin/bash
# 2. chmod +x 添加执行权限
# 3. ./script.sh 或 bash script.sh 运行
#
# shebang 常见写法：
#   #!/bin/bash          → 标准 Bash
#   #!/bin/sh            → POSIX Shell（兼容性最好）
#   #!/usr/bin/env bash  → 自动查找 bash 路径（推荐跨平台）
#
# 运行方式：
#   bash script.sh       → 不需要执行权限，子 Shell 中运行
#   ./script.sh          → 需要执行权限，子 Shell 中运行
#   source script.sh     → 当前 Shell 中运行（可修改环境变量）
#   . script.sh          → 同 source
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import os
# import subprocess
#
# # 用 Python 创建一个最简单的 Shell 脚本
# script = Path(__file__).parent / "hello.sh"
# script.write_text("#!/bin/bash\necho 'Hello from Shell!'\necho \"Today is $(date)\"\n", encoding="utf-8")
#
# # 运行脚本
# result = subprocess.run(["bash", str(script)], capture_output=True, text=True)
# print("=== Shell 脚本输出 ===")
# print(result.stdout)


# ============================================================
# 知识点2：Bash 变量
# ============================================================
# 定义变量：等号两边不能有空格！
#   name="ori"          → 定义字符串
#   count=42            → 定义数字
#
# 引用变量：$ 符号
#   echo $name          → 输出 ori
#   echo ${name}        → 推荐写法，避免歧义
#   echo "${name}_suffix" → 需要花括号区分边界
#
# 命令替换：
#   now=$(date)         → 推荐写法，把命令输出赋给变量
#   now=`date`          → 旧式写法，不推荐
#
# 环境变量：
#   echo $HOME          → 用户主目录
#   echo $USER          → 当前用户名
#   echo $PATH          → 命令搜索路径
#   export MY_VAR=val   → 导出为环境变量，子进程可见
#
# 只读变量：
#   readonly PI=3.14    → 不可修改
#   declare -r PI=3.14  → 另一种写法
# ============================================================

# # ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess

# script = Path(__file__).parent / "vars.sh"
# script.write_text("""#!/bin/bash
# name="cloud_engineer"
def batch_execute_commands(servers=None, commands=None, timeout=10):
    servers = servers or ["web-01", "web-02", "db-01"]
    commands = commands or ["uptime", "whoami", "pwd"]

    print("=== 批量执行报告 ===")
    successes = 0
    fails = 0

    for server in servers:
        print(f"[{server}]")
        for cmd in commands:
            try:
                start = time.perf_counter()
                result = subprocess.run(
                    ["bash", "-c", cmd],
                    capture_output=True, encoding="utf-8",
                    text=True, timeout=timeout
                )
                elapsed = time.perf_counter() - start
                if result.returncode == 0:
                    status = "OK"
                    successes += 1
                else:
                    status = "FAILED"
                    fails += 1
                print(f"  {cmd} -> {status} ({elapsed:.1f}s)")
            except subprocess.TimeoutExpired:
                fails += 1
                print(f"  {cmd} -> FAILED (timeout)")

    total = successes + fails
    print(f" === 成功: {successes}/{total}, 失败: {fails}/{total} ===")

batch_execute_commands()

# count=100
# now=$(date +%H:%M:%S)

# echo "用户: ${name}"
# echo "计数: ${count}"
# echo "时间: ${now}"
# echo "主目录: $HOME"
# echo "搜索路径: $PATH" | head -c 80
# echo "..."
# """, encoding="utf-8")

# result = subprocess.run(["bash", str(script)], capture_output=True, text=True, encoding="utf-8")
# print(result.stdout)


# ============================================================
# 知识点3：Bash 条件判断 — if / else / test
# ============================================================
# 语法：
#   if [ 条件 ]; then
#       命令
#   elif [ 条件 ]; then
#       命令
#   else
#       命令
#   fi
#
# 注意：[ ] 内侧必须有空格！[ $a == $b ] 不是 [$a==$b]
#
# 数值比较：
#   [ $a -eq $b ]  → 等于 (equal)
#   [ $a -ne $b ]  → 不等于 (not equal)
#   [ $a -gt $b ]  → 大于 (greater than)
#   [ $a -lt $b ]  → 小于 (less than)
#   [ $a -ge $b ]  → 大于等于
#   [ $a -le $b ]  → 小于等于
#
# 字符串比较：
#   [ "$a" == "$b" ]   → 等于
#   [ "$a" != "$b" ]   → 不等于
#   [ -z "$a" ]        → 是否为空 (zero length)
#   [ -n "$a" ]        → 是否非空
#
# 文件测试：
#   [ -f "file" ]  → 是普通文件
#   [ -d "dir"  ]  → 是目录
#   [ -e "path" ]  → 存在
#   [ -r "file" ]  → 可读
#   [ -w "file" ]  → 可写
#   [ -x "file" ]  → 可执行
#   [ -s "file" ]  → 非空文件
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# script = Path(__file__).parent / "condition.sh"
# script.write_text("""#!/bin/bash
# log_file="/var/log/syslog"
# disk_usage=85
#
# # 文件测试
# if [ -f "$log_file" ]; then
#     echo "日志文件存在: $log_file"
# else
#     echo "日志文件不存在 (Windows 正常)"
# fi
#
# # 数值比较
# if [ $disk_usage -gt 80 ]; then
#     echo "⚠️  磁盘使用率 ${disk_usage}%，超过80%阈值！"
# else
#     echo "✅ 磁盘使用率 ${disk_usage}%，正常"
# fi
#
# # 字符串比较
# os_type=$(uname -s)
# if [ "$os_type" == "Linux" ]; then
#     echo "运行在 Linux 上"
# else
#     echo "运行在 $os_type 上"
# fi
# """, encoding="utf-8")
#
# result = subprocess.run(["bash", str(script)], capture_output=True, text=True)
# print(result.stdout)


# ============================================================
# 知识点4：Bash 循环 — for / while
# ============================================================
# for 循环语法：
#   for var in 列表; do
#       命令
#   done
#
#   列表可以是：
#   for i in 1 2 3 4 5              → 空格分隔
#   for i in {1..10}                → 范围（Bash 特有）
#   for i in $(seq 1 10)            → seq 命令生成
#   for file in /etc/*.conf         → 通配符展开
#   for item in $(cat list.txt)     → 命令输出
#
# while 循环语法：
#   while [ 条件 ]; do
#       命令
#   done
#
# 常用场景：
#   while read line; do ... done < file.txt  → 逐行读取文件
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# script = Path(__file__).parent / "loop.sh"
# script.write_text("""#!/bin/bash
# echo "=== for 循环：批量创建目录 ==="
# for i in {1..3}; do
#     echo "  创建目录: project_${i}"
#     mkdir -p "/tmp/test_project_${i}"
# done
#
# echo ""
# echo "=== for 循环：遍历文件列表 ==="
# for file in /etc/host*; do
#     if [ -f "$file" ]; then
#         echo "  配置文件: $file"
#     fi
# done
#
# echo ""
# echo "=== while 循环：倒计时 ==="
# count=3
# while [ $count -gt 0 ]; do
#     echo "  倒计时: $count"
#     count=$((count - 1))
# done
# echo "  启动！"
# """, encoding="utf-8")
#
# result = subprocess.run(["bash", str(script)], capture_output=True, text=True)
# print(result.stdout)


# ============================================================
# 知识点5：Bash 函数
# ============================================================
# 语法：
#   function_name() {
#       命令
#       return 0  # 可选，返回状态码（0=成功，非0=失败）
#   }
#
# 调用：直接写函数名，不加括号
#   function_name
#   function_name arg1 arg2
#
# 函数参数：
#   $1, $2, ... $9  → 第1个、第2个参数
#   $#              → 参数个数
#   $@              → 所有参数（作为独立字符串）
#   $*              → 所有参数（作为一个字符串）
#
# 局部变量：
#   local var="value"  → 函数内部变量，不影响外部
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# script = Path(__file__).parent / "func.sh"
# script.write_text("""#!/bin/bash
# # 定义一个日志函数
# log_info() {
#     local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
#     echo "[${timestamp}] [INFO] $1"
# }
#
# log_error() {
#     local timestamp=$(date '+%Y-%m-%d %H:%M:%S')
#     echo "[${timestamp}] [ERROR] $1" >&2
# }
#
# # 检查磁盘的函数
# check_disk() {
#     local threshold=${1:-80}
#     local usage=$(df -h / | tail -1 | awk '{print $5}' | tr -d '%' 2>/dev/null || echo "N/A")
#     log_info "磁盘使用率: ${usage}% (阈值: ${threshold}%)"
# }
#
# log_info "开始系统检查..."
# check_disk 90
# log_info "系统检查完成"
# """, encoding="utf-8")
#
# result = subprocess.run(["bash", str(script)], capture_output=True, text=True)
# print(result.stdout)


# ============================================================
# 知识点6：特殊变量与退出码
# ============================================================
# 特殊变量：
#   $0      → 脚本名称
#   $1~$9   → 命令行参数
#   $#      → 参数个数
#   $@      → 所有参数（推荐用 "$@" 保留空格）
#   $?      → 上一条命令的退出码（0=成功）
#   $$      → 当前 Shell 的 PID
#   $!      → 最后一个后台进程的 PID
#
# 退出码：
#   exit 0  → 正常退出
#   exit 1  → 异常退出（1~255）
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# script = Path(__file__).parent / "special.sh"
# script.write_text("""#!/bin/bash
# echo "脚本名称: $0"
# echo "参数个数: $#"
# echo "所有参数: $@"
# echo "当前PID: $$"
#
# for i in "$@"; do
#     echo "  参数: $i"
# done
#
# # 检查上一条命令是否成功
# ls /nonexistent 2>/dev/null
# if [ $? -ne 0 ]; then
#     echo "上一条命令失败了（退出码非0）"
# fi
#
# exit 0
# """, encoding="utf-8")
#
# result = subprocess.run(
#     ["bash", str(script), "arg1", "arg2", "arg3"],
#     capture_output=True, text=True
# )
# print(result.stdout)
# print(f"脚本退出码: {result.returncode}")


# ============================================================
# 知识点7：Python 调用 Shell 脚本的完整流程
# ============================================================
# 运维中常见模式：Python 做编排，Shell 做执行
#
# Python 生成 Shell 脚本：
#   - 用字符串模板拼接 Shell 命令
#   - 写入 .sh 文件
#   - 用 subprocess.run() 执行
#   - 检查 returncode 和 stderr
#
# 传参方式：
#   - 命令行参数：subprocess.run(["bash", "script.sh", "arg1", "arg2"])
#   - 环境变量：subprocess.run(..., env={"MY_VAR": "val"})
#   - 标准输入：subprocess.run(..., input="data", text=True)
#
# 安全注意事项：
#   - 永远不要拼接用户输入到 Shell 命令中（Shell 注入风险）
#   - 用列表形式传参，不要用 shell=True
#   - 敏感信息（密码）用环境变量传递，不要写进命令行
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
# import os
#
# script = Path(__file__).parent / "python_driven.sh"
# script.write_text("""#!/bin/bash
# echo "被 Python 调用的 Shell 脚本"
# echo "收到参数: $@"
# echo "环境变量 MY_ENV: ${MY_ENV:-未设置}"
# echo "工作目录: $(pwd)"
# """, encoding="utf-8")
#
# # 方式1：命令行参数
# result = subprocess.run(
#     ["bash", str(script), "deploy", "production"],
#     capture_output=True, text=True
# )
# print("=== 方式1：命令行参数 ===")
# print(result.stdout)
#
# # 方式2：环境变量
# result = subprocess.run(
#     ["bash", str(script)],
#     capture_output=True, text=True,
#     env={**os.environ, "MY_ENV": "hello_from_python"}
# )
# print("=== 方式2：环境变量 ===")
# print(result.stdout)


# ============================================================
# ---- 题目1：用 Python 生成健康检查脚本并执行 ----
# ============================================================
# 场景：运维需要为多台服务器生成统一的健康检查脚本
# 写一个 Python 函数，动态生成 Shell 脚本并执行
#
# 要求：
# 1. 写一个函数 generate_health_check(server_name, disk_threshold)，生成
#    一个名为 health_check_<server_name>.sh 的脚本
# 2. 脚本内容包含以下检查项：
#    - 打印服务器名称
#    - 检查当前时间
#    - 检查磁盘使用率（df -h /），如果超过阈值则警告
#    - 检查内存使用情况（free -h 或 vmstat）
#    - 检查当前运行的进程数（ps aux | wc -l）
#    - 用函数封装每个检查项，main 函数统一调用
# 3. 脚本生成后立即执行，并打印输出
# 4. 脚本中包含完整的 shebang 和注释
#
# 预期输出：
#   ======== 健康检查报告: web-server-01 ========
#   检查时间: 2024-01-01 12:00:00
#   [OK]磁盘使用率: 45% (阈值: 80%) 
#   [OK] 内存使用: ...
#   [OK] 运行进程数: ...
#   ======== 检查完成 ========
#
# 提示：
#   - 用 f-string 拼接 Shell 脚本内容
#   - 用 Path.write_text() 写入文件
#   - 用 subprocess.run(["bash", str(script_path)], ...) 执行
#   - 用 df -h / | tail -1 | awk '{print $5}' 获取磁盘使用率
# ============================================================

# 请在下方写下你的答案：
import os
from datetime import datetime
import subprocess
from pathlib import Path

def generate_health_check(server_name, disk_threshold):
    script_dir = Path(__file__).parent
    script_path = script_dir / f"health_check_{server_name}.sh"

    script_content = f"""
#!/bin/bash
# ==================================================
# 健康检查脚本
# ==================================================
SERVER_NAME="{server_name}"
DISK_THRESHOLD="{disk_threshold}"

check_time() {{
    echo "检查时间: $(date '+%Y-%m-%d %H:%M:%S')"
}}

check_disk() {{
    local usage=$(df -h | tail -1 | awk '{{print $5}}' | tr -d '%')
    if [ -z "$usage" ]; then
        usage="N/A"
    fi
    if [ "$usage" != "N/A" ] && [ $usage -gt $DISK_THRESHOLD ]; then
        echo "[WARN] 磁盘使用率: ${{usage}}% (阈值: ${{DISK_THRESHOLD}}%)"
    else
        echo "[OK] 磁盘使用率: ${{usage}}% (阈值: ${{DISK_THRESHOLD}}%)"
    fi
}}

check_memory() {{
    echo "[OK] 内存使用: "
    free -h 2>/dev/null | head -2 || vmstat 2>/dev/null | head -2 || echo "  无法获取内存信息"
}}

check_processes() {{
    local pcount=$(ps aux | wc -l 2>/dev/null)
    if [ -z "$pcount" ] || [ "$pcount" -eq 0 ]; then
        pcount="N/A"
    fi
    echo "[OK] 运行进程数: $pcount"
}}

main() {{
    echo "======== 健康检查报告: $SERVER_NAME ========"
    check_time
    check_disk
    check_memory
    check_processes
    echo "======== 检查完成 ========"
}}

main
"""

    script_path.write_text(script_content, encoding="utf-8")
    result = subprocess.run(["bash", str(script_path)], capture_output=True, encoding="utf-8")
    print(result.stdout)
    if(result.stderr):
        print("[stderr]: ", result.stderr)
    return result

if __name__ == "__main__":
    generate_health_check("web-server-01", 80)

# ============================================================
# ---- 题目2：批量执行 Shell 命令 — 模拟多服务器运维 ----
# ============================================================
# 场景：运维需要同时在多台服务器上执行相同的命令
# 写一个脚本，模拟批量执行（用本地 bash 模拟多台服务器）
#
# 要求：
# 1. 定义一个服务器列表 servers = ["web-01", "web-02", "db-01"]
# 2. 定义一组要执行的命令列表：
#    - "uptime"          → 查看运行时间
#    - "whoami"          → 当前用户
#    - "pwd"             → 当前目录
# 3. 对每台服务器，依次执行所有命令，收集输出
# 4. 用 subprocess.run() 执行，设置 timeout=10 防止卡死
# 5. 如果某条命令失败（returncode != 0），标记为 FAILED
# 6. 打印汇总报告
#
# 预期输出：
#   === 批量执行报告 ===
#   [web-01]
#     uptime  → OK (0.2s)
#     whoami  → OK (0.1s)
#     pwd     → OK (0.1s)
#   [web-02]
#     uptime  → OK (0.2s)
#     whoami  → OK (0.1s)
#     pwd     → OK (0.1s)
#   [db-01]
#     uptime  → OK (0.2s)
#     whoami  → OK (0.1s)
#     pwd     → OK (0.1s)
#   === 成功: 9/9, 失败: 0/9 ===
#
# 提示：
#   - 用 subprocess.run(["bash", "-c", cmd], ...) 执行 Shell 命令
#   - 用 time.perf_counter() 计算耗时
#   - 用 try/except subprocess.TimeoutExpired 处理超时
# ============================================================

# 请在下方写下你的答案：
import os
import time
from pathlib import Path
import subprocess

print("=== 批量执行报告 ===")
servers = ["web-01", "web-02", "db-01"]
commands = ["uptime","whoami","pwd"]

successes = 0
fails = 0

for server in servers:
    print(f"[{server}]")
    for cmd in commands:
        try:
            start = time.perf_counter()
            result = subprocess.run(
                ["bash", "-c", cmd],
                capture_output=True, encoding="utf-8",
                text=True, timeout=10
            )
            elapsed = time.perf_counter() - start
            if result.returncode == 0:
                status = "OK"
                successes +=1
            else:
                status = "FAILED"
                fails += 1
            print(f"  {cmd} -> {status} ({elapsed:.1f}s)")
        except subprocess.TimeoutExpired:
            fails += 1
            print(f"  {cmd} -> FAILED (timeout)")

total = successes + fails
print(f" === 成功: {successes}/{total}, 失败: {fails}/{total} ===")

        

# ============================================================
# ---- 题目3：用 Python 解析 Shell 脚本输出 — 日志分析 ----
# ============================================================
# 场景：Shell 脚本输出了一段格式化的日志，Python 负责解析并生成报告
# 写一个脚本，先执行 Shell 脚本收集数据，再用 Python 解析
#
# 要求：
# 1. 创建一个 Shell 脚本 collect_logs.sh，输出以下格式的模拟日志：
#    每行格式：TIMESTAMP|LEVEL|SERVICE|MESSAGE
#    示例：
#    2024-01-01 10:00:01|INFO|nginx|连接数: 150
#    2024-01-01 10:00:02|WARN|mysql|慢查询: 2.3s
#    2024-01-01 10:00:03|ERROR|redis|连接超时
#    （至少生成 10 行不同级别的日志）
# 2. 用 Python 执行该脚本，捕获 stdout
# 3. 解析输出，按级别（INFO/WARN/ERROR）分类统计
# 4. 找出所有 ERROR 行，单独列出
# 5. 打印分析报告
#
# 预期输出：
#   === 日志分析报告 ===
#   总行数: 10
#   INFO:  5 条
#   WARN:  3 条
#   ERROR: 2 条
#
#   === ERROR 日志详情 ===
#   [2024-01-01 10:00:03] redis   → 连接超时
#   [2024-01-01 10:00:08] nginx   → 端口冲突
#
# 提示：
#   - Shell 脚本用 heredoc 或 echo 输出多行日志
#   - Python 用 splitlines() 分割输出
#   - 用 split("|") 解析每行
#   - 用 defaultdict(list) 按级别分组
# ============================================================

# 请在下方写下你的答案：
from collections import defaultdict
from pathlib import Path
import subprocess
import os

log_script = Path(__file__).parent / "collect_logs.sh"
log_script.write_text("""#!/bin/bash
echo "2024-01-01 10:00:01|INFO|nginx|连接数: 150"
echo "2024-01-01 10:00:02|WARN|mysql|慢查询: 2.3s"
echo "2024-01-01 10:00:03|ERROR|redis|连接超时"
echo "2024-01-01 10:00:04|INFO|nginx|请求处理完成"
echo "2024-01-01 10:00:05|INFO|app|用户登录成功"
echo "2024-01-01 10:00:06|WARN|nginx|响应时间: 1.5s"
echo "2024-01-01 10:00:07|INFO|mysql|查询完成: 0.1s"
echo "2024-01-01 10:00:08|ERROR|nginx|端口冲突"
echo "2024-01-01 10:00:09|INFO|app|数据同步完成"
echo "2024-01-01 10:00:10|WARN|redis|内存使用率: 75%"
""", encoding="utf-8")

results = subprocess.run(["bash",str(log_script)], capture_output=True, text=True, encoding="utf-8")
lines = results.stdout.strip().splitlines()
level_groups = defaultdict(list)

for line in lines:
    if not line.strip():
        continue
    parts = line.split("|")
    if len(parts) !=4:
        continue
    timestamp, level, service, message = parts
    level_groups[level].append((timestamp, service, message))

print("=== 日志分析报告 ===")
print(f"总行数: {len(lines)}")
for level in ["INFO", "WARN", "ERROR"]:
    count = len(level_groups.get(level, []))
    print(f"{level}: {count}条")
print()
print("=== ERROR 日志详情 ===")
for timestamp, service, message in level_groups.get("ERROR", []):
    print(f"{timestamp} {service}   → {message}")