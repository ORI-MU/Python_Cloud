# ============================================================
# Python 云计算运维 — 第22课：用户与权限管理 chmod / chown
# ============================================================
# 第三阶段：Linux 基础
# 目标：理解 Linux 文件权限体系，用 Python 读写权限位
# ============================================================
# 注意：Windows 上 chmod 只有只读位有效，完整权限操作需在 Linux 上验证
# ============================================================


# ============================================================
# 知识点1：Linux 权限位速览
# ============================================================
# 每个文件有三组权限：用户(u) / 组(g) / 其他人(o)
# 每组三个位：读(r=4) / 写(w=2) / 执行(x=1)
#
# 数字表示法：
#   7 = 4+2+1 = rwx    → 读写执行
#   6 = 4+2   = rw-    → 读写
#   5 = 4+1   = r-x    → 读执行
#   4 = 4     = r--    → 只读
#   0 = 0     = ---    → 无权限
#
# 常见组合：
#   755 = rwxr-xr-x  → 目录/可执行文件
#   644 = rw-r--r--  → 普通文件
#   600 = rw-------  → 私密文件（只有主人能读写）
#   777 = rwxrwxrwx  → 所有人全权限（危险！）
#
# 记住口诀：读4写2执行1，用户组人三组拼
# ============================================================


# ============================================================
# 知识点2：Linux 用户/组概念
# ============================================================
# 每个文件有一个 owner(uid) 和一个 group(gid)
# /etc/passwd  → 用户列表
# /etc/group   → 组列表
# root 用户 uid=0，拥有最高权限
#

# 用 Python 获取当前用户信息：
#   os.getuid()       → 当前用户 uid（Linux only）
#   os.getgid()       → 当前组 gid（Linux only）
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import os
#
# # Windows 上没有 uid/gid 概念，以下代码仅在 Linux 上有效
# try:
#     print(f"当前 uid: {os.getuid()}")
#     print(f"当前 gid: {os.getgid()}")
# except AttributeError:
#     print("Windows 不支持 uid/gid，请在 Linux 上运行此示例")


# ============================================================
# 知识点3：os.stat() 查看权限位
# ============================================================
# 语法：
#   info = os.stat(path)
#   info.st_mode          → 完整模式位（含文件类型）
#   oct(info.st_mode)     → 八进制显示（如 '0o100644'）
#   info.st_uid           → 所有者 uid（Linux only）
#   info.st_gid           → 所属组 gid（Linux only）
#
# 权限位 = st_mode 的低 9 位（后三位八进制）
#   0o100644 → 权限 = 644 → rw-r--r--
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import os
# import stat
#
# test_dir = Path(os.path.dirname(__file__)) / "test_perm"
# test_dir.mkdir(exist_ok=True)
# f = test_dir / "secret.txt"
# f.write_text("top secret")
#
# info = os.stat(f)
# mode = info.st_mode
# perm = mode & 0o777  # 只取低 9 位权限
# print(f"文件: {f.name}")
# print(f"完整 mode: {oct(mode)}")       # 如 0o100666
# print(f"权限位:   {oct(perm)}")        # 0o666
# print(f"权限符号: {stat.filemode(mode)}")  # -rw-rw-rw-


# ============================================================
# 知识点4：os.chmod() 修改权限
# ============================================================
# 语法：
#   os.chmod(path, 0o644)       → 设为 rw-r--r--
#   os.chmod(path, 0o755)       → 设为 rwxr-xr-x
#   os.chmod(path, 0o600)       → 设为 rw-------（私密文件）
#
# 注意：Windows 上 chmod 只能改只读位，Linux 上完整生效
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# from pathlib import Path
# import os
# import stat
#
# test_dir = Path(os.path.dirname(__file__)) / "test_perm"
# test_dir.mkdir(exist_ok=True)
# script = test_dir / "deploy.sh"
# script.write_text("#!/bin/bash\necho 'deploying...'")
#
# # 查看初始权限
# print(f"初始权限: {stat.filemode(os.stat(script).st_mode)}")
#
# # 设为可执行
# os.chmod(script, 0o755)
# print(f"chmod 755: {stat.filemode(os.stat(script).st_mode)}")
#
# # 设为私密
# os.chmod(script, 0o600)
# print(f"chmod 600: {stat.filemode(os.stat(script).st_mode)}")


