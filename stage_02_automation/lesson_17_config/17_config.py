# ============================================================
# Python 云计算实战 — 第17课：配置文件解析 configparser / yaml
# ============================================================
# 知识点：
#   configparser 模块：读取/写入 .ini 格式配置文件
#     config = configparser.ConfigParser()
#     config.read("config.ini")                    # 读取配置
#     config["section"]["key"]                      # 获取值
#     config["section"]["key"] = "value"           # 修改值
#     config.write(open("config.ini", "w"))         # 写入文件
#
#   yaml 模块（需 pip install pyyaml）：
#     import yaml
#     data = yaml.safe_load(open("config.yaml"))    # 读取 YAML
#     yaml.dump(data, open("config.yaml", "w"))     # 写入 YAML
#
#   运维场景：云服务配置（数据库连接、API密钥、服务器参数）统一管理
# ============================================================

# ---- 题目1 ----
# 用 configparser 读取 cloud_config.ini 配置文件，打印数据库连接信息
# 配置文件 cloud_config.ini 内容如下（请先创建该文件）：
#   [database]
#   host = 10.0.1.50
#   port = 3306
#   user = root
#   password = admin123
#   [server]
#   host = 0.0.0.0
#   port = 8080
#   debug = true
# 要求打印：
#   Database: root@10.0.1.50:3306
#   Server: 0.0.0.0:8080 (debug=True)

# 请在下方写下你的答案：
import configparser

cloudConf = configparser.ConfigParser()
cloudConf.read("cloud_config.ini")
sv = cloudConf["server"]
db = cloudConf["database"]
print(f"Database: {db['user']}@{db['host']}:{db['port']}\n")
print(f"Server: {sv['host']}:{sv['port']} (debug={sv['debug']})")

# ---- 题目2 ----
# 用 configparser 修改 server 端口为 9090，debug 改为 false，保存回文件
# 然后再读取一次验证修改是否成功

# 请在下方写下你的答案：
import configparser

cloudConf = configparser.ConfigParser()
cloudConf.read("cloud_config.ini")
cloudConf["server"]["port"] = "9090"
cloudConf["server"]["debug"] = "false"
cloudConf.write(open("cloud_config.ini","w"))
print(cloudConf["server"]["port"],cloudConf["server"]["debug"])


# ---- 题目3 ----
# 用 yaml 读取 cloud_config.yaml 配置文件，打印所有配置信息
# 配置文件 cloud_config.yaml 内容如下（请先创建该文件）：
#   database:
#     host: 10.0.1.50
#     port: 3306
#     user: root
#     password: admin123
#   server:
#     host: 0.0.0.0
#     port: 8080
#     debug: true
#   regions:
#     - cn-hangzhou
#     - cn-shanghai
#     - cn-beijing
# 提示：pip install pyyaml，然后 import yaml，用 yaml.safe_load() 读取

# 请在下方写下你的答案：
import yaml

cloudData = yaml.safe_load(open("cloud_config.yaml"))
print(cloudData)