# ============================================================
# Python 云计算运维 — 第25课：文本处理三剑客 grep / awk / sed 🎯
# ============================================================
# 第三阶段：Linux 基础
# 目标：掌握 grep/awk/sed 核心用法，用 Python 编排文本处理流水线
# ============================================================
# 注意：本机有 bash (Cygwin)，grep/awk/sed 均可使用
# ============================================================


# ============================================================
# 知识点1：grep — 文本搜索与过滤
# ============================================================
# grep 在三剑客中排第一，负责从文本中筛选匹配行
#
# 基本语法：
#   grep [选项] "模式" 文件...
#
# 常用选项：
#   -i      → 忽略大小写
#   -v      → 反向匹配（排除匹配行）
#   -r      → 递归搜索目录
#   -l      → 只显示文件名（不显示匹配内容）
#   -c      → 计数匹配行
#   -n      → 显示行号
#   -w      → 全词匹配
#   -E      → 扩展正则（支持 | + ?）
#   -A N    → 显示匹配行后 N 行 (After)
#   -B N    → 显示匹配行前 N 行 (Before)
#
# 正则模式：
#   grep "ERROR"           → 普通字符串匹配
#   grep "^2024"           → 以 2024 开头
#   grep "\.py$"           → 以 .py 结尾
#   grep -E "ERROR|WARN"   → 匹配 ERROR 或 WARN
#   grep "[0-9]{3}"        → 匹配3位数字
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# log_file = Path(__file__).parent / "sample_logs" / "app.log"
# print(f"文件: {log_file}")
#
# result = subprocess.run(
#     ["grep", "-n", "ERROR", str(log_file)],
#     capture_output=True, text=True
# )
# print("=== grep -n ERROR ===")
# print(result.stdout)
#
# result = subprocess.run(
#     ["grep", "-c", "-E", "ERROR|WARN", str(log_file)],
#     capture_output=True, text=True
# )
# print(f"ERROR+WARN 合计: {result.stdout.strip()} 行")


# ============================================================
# 知识点2：awk — 列提取与数据处理
# ============================================================
# awk 是文本处理利器，擅长按列操作和条件过滤
#
# 基本语法：
#   awk [选项] '条件 {动作}' 文件
#
# 内置变量：
#   $0      → 整行内容
#   $1, $2  → 第1列、第2列（默认空格/Tab分隔）
#   NF      → 当前行的列数 (Number of Fields)
#   NR      → 当前行号 (Number of Record)
#   FS      → 输入字段分隔符 (Field Separator)，默认空格
#   OFS     → 输出字段分隔符
#
# 常用模式：
#   awk '{print $1, $3}'            → 打印第1和第3列
#   awk -F':' '{print $1}'          → 用 : 分隔，打印第1列
#   awk '/ERROR/ {print $0}'        → 只打印含 ERROR 的行
#   awk '$3 > 100 {print}'          → 第3列大于100才打印
#   awk '{sum+=$2} END{print sum}'  → 累加第2列，最后打印总和
#   awk 'BEGIN{print "start"} ... END{print "end"}'  → BEGIN/END 块
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# log_file = Path(__file__).parent / "sample_logs" / "app.log"
#
# result = subprocess.run(
#     ["awk", '{print $1, $2, $3}', str(log_file)],
#     capture_output=True, text=True
# )
# print("=== awk 提取前3列 ===")
# print(result.stdout[:300])
#
# result = subprocess.run(
#     ["awk", '/ERROR/ {count++} END {print "ERROR行数:", count}', str(log_file)],
#     capture_output=True, text=True
# )
# print(result.stdout)


