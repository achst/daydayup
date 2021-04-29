

TODO:

热重启
https://zhuanlan.zhihu.com/p/230888784

- Q: MySQL中MVCC的正确打开方式（源码佐证）
————————————————
版权声明：本文为CSDN博主「Waves___」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Waves___/java/article/details/105295060
  
深入揭秘 epoll 是如何实现 IO 多路复用的！(重温)
https://mp.weixin.qq.com/s/6JNLyVlE6BWU-zScNuaYvQ


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


- Q: 共享内存是什么?
    现代Linux有两种共享内存机制：
        - POSIX 共享内存
           - shm_open()、shm_unlink() 结合 mmap() 使用
        - System V 共享内存
           - shmget()、shmat()、shmdt()
    mmap 和 System V 共享内存的主要区别在于：
         - sysv shm是持久化的，除非被一个进程明确的删除，否则它始终存在于内存里，直到系统关机； 
         - mmap 映射的内存在不是持久化的，如果进程关闭，映射随即失效，除非事先已经映射到了一个文件上。
    mmap 内存映射机制:
         - 匿名映射. 
             - 使用进程的虚拟内存空间，它和 malloc(3)类似，实际上有些malloc实现会使用mmap匿名映射分配内存，不过匿名映射不是POSIX标准中规定的。
         - 文件映射.
             - 有 MAP_PRIVATE 和 MAP_SHARED 两种。前者使用 COW 的方式，把文件映射到当前的进程空间，修改操作不会改动源文件。后者直接把文件映射到当前的进程空间，所有的修改会直接反应到文件的page cache，然后由内核自动同步到映射文件上。
    基于 mmap 的优势: 
         - 相比于IO函数调用，基于文件的 mmap 的一大优点是把文件映射到进程的地址空间，避免了数据从用户缓冲区到内核 page cache 缓冲区的复制过程；
         - 当然还有一个优点就是不需要频繁的 read/write 系统调用。
         - 由于接口易用，且可以方便的 persist 到文件，避免主机 shutdown 丢失数据的情况，所以在现代操作系统上一般偏向于使用 mmap 而不是传统的 System V 的共享内存机制。
    什么时候用共享内存:
         - 建议仅把 mmap 用于需要大量内存数据操作的场景，而不用于IPC。
           因为IPC总是在多个进程之间通信，而通信则涉及到同步问题，如果自己手工在mmap之上实现同步，容易滋生 bug。
           推荐使用socket之类的机制做IPC，基于socket的通信机制相对健全很多，有很多成熟的机制和模式，比如 epoll, reactor 等。  



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
    
- Q: mysql特别长的字符串如何索引？
- A: 使用前缀索引, 导入 es 等全文索引工具 (mysql 自带的全文索引似乎不太稳定)
     - like 'abc%' 这种会走索引 (最左匹配原则)
     - like '%abc%' 不会
     - like '%abc' 这种要建立`反向索引` (通过翻转函数把字符串倒转过来, 再建立索引) (实际上也是利用最左匹配原则)








