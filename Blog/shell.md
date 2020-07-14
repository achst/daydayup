
# 有 跳板机 的情况下 scp 拉取远端文件

scp -o "ProxyJump user@jump_server -p 60172"  user@target_server:/tmp/test.csv .