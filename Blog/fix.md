

TODO:

- Q: 如何查看进程的内存使用情况?
- Q: 进程间通信方式?
- Q: 共享内存是什么?
- Q: MySQL中MVCC的正确打开方式（源码佐证）
————————————————
版权声明：本文为CSDN博主「Waves___」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Waves___/java/article/details/105295060





- Q: mysql 查询耗时
- A: 表没有加索引

- Q: Python 进程内存飙升
- A: 一般有全局对象, 比如捕获 raise出来的全局异常对象, 比如业务全局变量的增加

- Q: MySQL 新版本支持的 performance_schema 性能监控, 会导致 MySQL 内存一直上涨
- A: 
    - 阿里云RDS(MySQL) 可以关闭 performance_schema 参数, 会重启
    - 可以考虑降低 innodb_buffer_pool_size 大小, 比如从 75% 改到 50%





