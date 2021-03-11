

TODO:


  

- Q: 共享内存是什么?
- Q: MySQL中MVCC的正确打开方式（源码佐证）
————————————————
版权声明：本文为CSDN博主「Waves___」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Waves___/java/article/details/105295060


- Q: 进程间通信方式?
- A: 进程之间要通信必须通过内核, socket 也是经过了内核空间的.
    - 信号:  kill -l
            ```
             1) SIGHUP       2) SIGINT       3) SIGQUIT      4) SIGILL       5) SIGTRAP
             6) SIGABRT      7) SIGBUS       8) SIGFPE       9) SIGKILL     10) SIGUSR1
            11) SIGSEGV     12) SIGUSR2     13) SIGPIPE     14) SIGALRM     15) SIGTERM
            16) SIGSTKFLT   17) SIGCHLD     18) SIGCONT     19) SIGSTOP     20) SIGTSTP
            21) SIGTTIN     22) SIGTTOU     23) SIGURG      24) SIGXCPU     25) SIGXFSZ
            26) SIGVTALRM   27) SIGPROF     28) SIGWINCH    29) SIGIO       30) SIGPWR
            31) SIGSYS      34) SIGRTMIN    35) SIGRTMIN+1  36) SIGRTMIN+2  37) SIGRTMIN+3
            38) SIGRTMIN+4  39) SIGRTMIN+5  40) SIGRTMIN+6  41) SIGRTMIN+7  42) SIGRTMIN+8
            43) SIGRTMIN+9  44) SIGRTMIN+10 45) SIGRTMIN+11 46) SIGRTMIN+12 47) SIGRTMIN+13
            48) SIGRTMIN+14 49) SIGRTMIN+15 50) SIGRTMAX-14 51) SIGRTMAX-13 52) SIGRTMAX-12
            53) SIGRTMAX-11 54) SIGRTMAX-10 55) SIGRTMAX-9  56) SIGRTMAX-8  57) SIGRTMAX-7
            58) SIGRTMAX-6  59) SIGRTMAX-5  60) SIGRTMAX-4  61) SIGRTMAX-3  62) SIGRTMAX-2
            63) SIGRTMAX-1  64) SIGRTMAX
            ```
      
    - 信号量：不能传递复杂消息，只能用来同步. 
            信号量其实是一个计数器，表示的是资源个数，其值可以通过两个原子操作来控制，分别是 P 操作和 V 操作。
    
    - 共享内存区：能够很容易控制容量，速度快，但要 (利用 信号量) 保持同步，比如一个进程在写的时候，另一个进程要注意读写的问题，相当于线程中的线程安全.
                当然，共享内存区同样可以用作线程间通讯，不过没这个必要 (需要访问内核空间)，线程间本来就已经共享了同一进程内的一块内存 (用户空间).
    
    - socket: 跨网络与不同主机上的进程之间通信，就需要 Socket 通信了 (TCP UDP)
      
    - 管道: 比如经常用的 linux 匿名管道命令: "|", 半双工通信 (单向的) 
      
    - 消息队列: 一般指代的是 linux 提供的消息队列, 而不是 kafka 这种消息队列 (项目中一般用后者)


- Q: 如何查看进程的内存使用情况?
- A:
    1. 首先, 可以通过 ps 命令找到进程id. `ps -ef | grep kafka`
    2. 然后, 可以通过 top 命令实时的看到 CPU 和 内存 的占用率. `top -p 2913` (按 q 退出)

- Q: mysql 查询耗时
- A: 表没有加索引

- Q: Python 进程内存飙升
- A: 一般有全局对象, 
      - 比如捕获 raise 出来的全局异常, 严重的还会导致异常栈溢出, 
      - 比如业务全局变量 hash map 的累积

- Q: MySQL 新版本支持的 performance_schema 性能监控, 会导致 MySQL 内存一直上涨
- A: 
    - 阿里云RDS(MySQL) 可以关闭 performance_schema 参数, 会重启
    - 可以考虑降低 innodb_buffer_pool_size 大小, 比如从 75% 改到 50%