# ============================================================
# 知识点3：sed — 流编辑器（替换/删除/插入）
# ============================================================
# sed 按行处理文本，可以做替换、删除、插入、提取
#
# 基本语法：
#   sed [选项] '动作' 文件
#
# 常用动作：
#   s/旧/新/g        → 替换（s=substitute, g=全局）
#   /模式/d          → 删除匹配行
#   /模式/p          → 打印匹配行（常与 -n 联用）
#   Ns/旧/新/g       → 只替换第 N 行
#   N,Md             → 删除第 N 到 M 行
#
# 常用选项：
#   -n      → 静默模式，只输出处理过的行
#   -i      → 原地修改文件（危险！建议先备份）
#   -i.bak  → 原地修改，备份为 .bak
#   -e      → 多个动作
#   -r / -E → 扩展正则
#
# 替换中的特殊字符：
#   &       → 代表匹配到的整个字符串
#   \1 \2   → 分组引用
#   /       → 分隔符可用 # @ | 代替，避免转义
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# log_file = Path(__file__).parent / "sample_logs" / "app.log"
#
# result = subprocess.run(
#     ["sed", "-n", "1,5p", str(log_file)],
#     capture_output=True, text=True
# )
# print("=== sed 提取第1~5行 ===")
# print(result.stdout)
#
# result = subprocess.run(
#     ["sed", "s/ERROR/CRITICAL/g", str(log_file)],
#     capture_output=True, text=True
# )
# print("=== sed 替换 ERROR→CRITICAL (前3行) ===")
# for line in result.stdout.splitlines()[:3]:
#     print(line)


# ============================================================
# 知识点4：管道组合 — grep | awk | sed
# ============================================================
# 三剑客通过管道 | 组合，形成强大的文本处理流水线
#
# 常见组合：
#   grep "ERROR" | awk '{print $1, $3}'           → 先筛选再提取列
#   awk '{print $1}' | sort | uniq -c | sort -rn  → 统计频率排序
#   grep -v "^#" | sed '/^$/d'                     → 去掉注释和空行
#   grep "ERROR" | awk -F'|' '{print $NF}' | sort -u  → 提取唯一值
#
# 在 Python 中模拟管道的两种方式：
#   1. 多次 subprocess.run()，中间结果存为变量
#   2. 用 shell=True 执行完整管道命令（不推荐，安全风险）
#   3. 用 Python 字符串处理替代（推荐）
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# upload_csv = Path(__file__).parent / "data.csv"
#
# # 用 grep+awk 提取特定列
# result = subprocess.run(
#     ["grep", "-v", "^#", str(upload_csv)],
#     capture_output=True, text=True
# )
# filtered = result.stdout
#
# result2 = subprocess.run(
#     ["awk", "-F,", '{print $1, $3}'],
#     input=filtered, capture_output=True, text=True
# )
# print("=== 管道模拟: grep | awk ===")
# print(result2.stdout)


# ============================================================
# 知识点5：Python 调用三剑客 — 完整流程
# ============================================================
# 运维场景中 Python 负责：
#   1. 遍历文件列表、收集文件路径
#   2. 为每个文件构造 grep/awk/sed 命令
#   3. 执行命令并收集结果
#   4. 汇总、格式化、生成报告
#
# 注意事项：
#   - 文件路径含空格时，用列表形式传参（不要用 shell=True）
#   - 大量文件时用 subprocess.run() 而非 Popen
#   - 检查 returncode，非0 时 stderr 可能有错误信息
#   - Windows 上 grep/awk/sed 来自 Cygwin/Git Bash，路径用正斜杠
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import subprocess
#
# log_dir = Path(__file__).parent / "sample_logs"
# keyword = "ERROR"
# total = 0
#
# for log_file in sorted(log_dir.glob("*.log")):
#     result = subprocess.run(
#         ["grep", "-c", keyword, str(log_file)],
#         capture_output=True, text=True
#     )
#     count = int(result.stdout.strip() or 0)
#     total += count
#     print(f"  {log_file.name}: {count} 条 {keyword}")
#
# print(f"总计: {total} 条 {keyword}")


