# ============================================================
# Python 云计算运维 — 第21课：Linux 文件系统与目录结构
# ============================================================
# 第三阶段：Linux 基础
# 目标：理解 Linux 目录结构，用 Python 写出 Linux 运维中常用的路径操作
# ============================================================


# ============================================================
# 知识点1：Linux 目录结构速览
# ============================================================
# /          → 根目录，一切从这里开始
# /home      → 用户家目录，/home/ori 就是你的地盘
# /etc       → 配置文件，nginx.conf、ssh_config 都在这
# /var       → 可变数据，日志文件 /var/log/、网站 /var/www/
# /tmp       → 临时文件，重启就清空
# /usr       → 用户程序，/usr/bin/python3 在这
# /opt       → 第三方软件，自己装的放这
# /root      → root 用户的家目录
# /dev       → 设备文件，硬盘是 /dev/sda，空设备是 /dev/null
# /proc      → 虚拟文件系统，进程信息 /proc/cpuinfo
#
# 记住口诀：etc 配，var 变，tmp 临，opt 选
# ============================================================


# ============================================================
# 知识点2：用 pathlib 操作 Linux 路径
# ============================================================
# 语法：
#   Path("/var/log/app.log")          → 创建路径对象
#   path.name                         → 文件名 "app.log"
#   path.stem                         → 不带后缀的文件名 "app"
#   path.parent                       → 父目录 "/var/log"
#   path.suffix                       → 后缀 ".log"
#   path.with_name("error.log")       → 替换文件名
#   path.with_suffix(".txt")          → 替换后缀
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
#
# # 模拟 Linux 路径（Windows 也能跑，Path 会自动处理分隔符）
# log_path = Path("/var/log/nginx/access.log")
# print(f"完整路径: {log_path}")
# print(f"文件名:   {log_path.name}")
# print(f"无后缀:   {log_path.stem}")
# print(f"所在目录: {log_path.parent}")
# print(f"后缀:     {log_path.suffix}")
# print(f"上级目录: {log_path.parent.parent}")
#
# # 替换文件名
# new_path = log_path.with_name("error.log")
# print(f"替换后:   {new_path}")


# ============================================================
# 知识点3：pathlib 判断文件类型
# ============================================================
# 语法：
#   path.exists()       → 是否存在
#   path.is_file()      → 是不是文件
#   path.is_dir()       → 是不是目录
#   path.is_absolute()  → 是不是绝对路径
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import os
#
# # 创建测试目录和文件
# test_dir = Path(os.path.dirname(__file__)) / "test_linux"
# test_dir.mkdir(exist_ok=True)
# (test_dir / "readme.txt").write_text("hello linux")
# (test_dir / "logs").mkdir(exist_ok=True)
#
# # 判断类型
# readme = test_dir / "readme.txt"
# logs = test_dir / "logs"
# ghost = test_dir / "ghost"
#
# print(f"readme.txt 存在: {readme.exists()}, 是文件: {readme.is_file()}")
# print(f"logs/ 存在:     {logs.exists()}, 是目录: {logs.is_dir()}")
# print(f"ghost 存在:     {ghost.exists()}")
# print(f"绝对路径:       {readme.is_absolute()}")


# ============================================================
# 知识点4：创建目录 — mkdir
# ============================================================
# 语法：
#   Path("logs").mkdir()                    → 创建单层目录（父目录必须存在）
#   Path("a/b/c").mkdir(parents=True)       → 递归创建多层目录
#   Path("logs").mkdir(exist_ok=True)       → 目录已存在也不报错
#   Path("a/b/c").mkdir(parents=True, exist_ok=True)  → 最常用写法
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import os
#
# base = Path(os.path.dirname(__file__)) / "test_dirs"
#
# # 递归创建嵌套目录（最常用：不管目录存不存在，一键创建）
# deep = base / "a" / "b" / "c"
# deep.mkdir(parents=True, exist_ok=True)
# print(f"嵌套目录已创建: {deep}")
# print(f"  存在: {deep.exists()}, 是目录: {deep.is_dir()}")
#
# # 创建单层目录
# logs = base / "logs"
# logs.mkdir(exist_ok=True)
# print(f"logs/ 已创建: {logs.exists()}")


# ============================================================
# 知识点5：拼接路径 — / 运算符
# ============================================================
# pathlib 的 Path 对象支持用 / 拼接路径，比 os.path.join 更直观
# 语法：
#   base = Path("/var")
#   full = base / "log" / "app.log"   → "/var/log/app.log"
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
#
# base = Path("/var")
# log_dir = base / "log"
# log_file = log_dir / "app.log"
# print(log_file)  # /var/log/app.log
#
# # 批量拼路径
# dirs = ["etc", "var", "tmp", "opt"]
# for d in dirs:
#     print(Path("/") / d)  # /etc, /var, /tmp, /opt