# ============================================================
# 知识点5：权限位解析 — 八进制 ↔ 符号
# ============================================================
# 用 stat 模块解析和转换权限
# 语法：
#   stat.S_IRUSR  → 用户读 (0o400)
#   stat.S_IWUSR  → 用户写 (0o200)
#   stat.S_IXUSR  → 用户执行 (0o100)
#   stat.S_IRGRP  → 组读 (0o040)
#   stat.S_IROTH  → 其他人读 (0o004)
#   stat.filemode(mode) → 数字转符号 "-rwxr-xr-x"
# ============================================================

# ==== 运行示例（取消注释即可运行）====
# import os
# import stat
# from pathlib import Path
#
# test_dir = Path(os.path.dirname(__file__)) / "test_perm"
# test_dir.mkdir(exist_ok=True)
# f = test_dir / "test.txt"
# f.write_text("hello")
#
# mode = os.stat(f).st_mode
# print(f"符号: {stat.filemode(mode)}")
#
# # 逐位检查
# checks = [
#     ("用户读", stat.S_IRUSR),
#     ("用户写", stat.S_IWUSR),
#     ("用户执行", stat.S_IXUSR),
#     ("组读", stat.S_IRGRP),
#     ("组写", stat.S_IWGRP),
#     ("其他人读", stat.S_IROTH),
# ]
# for name, flag in checks:
#     print(f"  {name}: {'✅' if mode & flag else '❌'}")


# ============================================================
# 知识点6：os.chown() 修改所有者（Linux only）
# ============================================================
# 语法：
#   os.chown(path, uid, gid)    → 修改文件所有者
#   只改所有者：os.chown(path, uid, -1)
#   只改组：    os.chown(path, -1, gid)
#
# 需要 root 权限才能把文件给别人
# ============================================================

# ==== 运行示例（取消注释即可运行，仅 Linux）====
# import os
# from pathlib import Path
#
# test_dir = Path(os.path.dirname(__file__)) / "test_perm"
# f = test_dir / "owned_by_root.txt"
# f.write_text("root's file")
#
# try:
#     # 查看当前所有者
#     info = os.stat(f)
#     print(f"uid={info.st_uid}, gid={info.st_gid}")
#
#     # 尝试改所有者（需要 root 权限）
#     # os.chown(f, 0, -1)  # 改为 root
#     # print("所有者已改为 root")
# except AttributeError:
#     print("Windows 不支持 chown，请切换到 Linux 运行")


# ============================================================
# ---- 题目1：文件权限检查器 ----
# ============================================================
# 场景：运维要检查服务器上关键文件的权限是否合规
# 写一个脚本，批量检查文件权限并报告风险
#
# 要求：
# 1. 创建模拟目录 test_perm/，包含以下文件：
#    test_perm/secret.key    → 内容 "my-secret-key"（预期权限 600）
#    test_perm/deploy.sh     → 内容 "#!/bin/bash"（预期权限 755）
#    test_perm/app.conf      → 内容 "port=8080"（预期权限 644）
# 2. 用 os.chmod() 设置每个文件的权限（模拟真实场景）
# 3. 对每个文件，读取实际权限并与预期对比
# 4. 打印权限合规报告：
#    - 如果实际 = 预期 → ✅
#    - 如果实际 ≠ 预期 → ❌ 报告风险（如：权限过大）
#
# 预期输出：
#   检查 secret.key: 预期 600, 实际 600 ✅
#   检查 deploy.sh:  预期 755, 实际 755 ✅
#   检查 app.conf:   预期 644, 实际 644 ✅
#   所有文件权限合规！
#
# 提示：
#   - 用 os.chmod(path, 0o600) 设置权限（注意 0o 前缀）
#   - 用 os.stat(path).st_mode & 0o777 获取权限位
#   - 用 oct() 转成八进制字符串比较
# ============================================================

# 请在下方写下你的答案：
from pathlib import Path
import os