# ============================================================
# 知识点6：Python 原生替代方案
# ============================================================
# 当无法使用 grep/awk/sed 时（如纯 Windows 环境），Python 自带能力可替代
#
# grep 替代：
#   re.search(pattern, line)         → 正则匹配
#   [line for line in f if "ERROR" in line]  → 简单筛选
#
# awk 替代：
#   line.split()                     → 按空格分割
#   line.split(",")                  → 按逗号分割
#   csv 模块                         → 专业 CSV 解析
#
# sed 替代：
#   re.sub(pattern, repl, text)      → 正则替换
#   line.replace(old, new)           → 简单替换
#   unicodecsv / csv.reader          → 处理复杂 CSV
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import re
# from pathlib import Path
#
# log_file = Path(__file__).parent / "sample_logs" / "app.log"
# text = log_file.read_text(encoding="utf-8")
#
# # Python 版 grep -c ERROR
# error_count = sum(1 for line in text.splitlines() if "ERROR" in line)
# print(f"grep -c ERROR  → Python版: {error_count} 行")
#
# # Python 版 awk '{print $1, $3}'
# print("\nawk {print $1, $3} → Python版:")
# for line in text.splitlines()[:5]:
#     cols = line.split()
#     if len(cols) >= 3:
#         print(f"  {cols[0]} {cols[2]}")
#
# # Python 版 sed 's/ERROR/CRITICAL/g'
# replaced = re.sub(r"ERROR", "CRITICAL", text)
# print("\nsed s/ERROR/CRITICAL/g → Python版 (前3行):")
# for line in replaced.splitlines()[:3]:
#     print(f"  {line}")


# ============================================================
# ---- 题目1：日志文件搜索器 — grep 实战 ----
# ============================================================
# 场景：运维收到告警，需要在多个日志文件中搜索关键字定位问题
# 写一个 Python 脚本，遍历 sample_logs 目录下所有 .log 文件，
# 用 grep 搜索指定关键字，返回带行号和上下文的匹配结果
#
# 要求：
# 1. 定义一个函数 search_logs(keyword, context_lines=1)
# 2. 遍历 sample_logs/ 下所有 .log 文件
# 3. 对每个文件执行 grep -n -B N -A N 搜索关键字
# 4. 把匹配结果按文件名分组，格式化输出
# 5. 统计总匹配行数和涉及文件数
#
# 预期输出（grep -n -B 1 -A 1 格式，- 开头=上下文，: 开头=匹配行）：
#   === 日志搜索结果: "timeout" ===
#   [app.log]
#     2-2024-01-15 09:05:13 INFO ...
#     3:2024-01-15 10:23:45 WARN nginx upstream timeout (5.0s)
#     4-2024-01-15 10:23:46 INFO ...
#     --
#     9-2024-01-15 14:30:03 INFO ...
#     10:2024-01-15 14:30:04 ERROR redis connection timeout
#     11-2024-03-20 09:15:00 INFO ...
#   [system.log]
#     3-2024-01-15 10:15:30 WARN ...
#     4:2024-03-15 09:30:00 ERROR service timeout after 30s
#     5-2024-03-15 09:30:01 INFO ...
#   === 共 2 个文件, 2 处匹配 ===
#
# 提示：
#   - 用 Path.glob("*.log") 遍历文件
#   - grep -n -B 1 -A 1 "keyword" file 可获取上下文
#   - 用 defaultdict(list) 按文件名分组结果
# ============================================================

# 请在下方写下你的答案：
import subprocess
from collections import defaultdict
from pathlib import Path

def search_logs(keyword, context_lines=1):
    logs_dir = Path(__file__).parent / "sample_logs"
    groups = defaultdict(list)       # 按文件名分组存储匹配行
    total_match = 0

    for log in sorted(logs_dir.glob("*.log")):
        # grep -n 显示行号, -B 前N行, -A 后N行
        result = subprocess.run(
                ["grep", "-n", f"-B{context_lines}", f"-A{context_lines}", keyword, str(log)],
                capture_output=True, encoding="utf-8", text=True
                )
        if result.stdout.strip():
            groups[log.name] = result.stdout.strip().splitlines()
            total_match += 1

    print(f'=== 日志搜索结果: "{keyword}" ===')
    for fname, lines in groups.items():
        print(f"[{fname}]")
        for line in lines:
            print(f"  {line}")
    print(f"=== 共 {len(groups)} 个文件, {total_match} 处匹配 ===")


if __name__ == "__main__":
    search_logs("timeout")
    search_logs("ERROR", context_lines=2)

