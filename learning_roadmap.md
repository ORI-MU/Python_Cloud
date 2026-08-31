# Python 云计算工程师 — 完整学习路线（HCIE-Cloud Computing 对标版）

> 目标认证：华为 HCIE-Cloud Computing（笔试 H13-531 + 实验 + 面试）
> 标注 🎯 的课程为 HCIE 考试直接相关

---

## 第一阶段：Python 基础（已完成 ✅）

| 课号 | 内容 | 目录 | 状态 |
|------|------|------|------|
| 01 | Hello World、print | lesson_01_hello | ✅ |
| 02 | 变量、数据类型 | lesson_02_variables | ✅ |
| 03 | input 用户输入 | lesson_03_input | ✅ |
| 04 | if/else 条件判断 | lesson_04_if_else | ✅ |
| 05 | list 列表 | lesson_05_list | ✅ |
| 06 | for/while 循环 | lesson_06_loops | ✅ |
| 07 | dict 字典 | lesson_07_dict | ✅ |
| 08 | 函数 | lesson_08_functions | ✅ |
| 09 | 文件读写 | lesson_09_file_io | ✅ |
| 10 | 异常处理 + JSON + 模块 | lesson_10_advanced | ✅ |

---

## 第二阶段：Python 运维自动化（已完成 ✅）

| 课号 | 内容 | 应用场景 | 目录 | 状态 |
|------|------|----------|------|------|
| 11 | subprocess 执行系统命令 | 调用 Shell、管理进程 | lesson_11_subprocess | ✅ |
| 12 | os / pathlib 文件系统操作 | 管理日志、配置、批量文件 | lesson_12_os_filesystem | ✅ |
| 13 | 正则表达式 re 模块 | 日志解析、文本提取 | lesson_13_regex | ✅ |
| 14 | 时间日期 datetime / time | 定时任务、日志时间戳 | lesson_14_datetime | ✅ |
| 15 | 网络请求 requests 库 | 调用云 API、HTTP 接口 | lesson_15_requests | ✅ |
| 16 | 日志模块 logging | 规范化日志输出 | lesson_16_logging | ✅ |
| 17 | 配置文件解析 configparser / yaml | 读取云服务配置 | lesson_17_config | ✅ |
| 18 | 并发编程 threading / multiprocessing | 批量操作云资源 | lesson_18_concurrency | ✅ |
| 19 | 异步编程 asyncio / aiohttp | 高并发 API 调用 | lesson_19_asyncio | ✅ |
| 20 | 综合实战：自动化运维脚本 | 整合所有知识点 | lesson_20_project | 🔄 |

---

## 第三阶段：Linux 基础 🎯

| 课号 | 内容 | HCIE 考点 |
|------|------|:---------:|
| 21 | Linux 文件系统、目录结构 | ✅ |
| 22 | 用户与权限管理 chmod / chown | ✅ |
| 23 | 进程管理 ps / top / kill | ✅ |
| 24 | Shell 脚本入门 bash | ✅ |
| 25 | 文本处理三剑客 grep / awk / sed | ✅ |
| 26 | 网络工具 curl / netstat / ss | ✅ |
| 27 | systemd 服务管理 | ✅ |
| 28 | 定时任务 crontab | ✅ |

---

## 第四阶段：Linux 深度进阶 🎯（HCIE 核心）

| 课号 | 内容 | HCIE 考点 |
|------|------|:---------:|
| 29 | 磁盘分区与格式化 fdisk / mkfs | ✅ |
| 30 | LVM 逻辑卷管理 | ✅ 重点 |
| 31 | 文件系统修复 fsck / 系统启动流程 GRUB | ✅ 重点 |
| 32 | ACL 访问控制 + SELinux | ✅ |
| 33 | 内核参数调优 sysctl / ulimit | ✅ |
| 34 | 系统性能监控 top / iostat / vmstat | ✅ |
| 35 | 故障排查实战：日志分析、启动失败、磁盘满 | ✅ 重点 |
| 36 | Shell 脚本进阶：函数、数组、调试 | ✅ |

---

## 第五阶段：虚拟化技术 🎯（HCIE 核心）