# ============================================================
# 知识点6：遍历目录 — iterdir / glob
# ============================================================
# 语法：
#   path.iterdir()            → 遍历目录下所有内容
#   path.glob("*.log")        → 按模式匹配文件
#   path.rglob("*.log")       → 递归匹配（含子目录）
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import os
#
# # 模拟 /var/log 目录结构
# var_log = Path(os.path.dirname(__file__)) / "var_log"
# var_log.mkdir(exist_ok=True)
# (var_log / "syslog").write_text("system log")
# (var_log / "auth.log").write_text("auth log")
# (var_log / "nginx").mkdir(exist_ok=True)
# (var_log / "nginx" / "access.log").write_text("access log")
# (var_log / "nginx" / "error.log").write_text("error log")
#
# print("=== 遍历目录 ===")
# for item in var_log.iterdir():
#     print(f"  {item.name} ({'目录' if item.is_dir() else '文件'})")
#
# print("\n=== 匹配 *.log ===")
# for log in var_log.glob("*.log"):
#     print(f"  {log.name}")
#
# print("\n=== 递归匹配所有 .log ===")
# for log in var_log.rglob("*.log"):
#     print(f"  {log}")


# ============================================================
# 知识点7：os.stat() 获取文件元数据
# ============================================================
# Linux 运维经常需要查看文件的大小、修改时间、权限等信息
# 语法：
#   info = os.stat(path)           → 获取文件信息
#   info.st_size                   → 文件大小（字节）
#   info.st_mtime                  → 最后修改时间（Unix 时间戳）
#   info.st_atime                  → 最后访问时间
#   info.st_ctime                  → 元数据变更时间（Linux 下）
#   info.st_mode                   → 文件权限位（如 0o100644）
#   datetime.fromtimestamp(ts)     → 时间戳转可读时间
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import os
# from datetime import datetime
#
# # 创建测试文件
# test_dir = Path(os.path.dirname(__file__)) / "test_linux"
# test_dir.mkdir(exist_ok=True)
# config_file = test_dir / "nginx.conf"
# config_file.write_text("server { listen 80; }")
#
# info = os.stat(config_file)
# print(f"文件: {config_file.name}")
# print(f"大小: {info.st_size} bytes")
# print(f"修改时间: {datetime.fromtimestamp(info.st_mtime)}")
# print(f"权限位: {oct(info.st_mode)}")
#
# # 用 Path 也可以直接拿
# print(f"大小(Path): {config_file.stat().st_size} bytes")


# ============================================================
# 知识点8：shutil 文件操作（复制、移动、删除）
# ============================================================
# Linux 运维中批量复制配置、移动日志、清理目录是家常便饭
# 语法：
#   shutil.copy(src, dst)          → 复制文件（不保留元数据）
#   shutil.copy2(src, dst)         → 复制文件（保留元数据）
#   shutil.move(src, dst)          → 移动文件/目录
#   shutil.rmtree(path)            → 递归删除目录（危险！）
#   shutil.copytree(src, dst)      → 递归复制目录
#   shutil.disk_usage(path)        → 磁盘使用情况
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import shutil
# import os
#
# test_dir = Path(os.path.dirname(__file__)) / "test_linux"
# test_dir.mkdir(exist_ok=True)
#
# # 创建源文件
# src = test_dir / "app.conf"
# src.write_text("port=8080")
#
# # 复制文件
# dst = test_dir / "app.conf.bak"
# shutil.copy(src, dst)
# print(f"备份完成: {dst.name} 存在={dst.exists()}")
#
# # 移动文件（重命名）
# moved = test_dir / "app_v2.conf"
# shutil.move(dst, moved)
# print(f"移动后: {moved.name} 存在={moved.exists()}, 原文件存在={dst.exists()}")
#
# # 磁盘使用情况
# usage = shutil.disk_usage(test_dir)
# print(f"磁盘总容量: {usage.total // (1024**3)} GB")
# print(f"已用:       {usage.used // (1024**3)} GB")
# print(f"可用:       {usage.free // (1024**3)} GB")


# ============================================================
# ---- 题目1：Linux 日志文件巡检 ----
# ============================================================
# 场景：运维经常要检查 /var/log 下的日志文件，你写一个脚本
# 模拟 Linux 日志目录，完成以下操作：
#
# 要求：
# 1. 创建目录 var_log/{nginx, mysql, system}
# 2. 创建以下 6 个文件：
#    var_log/nginx/access.log  → 内容 "GET / 200"
#    var_log/nginx/error.log   → 内容 "500 error"
#    var_log/mysql/slow.log    → 空文件
#    var_log/mysql/error.log   → 空文件
#    var_log/system/syslog     → 空文件
#    var_log/system/auth.log   → 空文件
# 3. 用 pathlib 遍历所有 .log 文件
# 4. 打印每个日志文件的路径和大小
# 5. 找出所有名为 "error.log" 的文件
# 6. 统计共有多少个日志文件
#
# 预期输出：
#   var_log/nginx/access.log (20 bytes)
#   var_log/nginx/error.log (9 bytes)
#   var_log/mysql/slow.log (0 bytes)
#   var_log/mysql/error.log (0 bytes)
#   var_log/system/sys.log (0 bytes)
#   var_log/system/auth.log (0 bytes)
#   ---
#   共 6 个日志文件
#   包含 "error.log" 的文件:
#     var_log/nginx/error.log
#     var_log/mysql/error.log
#
# 提示：
#   - 用 Path.mkdir(parents=True, exist_ok=True) 创建嵌套目录
#   - 用 Path.write_text() 创建文件并写入内容
#   - 用 rglob("*.log") 递归查找所有 .log 文件
#   - 用 stat().st_size 获取文件大小
# ============================================================