# ============================================================
# ---- 题目2：日志统计分析 — awk 实战 ----
# ============================================================
# 场景：运维需要从 Nginx 日志中提取统计信息
# 写一个 Python 脚本，用 awk 解析 access.log 并生成统计报告
#
# 要求：
# 1. 定义函数 analyze_access_log(log_path)，解析 Nginx 格式日志
#    Nginx 日志格式示例：
#    192.168.1.1 - - [15/Jan/2024:10:23:45 +0800] "GET /api/users HTTP/1.1" 200 1234
# 2. 用 awk 统计以下信息：
#    - 总请求数（行数）
#    - 各 HTTP 状态码的分布（200/404/500 等）
#    - 请求量 Top 3 的 IP 地址
#    - 平均响应体大小（$NF 最后一列，假设是 body_bytes_sent）
# 3. 打印格式化的统计报告
#
# 预期输出：
#   === Nginx 访问日志分析 ===
#   总请求数: 20
#   状态码分布:
#     200: 15
#     404: 3
#     500: 2
#   Top 3 IP:
#     192.168.1.100: 8 次
#     192.168.1.101: 5 次
#     10.0.0.50: 3 次
#   平均响应大小: 2345.6 bytes
#
# 提示：
#   - awk '{print $9}' 获取状态码（第9列）
#   - awk '{print $1}' 获取 IP
#   - awk '{sum+=$NF; count++} END{print sum/count}' 计算平均值
#   - 用 sort | uniq -c | sort -rn | head -3 获取 Top 3
#   - 按管道模式：先 grep/awk 过滤 → 再 sort/uniq 统计
# ============================================================

# 请在下方写下你的答案：
import subprocess
from pathlib import Path
from collections import Counter

def analyze_access_log(log_path):
    log_path = Path(log_path)
    total = subprocess.run(
        ["awk", "END{print NR}", str(log_path)],
        capture_output=True,text=True,encoding="utf-8"
        )
    totle_reqs = int(total.stdout.strip())

    status = subprocess.run(
        ["awk", "{print $9}", str(log_path)],
        capture_output=True,text=True,encoding="utf-8"
        )
    code_dist = Counter(status.stdout.strip().splitlines())

    ip_result = subprocess.run(
        ["awk", "{print $1}", str(log_path)],
        capture_output=True, text=True, encoding="utf-8"
        )
    ip_dist = Counter(ip_result.stdout.strip().splitlines())

    avg_result = subprocess.run(
        ["awk", "{sum+=$NF; count++} END{print sum/count}", str(log_path)],
        capture_output=True, text=True
        )
    avg_size = avg_result.stdout.strip()
    print("=== Nginx 访问日志分析 ===")
    print(f"总请求数: {totle_reqs}")
    print("状态码分布:")
    for code, count in sorted(code_dist.items()):
        print(f"  {code}: {count}")
    print("Top 3 IP:")
    for ip, count in ip_dist.most_common(3):
        print(f"  {ip}: {count} 次")
    print(f"平均响应大小: {avg_size} bytes")

if __name__ == "__main__":
    log_path = Path(__file__).parent / "sample_logs" / "access.log"
    analyze_access_log(str(log_path))


# ============================================================
# ---- 题目3：配置文件批量修改 — sed 实战 ----
# ============================================================
# 场景：运维需要批量修改多台服务器的配置文件
# 写一个 Python 脚本，用 sed 修改配置文件中的指定项
#
# 要求：
# 1. 定义函数 update_config(config_path, changes)
#    changes 是字典，格式如 {"host": "10.0.0.1", "port": "8080"}
# 2. 配置文件格式为 key = value（如 app.conf）
# 3. 用 sed 的 s 命令替换对应 key 的值
# 4. 修改前先创建备份文件（.bak）
# 5. 修改后打印变更前后对比
#
# 示例 changes：
#   changes = {
#       "host": "192.168.1.100",
#       "port": "9090",
#       "max_connections": "200"
#   }
#
# 预期输出：
#   === 配置变更: app.conf ===
#   [host]      localhost → 192.168.1.100
#   [port]      3306 → 9090
#   [max_connections]  100 → 200
#   === 备份已保存: app.conf.bak ===
#
# 提示：
#   - sed -i.bak 's/^host = .*/host = 新值/' config.conf
#   - 用 sed -n '/^key /p' 提取修改前的值
#   - 对每个 changes 项分别执行 sed -i
#   - 注意 sed 正则中 . * 等需要转义
# ============================================================

# 请在下方写下你的答案：
import subprocess
from pathlib import Path
import shutil