| 课号 | 内容 | HCIE 考点 |
|------|------|:---------:|
| 37 | 虚拟化原理：CPU/内存/IO 虚拟化 | ✅ |
| 38 | KVM 安装与虚拟机创建（virsh / virt-install） | ✅ 重点 |
| 39 | libvirt 管理：存储池、网络池、快照 | ✅ 重点 |
| 40 | 虚拟机迁移（冷迁移 / 热迁移） | ✅ 重点 |
| 41 | 高可用 HA 与故障恢复 | ✅ 重点 |
| 42 | FusionCompute 架构与安装 | ✅ 重点 |
| 43 | FusionCompute 集群管理与资源调度 | ✅ 重点 |
| 44 | 虚拟化综合实战：搭建虚拟化平台 | ✅ |

---

## 第六阶段：分布式存储 🎯（HCIE 核心）

| 课号 | 内容 | HCIE 考点 |
|------|------|:---------:|
| 45 | 存储基础：DAS / NAS / SAN 区别 | ✅ |
| 46 | NFS 网络文件系统搭建 | ✅ |
| 47 | iSCSI 块存储实战 | ✅ |
| 48 | Ceph 分布式存储架构与部署 | ✅ 重点 |
| 49 | 华为分布式存储 FusionStorage | ✅ 重点 |
| 50 | 存储综合实战：统一存储平台 | ✅ |

---

## 第七阶段：SDN 与虚拟网络 🎯（HCIE 核心）

| 课号 | 内容 | HCIE 考点 |
|------|------|:---------:|
| 51 | 网络基础回顾：TCP/IP、VLAN、路由 | ✅ |
| 52 | Open vSwitch (OVS) 安装与配置 | ✅ 重点 |
| 53 | VXLAN 隧道技术 | ✅ 重点 |
| 54 | SDN 架构与 OpenFlow 协议 | ✅ |
| 55 | 华为 SDN 控制器（AC-DCN） | ✅ 重点 |
| 56 | 虚拟网络综合实战：多租户网络隔离 | ✅ |

---

## 第八阶段：Docker 容器

| 课号 | 内容 |
|------|------|
| 57 | Docker 核心概念：镜像、容器、仓库 |
| 58 | Dockerfile 编写最佳实践 |
| 59 | docker-compose 多容器编排 |
| 60 | 容器网络与数据卷 |
| 61 | 镜像优化与多阶段构建 |
| 62 | Docker 日志与监控 |
| 63 | 用 Python 操作 Docker（docker SDK） |

---

## 第九阶段：Kubernetes (K8s) 🎯

| 课号 | 内容 | HCIE 考点 |
|------|------|:---------:|
| 64 | K8s 核心概念：Pod、Service、Deployment | ✅ |
| 65 | 资源清单 YAML 编写 | ✅ |
| 66 | ConfigMap / Secret 配置管理 | ✅ |
| 67 | 存储卷 PV / PVC | ✅ |
| 68 | Ingress 网络入口 | ✅ |
| 69 | Helm 包管理工具 | 加分项 |
| 70 | 用 Python 操作 K8s（kubernetes-client） | 加分项 |

---

## 第十阶段：CI/CD 与 DevOps 工具链

| 课号 | 内容 |
|------|------|
| 71 | Git 版本控制进阶 |
| 72 | GitHub Actions / GitLab CI |
| 73 | Jenkins 流水线 |
| 74 | Ansible 自动化部署 |
| 75 | Terraform 基础设施即代码 |

---

## 第十一阶段：云平台实战 🎯

| 课号 | 内容 | HCIE 考点 |
|------|------|:---------:|
| 76 | 华为云 SDK 实战（ECS、OBS、VPC） | ✅ 重点 |
| 77 | 华为云 FusionCloud 架构 | ✅ 重点 |
| 78 | 阿里云 SDK 实战（ECS、OSS、SLB） | 加分项 |
| 79 | AWS SDK boto3 实战 | 加分项 |
| 80 | 云资源监控与告警（Prometheus + Grafana） | ✅ |
| 81 | 成本优化与资源清理 | ✅ |

---

## 第十二阶段：HCIE 综合实战项目 🏗️

