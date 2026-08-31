
#!/bin/bash
# ==================================================
# 健康检查脚本
# ==================================================
SERVER_NAME="web-server-01"
DISK_THRESHOLD="80"

check_time() {
    echo "检查时间: $(date '+%Y-%m-%d %H:%M:%S')"
}

check_disk() {
    local usage=$(df -h | tail -1 | awk '{print $5}' | tr -d '%')
    if [ -z "$usage" ]; then
        usage="N/A"
    fi
    if [ "$usage" != "N/A" ] && [ $usage -gt $DISK_THRESHOLD ]; then
        echo "[WARN] 磁盘使用率: ${usage}% (阈值: ${DISK_THRESHOLD}%)"
    else
        echo "[OK] 磁盘使用率: ${usage}% (阈值: ${DISK_THRESHOLD}%)"
    fi
}

check_memory() {
    echo "[OK] 内存使用: "
    free -h 2>/dev/null | head -2 || vmstat 2>/dev/null | head -2 || echo "  无法获取内存信息"
}

check_processes() {
    local pcount=$(ps aux | wc -l 2>/dev/null)
    if [ -z "$pcount" ] || [ "$pcount" -eq 0 ]; then
        pcount="N/A"
    fi
    echo "[OK] 运行进程数: $pcount"
}

main() {
    echo "======== 健康检查报告: $SERVER_NAME ========"
    check_time
    check_disk
    check_memory
    check_processes
    echo "======== 检查完成 ========"
}

main
