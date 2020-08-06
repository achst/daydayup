

## 服务器导出文件, scp 拉取到本地的命令:

#### 有 跳板机 的情况下 scp 拉取远端文件
#### 适合正式环境
`scp -o "ProxyJump user@jump_server -p 60172"  user@target_server:/tmp/*.csv .`

```
scp -o "ProxyJump tanshuai@10.104.23.157 -p 50092"  tanshuai@t-uae-mashi-admin:/tmp/\*.csv .
sftp -P 22 -o "ProxyCommand=ssh tanshuai@10.104.23.157 -p 50092 -W %h:%p" tanshuai@t-uae-mashi-admin:/tmp/\*.csv .
```

#### ssh 隧道端口拉取文件
#### 适合测试环境
`scp -P 22090 user@10.104.36.251:/tmp/*.csv .`

注意:
zsh shell 要转义符号 *, 改为 \*


## redis 批量删除 key

#### 批量删除以video开头的key
`redis-cli keys video* | xargs redis-cli del`

#### 以j，r开头，紧跟edis字符串的所有键
`redis-cli keys [j,r]edis | xargs redis-cli del`