| 项目 | 内容 | HCIE 对标 |
|------|------|:---------:|
| 项目1 | 企业级虚拟化平台搭建（KVM + 热迁移 + HA） | 实验重点 |
| 项目2 | 分布式存储集群部署（Ceph + 故障恢复） | 实验重点 |
| 项目3 | Docker 化 Python 应用并部署到 K8s | 笔试重点 |
| 项目4 | CI/CD 流水线搭建（代码→镜像→部署） | 面试加分 |
| 项目5 | 云资源一键开通/销毁脚本（华为云 SDK） | 面试重点 |

---

## 总览

```
Python基础 ✅ → 运维自动化 ✅ → Linux基础 → Linux深度 → 虚拟化 → 存储 → SDN网络
   (10课)         (10课)         (8课)      (8课)      (8课)    (6课)   (6课)

  → Docker → K8s → CI/CD → 云平台 → 实战项目
   (7课)   (7课)  (5课)   (6课)    (5项)
```

| 维度 | 数据 |
|------|------|
| 总课数 | 81 课 |
| 实战项目 | 5 个 |
| 🎯 HCIE 直接相关 | 约 55 课（68%） |
| 预计周期 | 4-6 个月 |

---

## HCIE 考试覆盖热力图

```
阶段1 Python基础      ████░░░░░░ 40% (笔试不考，实验/面试加分)
阶段2 运维自动化      ██████░░░░ 60% (实验自动化脚本)
阶段3 Linux基础       ██████████ 100% (笔试+实验)
阶段4 Linux深度       ██████████ 100% (实验核心)
阶段5 虚拟化          ██████████ 100% (实验核心)
阶段6 分布式存储      ██████████ 100% (实验核心)
阶段7 SDN虚拟网络     ██████████ 100% (实验核心)
阶段8 Docker          ██████░░░░ 60% (笔试重点)
阶段9 K8s             ██████░░░░ 60% (笔试重点)
阶段10 CI/CD          ████░░░░░░ 40% (面试加分)
阶段11 云平台         ████████░░ 80% (笔试+面试)
阶段12 实战项目       ██████████ 100% (面试核心)
```

---

## 运行方式

```powershell
# 进入对应课程目录，用 py 启动器运行（推荐）
cd stage_03_linux\lesson_21_linux_fs
py 21_linux_fs.py

# 或用完整路径直接运行
py f:\桌面\python_learning\stage_03_linux\lesson_21_linux_fs\21_linux_fs.py
```

> 本机使用 `py` 启动器（Python 3.13），`python` 命令不可用。

---

## 出题规范（AI 执行标准）

### 互动模式
1. AI 出题，写在 `.py` 文件里
2. 用户写代码
3. 用户扣 `1` 表示交卷，AI 检查后运行验证
4. 通过后进入下一课

### 文件结构
```
每课目录/
├── XX_主题.py          ← 主文件（知识点 + 题目）
├── XX_hints.md         ← 结构方案（可选，用户要求时才创建）
└── 依赖文件（.sh / .conf / 数据文件等，由 AI 自动创建）
```

### 代码风格
- 每个知识点 = 语法说明（注释） + 完整示例（注释掉的代码，自带 import）
- 示例**不要自动运行**，用户自己取消注释执行
- 每道题 = 紧接在知识点示例后面，方便用户照猫画虎
- 每个 import 写在对应示例/题目里，**不要放文件顶部**
- 所有执行代码放在 `if __name__ == "__main__"` 里
- 不要写过多注释，关键行注释即可

### 出题规则
- 出题时自动创建目录和所有需要的文件（配置文件、示例数据等）
- 题目依赖第三方库时，自动用 `py -m pip install xxx` 安装
- 不让用户手动创建任何文件或安装任何包
- 出题后运行 `py <文件路径>` 验证文件可正常执行

### 题目难度标准
- 对标 HCIE 考点标记：有 🎯 的课可以适当拔高，无标记的课以**能看懂、会改、能跑**为目标
- 每道题 = 知识点示例的变体，用户能照猫画虎完成
- 优先考虑 Windows 兼容性，Linux 专有命令给出降级方案

### 自动 Git 推送
- 每道题通过后，自动执行 `git add . && git commit -m "xxx" && git push`
- 远程仓库：`https://github.com/ORI-MU/Python_Cloud.git`
- `.gitignore` 不要忽略 `.sh` 文件（Shell 脚本也是学习成果）

### 运行方式
```powershell
py f:\桌面\python_learning\stage_XX_xxx\lesson_XX_xxx\XX_xxx.py
```