base = Path(os.path.dirname(__file__)) / "test_perm"
base.mkdir(exist_ok=True)
(base / "secret.key").write_text("my-secret-key")
(base / "deploy.sh").write_text("#!/bin/bash")
(base / "app.conf").write_text("port=8080")

permsdand = {"secret.key": 0o600, 
             "deploy.sh": 0o755, 
             "app.conf": 0o644
             }
os.chmod(base / "secret.key", 0o600)
os.chmod(base / "deploy.sh", 0o755)
os.chmod(base / "app.conf", 0o644)

check = 0
true = 0
false = []
print("预期输出：")
for f in base.iterdir():
    check += 1
    if f.is_file():
        actural = os.stat(f).st_mode & 0o777
        excepted = permsdand[f.name]
        ok = actural == excepted
        if ok:
            true += 1
        else:
            false.append(f)
        print(f"   检查 {f.name}: 预期 {oct(permsdand[f.name])}, 实际 {oct(actural)} {'✅' if ok else '❌'}")

if true == check:
    print("   所有文件权限合规！")
else:
    print(f"   共{check}个文件, {true}个文件合规,不合规文件为{false}")

# ============================================================
# ---- 题目2：批量权限加固脚本 ----
# ============================================================
# 场景：运维发现一批文件权限过大，需要批量收紧
# 写一个脚本，扫描目录中所有文件，自动收紧权限
#
# 要求：
# 1. 创建模拟目录 test_perm2/，包含以下文件：
#    test_perm2/public/readme.txt   → 内容 "public info"（设为 777，模拟错误）
#    test_perm2/public/style.css    → 内容 "body {}"（设为 777，模拟错误）
#    test_perm2/private/.env        → 内容 "DB_PASS=123"（设为 777，模拟错误）
#    test_perm2/private/token.key   → 内容 "abcdef"（设为 777，模拟错误）
# 2. 写一个函数 classify(path)，根据文件类型返回安全权限：
#    - 以 .sh 结尾 → 755
#    - 以 .key 或 .env 结尾 → 600
#    - 其他文件 → 644
# 3. 遍历所有文件，检查权限，如果比安全权限大则收紧
# 4. 打印修复日志
#
# 预期输出：
#   修复 public/readme.txt: 777 → 644
#   修复 public/style.css:  777 → 644
#   修复 private/.env:      777 → 600
#   修复 private/token.key: 777 → 600
#   ---
#   共修复 4 个文件
#
# 提示：
#   - 用 rglob("*") 遍历所有文件（跳过目录）
#   - 定义安全权限字典：{".sh": 0o755, ".key": 0o600, ".env": 0o600}
#   - 用 path.suffix 获取后缀
#   - 比较时用 os.stat(path).st_mode & 0o777
# ============================================================

# 请在下方写下你的答案：
import os
from pathlib import Path

permsdand = {".sh": 0o755, ".key": 0o600, ".env": 0o600}
base = Path(os.path.dirname(__file__)) / "test_perm2"
dirs = ["public", "private"]
for d in dirs:
    (base / d).mkdir(parents=True, exist_ok=True)
(base / "public" / "readme.txt").write_text("public info")
os.chmod(base / "public" / "readme.txt", 0o777)

(base / "public" / "style.css").write_text("body {}")
os.chmod(base / "public" / "style.css", 0o777)

(base / "private" / ".env").write_text("DB_PASS=123")
os.chmod(base / "private" / ".env", 0o777)

(base / "private" / "token.key").write_text("abcdef")
os.chmod(base / "private" / "token.key", 0o777)


print("预期输出：")
def classify(path):
    count = 0
    for f in path.rglob("*"):
        if not f.is_file():
            continue
        safe_perm = permsdand.get(f.suffix, 0o644)
        actual = os.stat(f).st_mode & 0o777
        if actual > safe_perm:
            os.chmod(f, safe_perm)
            print(f"   修复 {f.relative_to(path)}: {oct(actual)} → {oct(safe_perm)}")
            count += 1
    print(f"   ---")
    print(f"   共修复 {count} 个文件")

classify(base)