# 请在下方写下你的答案：
from pathlib import Path
import os

errors = []
count = 0
base = Path(os.path.dirname(__file__)) / "var_log"
dirs = ["nginx","mysql","system"]
for d in dirs:
    (base / d).mkdir(parents=True, exist_ok=True)

(base / "nginx" / "access.log").write_text("GET / 200")
(base / "nginx" / "error.log").write_text("500 error")
(base / "mysql" / "slow.log").write_text("")
(base / "mysql" / "error.log").write_text("")
(base / "system" / "syslog.log").write_text("")
(base / "system" / "auth.log").write_text("")

for log in base.rglob("*.log"):
    print(f"{log} ({os.stat(log).st_size} bytes)")
    count += 1
    if log.name == "error.log":
        errors.append(log)

print("---")
print(f"共 {count} 个日志文件")
print(f"包含 \"error.log\" 的文件:")
for e in errors:
    print(f"  {e}")

# ============================================================
# ---- 题目2：配置文件备份与清理 ----
# ============================================================
# 场景：运维改配置前要备份，还要定期清理过期备份
# 模拟 /etc/nginx/ 目录，完成以下操作：
#
# 要求：
# 1. 创建模拟目录结构：
#    etc_nginx/
#    ├── nginx.conf        (内容: "worker_processes 4;")
#    ├── sites-enabled/
#    │   └── default.conf  (内容: "listen 80;")
#    └── backups/          (空目录，放备份)
# 2. 用 shutil.copy2() 把所有 .conf 文件备份到 backups/ 目录
#    备份文件命名为「原文件名_日期.conf」，如 nginx.conf_20260825.conf
# 3. 用 os.stat() 打印每个备份文件的大小和修改时间
# 4. 用 shutil.disk_usage() 打印 backups/ 目录所在磁盘的可用空间
# 5. 用 shutil.rmtree() 清理整个 etc_nginx/ 目录（模拟任务结束清理）
#
# 预期输出：
#   备份: nginx.conf -> nginx.conf_20260825.conf
#   备份: default.conf -> default.conf_20260825.conf
#   ---
#   备份文件信息:
#     nginx.conf_20260825.conf: 22 bytes, 修改于 2026-08-25 10:30:00
#     default.conf_20260825.conf: 11 bytes, 修改于 2026-08-25 10:30:00
#   磁盘可用空间: XXX GB
#   ---
#   已清理 etc_nginx/ 目录
#
# 提示：
#   - 用 Path.mkdir(parents=True, exist_ok=True) 创建嵌套目录
#   - 用 shutil.copy2(src, dst) 保留文件的时间戳
#   - 用 datetime.now().strftime("%Y%m%d") 获取日期字符串
#   - 用 shutil.disk_usage(path) 查磁盘空间
#   - 用 shutil.rmtree(path) 删除目录（保留到题目最后再做）
# ============================================================

# 请在下方写下你的答案：
import os
from pathlib import Path
from datetime import datetime
import shutil

base = Path(os.path.dirname(__file__)) / "etc_nginx"
dirs = ["sites-enabled", "backups"]
for d in dirs:
    (base / d).mkdir(parents=True, exist_ok=True)
(base / "nginx.conf").write_text("worker_processes 4;")
(base / "sites-enabled" / "default.conf").write_text("listen 80;")

date_str = datetime.now().strftime("%Y%m%d")
for conf in base.rglob(".conf"):
    if conf.parent.name == "backups":
        continue
    backup_name = f"{conf.name}{date_str}{conf.suffix}"
    backup_path = base / "backups" / backup_name
    shutil.copy2(conf, backup_path)
    print(f"备份: {conf.name} -> {backup_name}")

print("---")
print("备份文件信息:")
for backup in sorted((base / "backups").iterdir()):
    info = os.stat(backup)
    mtime = datetime.fromtimestamp(info.st_mtime)
    print(f"  {backup.name}: {info.st_size} bytes, 修改于 {mtime}")

usage = shutil.disk_usage(base / "backups")
print(f"磁盘可用空间: {usage.free // (1024**3) } GB")

print("---")
shutil.rmtree(base)
print(f" 已清理 etc_nginx/ 目录")