def update_config(config_path, changes):
    config_path = Path(config_path)
    bak_path = config_path.with_suffix(config_path.suffix + ".bak")
    shutil.copy(config_path, bak_path)       # 先备份

    print(f"=== 配置变更: {config_path.name} ===")
    for key, new_val in changes.items():
        # 提取旧值
        old = subprocess.run(
            ["sed", "-n", f"s/^{key} = //p", str(config_path)],
            capture_output=True, text=True, encoding="utf-8"
        )
        old_val = old.stdout.strip()

        # 原地替换
        subprocess.run(
            ["sed", "-i", f"s/^{key} = .*/{key} = {new_val}/", str(config_path)],
            capture_output=True, text=True
        )
        print(f"  [{key}]      {old_val} → {new_val}")
    print(f"=== 备份已保存: {bak_path.name} ===")


if __name__ == "__main__":
    config_path = Path(__file__).parent / "app.conf"
    changes = {
        "host": "192.168.1.100",
        "port": "9090",
        "max_connections": "200"
    }
    update_config(str(config_path), changes)


# ============================================================
# ---- 题目4（拔高 🎯）：综合日志分析流水线 ----
# ============================================================
# 场景：运维需要从混合日志中提取 ERROR 信息，按服务分组，统计时间段分布
# 这是 HCIE 级别的综合题，需要组合 grep / awk / sed 完成
#
# 要求：
# 1. 定义函数 analyze_errors(log_path)
# 2. 用 grep 提取所有 ERROR 行
# 3. 用 awk 按服务名称（第4列）分组统计
# 4. 用 sed 提取时间戳中的小时部分
# 5. 生成按小时分布的 ERROR 数量统计
# 6. 打印完整分析报告
#
# 日志格式（sample_logs/app.log 中）：
#   2024-01-15 10:23:45 ERROR nginx connection refused
#   列1=日期  列2=时间  列3=级别  列4=服务  列5+=消息
#
# 预期输出：
#   === ERROR 分析报告 ===
#   总 ERROR 数: 7
#   按服务分布:
#     nginx:  2 次
#     redis:  2 次
#     mysql:  1 次
#     db:     1 次
#     app:    1 次
#   按小时分布:
#     10:00~10:59: 1 次
#     14:00~14:59: 4 次
#     22:00~22:59: 2 次
#
# 提示：
#   - grep "ERROR" 提取行，再 awk 处理
#   - awk '{print $4}' 获取服务名（第4列）
#   - awk '{print $2}' 获取时间，用 cut -d: -f1 取小时
#   - 或全用 Python 处理：split() 后按索引取值
# ============================================================

# 请在下方写下你的答案：
import subprocess
from pathlib import Path
from collections import Counter

def analyze_errors(log_path):
    log_path = Path(log_path)

    # grep 提取所有 ERROR 行
    result = subprocess.run(
        ["grep", "ERROR", str(log_path)],
        capture_output=True, text=True, encoding="utf-8"
    )
    error_lines = result.stdout.strip().splitlines()
    total_errors = len(error_lines)

    if total_errors == 0:
        print("=== ERROR 分析报告 ===")
        print("没有 ERROR 日志")
        return

    # awk 提取第4列（服务名）
    awk_svc = subprocess.run(
        ["awk", "{print $4}"],
        input=result.stdout, capture_output=True, text=True
    )
    svc_dist = Counter(awk_svc.stdout.strip().splitlines())

    # awk 提取第2列（时间），再 cut 取小时
    awk_time = subprocess.run(
        ["awk", "{print $2}"],
        input=result.stdout, capture_output=True, text=True
    )
    hour_dist = Counter()
    for t in awk_time.stdout.strip().splitlines():
        hour = t.split(":")[0]
        hour_dist[hour] += 1

    print("=== ERROR 分析报告 ===")
    print(f"总 ERROR 数: {total_errors}")
    print("按服务分布:")
    for svc, cnt in svc_dist.most_common():
        print(f"  {svc}:  {cnt} 次")
    print("按小时分布:")
    for h in sorted(hour_dist):
        print(f"  {h}:00~{h}:59: {hour_dist[h]} 次")


if __name__ == "__main__":
    log_path = Path(__file__).parent / "sample_logs" / "app.log"
    analyze_errors(str(log_path))