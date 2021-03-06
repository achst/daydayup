网络协议相关
---

- 为什么 websocket 需要依赖 http 握手建立连接, 而不是直接用 tcp?

1. 可行性: websocket 是为了解决服务器向浏览器推送消息而设计的, 浏览器不支持直接调用系统底层的 Socket (tcp/udp).
2. 复用性: 因为 浏览器是基于 HTTP 的标准客户端，而且 HTTP 协议发展到今天在各个方面已经非常成熟，所以最大程度复用是合理的。

某网友:
浏览器不能通过操作系统的 API 发起直接基于 TCP 的 Socket，是各大浏览器厂商遵循 W3C、ECMA 规范的结果。如果浏览器厂商不想遵循规范，
它完全可以编制一套 API 让网页直接发起基于 TCP 的 Socket 连接。W3C、ECMA 规范只允许 WebSocket 而不允许 TCP Socket，原因就多了去了，
不光是安全，让前端更容易开发也是一个重要的原因。


回答:
websocket 是为了解决服务器与浏览器之间的双工通信设计的, 因为 W3C、ECMA 规范, 浏览器是一个基于 HTTP 的应用, 
所以在实现 websocket 协议采用 http 来握手切换, 对浏览器的改动代价最小.
