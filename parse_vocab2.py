#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 markdown 词汇表解析并添加到 content.js - 第 2 部分 (J-Z)
"""

import re
from pathlib import Path

VOCAB_DATA = """
### J

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| Java applet | Java 小程序 |  | |
| JavaScript | JavaScript |  | |
| join | 联合 | 连接 | |
| jump | 跳转 |  | |
| just in time, JIT | 即时编译 |  | |

### K

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| keyword | 关键字 |  | |
| knapsack problem | 背包问题 |  | |

### L

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| lambda calculus | lambda 演算 |  | |
| lambda expression | lambda 表达式 |  | |
| language | 语言 |  | |
| lazy evaluation | 惰性求值 | 懒求值 | |
| leaf | 叶 | 叶子 | |
| left child | 左子节点 |  | |
| left subtree | 左子树 |  | |
| level | 层 | 级 | |
| lexical | 词法 |  | |
| lexical address | 词法地址 |  | |
| lexical scoping | 词法作用域 |  | |
| library | 库 | 程序库 | |
| life cycle | 生命周期 |  | |
| lifetime | 生命期 |  | |
| Lisp | Lisp 语言 |  | |
| list | 表 | 列表 | |
| list structure | 表结构 |  | |
| literal | 字面常量 | 字面量 | |
| load | 加载 |  | |
| loader | 加载器 |  | |
| local | 局部的 |  | |
| local declaration | 局部声明 |  | |
| local variable | 局部变量 |  | |
| logic programming | 逻辑式编程 |  | |
| loop | 循环 |  | |
| lower bound | 下界 |  | |

### M

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| machine | 机器 |  | |
| machine code | 机器码 |  | |
| machine language | 机器语言 |  | |
| macro | 宏 |  | |
| macro expansion | 宏展开 |  | |
| mail | 邮件 |  | |
| main | 主 |  | |
| maintainability | 可维护性 |  | |
| management | 管理 |  | |
| manifest | 清单 |  | |
| mantissa | 尾数 |  | |
| map | 映射 |  | |
| matrix | 矩阵 |  | |
| mean | 均值 |  | |
| member | 成员 |  | |
| member function | 成员函数 |  | |
| memory | 内存 | 存储器 | |
| message | 消息 |  | |
| message passing | 消息传递 |  | |
| meta | 元 |  | |
| meta-language | 元语言 |  | |
| meta-circular evaluator | 元循环求值器 |  | |
| method | 方法 |  | |
| metric | 度量 |  | |
| microcode | 微码 |  | |
| middle-out | 中间展开 |  | |
| milestone | 里程碑 |  | |
| millennium bug | 千年虫 |  | |
| minimum | 最小值 | 极小值 | |
| mirror | 镜像 |  | |
| miscellaneous | 杂项 | 其他 | |
| modeling | 建模 |  | |
| modeling language | 建模语言 |  | |
| modem | 调制解调器 |  | |
| modification | 修改 |  | |
| module | 模块 |  | |
| monad | 单子 |  | |
| monolithic | 单体的 |  | |
| morphism | 态射 |  | |
| most general unifier | 最广合一子 |  | |
| mouse | 鼠标 |  | |
| multi-method | 多方法 |  | |
| multiple inheritance | 多重继承 |  | |
| multiprocessing | 多处理 |  | |
| multiprogramming | 多道程序设计 |  | |
| multitasking | 多任务 |  | |
| multithreading | 多线程 |  | |
| mutation | 突变 |  | |
| mutual recursion | 相互递归 |  | |

### N

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| name | 名字 | 名称 | |
| namespace | 名字空间 | 命名空间 | |
| native | 原生的 | 本地 | |
| natural language | 自然语言 |  | |
| network | 网络 |  | |
| neural network | 神经网络 |  | |
| node | 节点 |  | |
| non-deterministic | 非确定性的 |  | |
| non-modifying | 非修改的 |  | |
| non-terminating | 不终止的 |  | |
| normal form | 范式 |  | |
| normalization | 规范化 |  | |
| normalization by evaluation | 求值归一化 |  | |
| notation | 表示法 | 记法 | |
| null | 空 |  | |
| null pointer | 空指针 |  | |
| number | 数值 | 数字 | |
| numeric | 数值的 |  | |
| numerical analysis | 数值分析 |  | |
| n-ary | n元 |  | |
| nybble | 半字节 |  | |

### O

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| object | 对象 |  | |
| object code | 目标码 |  | |
| object language | 目标语言 |  | |
| object-oriented | 面向对象 |  | |
| object-oriented programming, OOP | 面向对象编程 |  | |
| observe | 观测 |  | |
| obsolete | 过时 | 废弃 | |
| occurrence | 出现 | 发生 | |
| octal | 八进制 |  | |
| open | 打开 | 开放 | |
| open world assumption | 开放世界假定 |  | |
| operand | 操作数 | 运算对象 | |
| operating system, OS | 操作系统 |  | |
| operation | 操作 | 运算 | |
| operator | 操作符 | 运算符 | |
| opportunistic | 机会式 |  | |
| optimize | 优化 |  | |
| order | 阶 | 序 | |
| ordering | 排序 |  | |
| origin | 原点 | 起源 | |
| orthogonality | 正交性 |  | |
| out of band | 带外 |  | |
| output | 输出 |  | |
| overflow | 溢出 | 上溢 | |
| overload | 重载 |  | |
| overloading | 重载 |  | |
| overriding | 覆盖 | 重写 | |

### P

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| package | 包 |  | |
| padding | 填充 |  | |
| palindrome | 回文 |  | |
| parallel | 并行的 |  | |
| parallelism | 并行性 |  | |
| parameter | 参数 | 形式参数 | 形参 |
| parent | 父节点 |  | |
| parent class | 父类 |  | |
| parse | 语法分析 | 解析 | |
| parser | 语法分析器 | 解析器 | |
| partial | 部分的 | 偏 | |
| partial application | 部分应用 | 偏应用 | |
| partial function | 部分函数 | 偏函数 | |
| partition | 分区 | 划分 | |
| pass | 传递 |  | |
| pass by reference | 引用传递 |  | |
| pass by value | 值传递 |  | |
| password | 口令 | 密码 | |
| path | 路径 |  | |
| pattern | 模式 |  | |
| pattern matching | 模式匹配 |  | |
| payload | 有效载荷 |  | |
| peek | 查看 |  | |
| performance | 性能 | 表现 | |
| peripheral | 外设 | 外围设备 | |
| persistence | 持久化 |  | |
| persistent | 持久的 |  | |
| personal computer, PC | 个人计算机 |  | |
| phase | 阶段 |  | |
| pixel | 像素 |  | |
| place | 位 | 位置 | |
| plain text | 明文 |  | |
| platform | 平台 |  | |
| pointer | 指针 |  | |
| polymorphism | 多态 |  | |
| pop | 弹出 |  | |
| port | 端口 |  | |
| portable | 可移植的 |  | |
| portability | 可移植性 |  | |
| position | 位置 |  | |
| postfix | 后缀 |  | |
| precedence | 优先级 |  | |
| precision | 精度 |  | |
| predicate | 谓词 |  | |
| prefix | 前缀 |  | |
| preorder | 前序 |  | |
| preprocessor | 预处理器 |  | |
| presentation | 表示 | 展现 | |
| primitive | 基本的 | 原语 | 基元 |
| print | 打印 |  | |
| printer | 打印机 |  | |
| priority | 优先级 |  | |
| private | 私有 |  | |
| probe | 探查 |  | |
| procedure | 过程 |  | |
| process | 进程 | 处理 | |
| processor | 处理器 |  | |
| product | 乘积 | 积 | |
| program | 程序 |  | |
| program counter | 程序计数器 |  | |
| programmable | 可编程的 |  | |
| programming | 编程 | 程序设计 | |
| programming language | 程序设计语言 | 编程语言 | |
| project | 项目 | 工程 | |
| projection | 投影 |  | |
| protocol | 协议 |  | |
| pseudo | 伪 |  | |
| pseudo-code | 伪代码 |  | |
| public | 公有 |  | |
| push | 压入 |  | |
| polymorphic | 多态的 |  | |
| pipeline | 流水线 | 管道 | |
| pipe | 管道 |  | |

### Q

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| qualified | 受限的 | 限定的 | |
| quantifier | 量词 |  | |
| query | 查询 |  | |
| queue | 队列 |  | |
| quicksort | 快速排序 |  | |

### R

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| race condition | 竞态条件 |  | |
| radix | 基数 |  | |
| random | 随机 |  | |
| random access memory, RAM | 随机存取存储器 |  | |
| range | 范围 |  | |
| rank | 秩 |  | |
| rational | 有理的 |  | |
| read | 读 | 读取 | |
| read only memory, ROM | 只读存储器 |  | |
| reader | 读取器 |  | |
| record | 记录 |  | |
| recursion | 递归 |  | |
| recursive | 递归的 |  | |
| redirect | 重定向 |  | |
| reduce | 归约 |  | |
| reduction | 归约 |  | |
| redundant | 冗余 |  | |
| reference | 引用 | 参考 | |
| reflection | 反射 |  | |
| refresh | 刷新 |  | |
| register | 寄存器 |  | |
| regular expression | 正则表达式 |  | |
| relational | 关系的 |  | |
| release | 发布 | 释放 | |
| reliability | 可靠性 |  | |
| relocatable | 可重定位的 |  | |
| rem | 余 | 取余 | |
| remote | 远程 |  | |
| repair | 修复 |  | |
| repeat | 重复 |  | |
| repetition | 重复 | 循环 | |
| representation | 表示法 | 表示 | |
| requirement | 需求 | 要求 | |
| reserved word | 保留字 |  | |
| resolution | 分辨率 | 归结 | |
| resolver | 解析器 |  | |
| resource | 资源 |  | |
| response | 响应 |  | |
| restoration | 恢复 |  | |
| restricted | 受限的 |  | |
| result | 结果 |  | |
| return | 返回 |  | |
| reverse | 反转 | 倒序 | |
| right child | 右子节点 |  | |
| right subtree | 右子树 |  | |
| root | 根 |  | |
| rotate | 旋转 |  | |
| round | 舍入 |  | |
| round off | 四舍五入 |  | |
| route | 路由 |  | |
| router | 路由器 |  | |
| routine | 例程 |  | |
| row | 列 | 行 | |
| row-major order | 列主序 |  | |
| RPC | 远程过程调用 |  | |
| rule | 规则 |  | |
| runtime | 运行时 | 执行期 | |

### S

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| sandbox | 沙箱 |  | |
| scalar | 标量 |  | |
| scope | 作用域 | 范围 | |
| search | 搜索 | 查找 | |
| security | 安全性 | 安全 | |
| seed | 种子 |  | |
| segment | 段 | 分段 | |
| selection | 选择 |  | |
| semantic | 语义 |  | |
| semantics | 语义学 | 语义 | |
| sentinel | 哨兵 |  | |
| sequence | 序列 |  | |
| sequential | 顺序的 | 串行的 | |
| serial | 串行 |  | |
| server | 服务器 |  | |
| service | 服务 |  | |
| session | 会话 |  | |
| set | 集合 |  | |
| setter | 设置器 |  | |
| shadow | 遮蔽 |  | |
| shared | 共享的 |  | |
| shell | 外壳 | 命令行 | |
| shift | 移位 | 偏移 | |
| shortcut | 快捷方式 |  | |
| sibling | 兄弟节点 |  | |
| side effect | 副作用 |  | |
| signal | 信号 |  | |
| signature | 签名 | 特征 | |
| simulation | 模拟 | 仿真 | |
| singleton | 单例 |  | |
| size | 大小 | 尺寸 | |
| slice | 切片 |  | |
| small talk | 聊天 |  | |
| socket | 套接字 |  | |
| software | 软件 |  | |
| source | 源 | 来源 | |
| source code | 源代码 |  | |
| source language | 源语言 |  | |
| specialization | 特化 |  | |
| stack | 栈 | 堆栈 | |
| stack overflow | 栈溢出 |  | |
| statement | 语句 | 陈述 | |
| static | 静态的 |  | |
| static binding | 静态绑定 |  | |
| static scope | 静态作用域 |  | |
| static type | 静态类型 |  | |
| status | 状态 |  | |
| step | 步骤 | 步长 | |
| storage | 存储 |  | |
| stream | 流 |  | |
| string | 字符串 |  | |
| structure | 结构 |  | |
| structured programming | 结构化编程 |  | |
| subclass | 子类 |  | |
| subexpression | 子表达式 |  | |
| subroutine | 子例程 |  | |
| subschema | 子模式 |  | |
| subsequence | 子序列 |  | |
| subset | 子集 |  | |
| substitution | 代入 | 替换 | |
| subtype | 子类型 |  | |
| subtree | 子树 |  | |
| superclass | 超类 | 父类 | |
| support | 支持 |  | |
| symbol | 符号 |  | |
| syntax | 语法 |  | |
| system | 系统 |  | |
| system call | 系统调用 |  | |

### T

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| tail | 尾 | 尾部 | |
| tail recursion | 尾递归 |  | |
| target | 目标 |  | |
| task | 任务 |  | |
| template | 模板 |  | |
| terminal | 终端 |  | |
| terminating | 终止的 |  | |
| termination | 终止 | 结束 | |
| term rewriting system | 项重写系统 |  | |
| test | 测试 |  | |
| testing | 测试 |  | |
| text | 文本 | 正文 | |
| theorem | 定理 |  | |
| theory | 理论 |  | |
| thread | 线程 |  | |
| throw | 抛出 | 扔 | |
| time | 时间 |  | |
| time-sharing | 分时 |  | |
| timeout | 超时 |  | |
| timestamp | 时间戳 |  | |
| token | 令牌 | 词法单元 | |
| top-down | 自顶向下 |  | |
| top-down programming | 自顶向下编程 |  | |
| topic | 主题 | 话题 | |
| trailing | 尾部 | 后随 | |
| transaction | 事务 |  | |
| transfer | 传送 | 转移 | |
| transform | 变换 |  | |
| transformation | 变换 | 转换 | |
| transition | 过渡 | 变迁 | |
| translation | 翻译 | 平移 | |
| transmission | 传输 | 传送 | |
| transparent | 透明 |  | |
| tree | 树 |  | |
| traversal | 遍历 |  | |
| traverse | 遍历 |  | |
| tuple | 元组 |  | |
| Turing machine | 图灵机 |  | |
| type | 类型 |  | |
| type checking | 类型检查 |  | |
| type constructor | 类型构造器 |  | |
| type error | 类型错误 |  | |
| type inference | 类型推导 |  | |
| type system | 类型系统 |  | |
| typo | 笔误 | 打印错误 | |

### U

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| unary | 一元 |  | |
| unbound | 未绑定 |  | |
| undefined | 未定义 |  | |
| underflow | 下溢 |  | |
| unification | 合一 | 统一 | |
| uniform | 一致的 | 均匀 | |
| union | 并集 | 联合 | |
| unique | 唯一的 | 独特的 | |
| unit | 单元 |  | |
| unit test | 单元测试 |  | |
| universe | 论域 | 宇宙 | |
| Unix | Unix 操作系统 |  | |
| unload | 卸载 |  | |
| unlock | 解锁 |  | |
| unpack | 解包 |  | |
| unsigned | 无符号 |  | |
| untyped | 无类型 |  | |
| update | 更新 |  | |
| upgrade | 升级 |  | |
| upload | 上传 |  | |
| URI | 统一资源标识符 |  | |
| URL | 统一资源定位符 |  | |
| usability | 可用性 |  | |
| use case | 用例 |  | |
| user | 用户 |  | |
| user interface, UI | 用户界面 |  | |
| utility | 实用工具 | 实用程序 | |

### V

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| valid | 有效的 |  | |
| validate | 验证 |  | |
| value | 值 | 数值 | |
| variable | 变量 |  | |
| variance | 协变 | 变体 | |
| vector | 向量 |  | |
| verbose | 啰嗦 | 冗长 | |
| verify | 验证 | 校验 | |
| version | 版本 |  | |
| vertex | 顶点 |  | |
| vertical | 垂直的 |  | |
| VGA | 视频图形阵列 |  | |
| virtual | 虚拟的 |  | |
| virtual function | 虚函数 |  | |
| virtual machine | 虚拟机 |  | |
| virtual memory | 虚拟内存 |  | |
| virus | 病毒 |  | |
| visibility | 可见性 |  | |
| visitor | 访问者 |  | |
| volatile | 易失的 | 不稳定的 | |
| volume | 卷 | 音量 | |

### W

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| walk | 遍历 | 走查 | |
| whitespace | 空白 |  | |
| wide | 宽的 |  | |
| widget | 小部件 | 组件 | |
| window | 窗口 |  | |
| wireless | 无线 |  | |
| word | 字 | 单词 | |
| workstation | 工作站 |  | |
| wrapper | 包装器 |  | |
| write | 写 | 写入 | |

### X

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| XML | 可扩展标记语言 |  | |

### Y

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| yacc | yacc 编译器 |  | |

### Z

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| zero | 零 |  | |
| zip | 压缩 | 拉链 | |

### 专业名词

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| A* search algorithm | A*搜索算法 |  | |
| abstract data type, ADT | 抽象数据类型 |  | |
| American National Standards Institute, ANSI | 美国国家标准学会 |  | |
| Advanced Research Projects Agency Network, ARPANET | 阿帕网 |  | |
| American Standard Code for Information Interchange, ASCII | 美国信息交换标准码 |  | |
| Asynchronous JavaScript and XML, AJAX | 异步 JavaScript 和 XML |  | |
| binary-coded decimal, BCD | 二进制编码的十进制 |  | |
| Basic Combined Programming Language, BCPL | 基本组合编程语言 |  | |
| Berkeley Software Distribution, BSD | 伯克利软件发行版 |  | |
| Business Software Alliance, BSA | 商业软件联盟 |  | |
| Canadian National Standard, CNS | 中国国家标准 |  | |
| Centronics | Centronics 接口 |  | |
| Common Business-Oriented Language, COBOL | 面向商业的通用语言 |  | |
| Common Object Request Broker Architecture, CORBA | 公共对象请求代理体系结构 |  | |
| Compact Disc Read-Only Memory, CD-ROM | 只读光盘 |  | |
| Computer Aided Design, CAD | 计算机辅助设计 |  | |
| Computer Aided Manufacturing, CAM | 计算机辅助制造 |  | |
| Computer Aided Software Engineering, CASE | 计算机辅助软件工程 |  | |
| Computer Science, CS | 计算机科学 |  | |
| Computer Supported Cooperative Work, CSCW | 计算机支持的协同工作 |  | |
| Digital Video Disc, DVD | 数字视频光盘 |  | |
| Electronic Numerical Integrator and Computer, ENIAC | 电子数字积分计算机 |  | |
| European Organization for Nuclear Research, CERN | 欧洲核子研究组织 |  | |
| Extensible Markup Language, XML | 可扩展标记语言 |  | |
| Extensible Stylesheet Language, XSL | 可扩展样式表语言 |  | |
| File Transfer Protocol, FTP | 文件传输协议 |  | |
| Free Software Foundation, FSF | 自由软件基金会 |  | |
| GNU General Public License, GPL | GNU 通用公共许可证 |  | |
| GNU's Not Unix, GNU | GNU 项目 |  | |
| Graphical User Interface, GUI | 图形用户界面 |  | |
| HyperText Markup Language, HTML | 超文本标记语言 |  | |
| HyperText Transfer Protocol, HTTP | 超文本传输协议 |  | |
| Institute of Electrical and Electronics Engineers, IEEE | 电气和电子工程师协会 |  | |
| International Business Machines, IBM | 国际商业机器公司 |  | |
| International Organization for Standardization, ISO | 国际标准化组织 |  | |
| Internet Corporation for Assigned Names and Numbers, ICANN | 互联网名称与数字地址分配机构 |  | |
| Internet Message Access Protocol, IMAP | 互联网消息访问协议 |  | |
| Internet Protocol, IP | 网际协议 |  | |
| Internet Service Provider, ISP | 互联网服务提供商 |  | |
| Java 2 Platform Enterprise Edition, J2EE | Java 2 平台企业版 |  | |
| Java 2 Platform Micro Edition, J2ME | Java 2 平台微型版 |  | |
| Java 2 Platform Standard Edition, J2SE | Java 2 平台标准版 |  | |
| JavaScript Object Notation, JSON | JavaScript 对象表示法 |  | |
| Local Area Network, LAN | 局域网 |  | |
| Massachusetts Institute of Technology, MIT | 麻省理工学院 |  | |
| Metropolitan Area Network, MAN | 城域网 |  | |
| Microsoft Foundation Classes, MFC | 微软基础类库 |  | |
| Multipurpose Internet Mail Extensions, MIME | 多用途互联网邮件扩展 |  | |
| MySQL | MySQL 数据库 |  | |
| National Institute of Standards and Technology, NIST | 美国国家标准与技术研究院 |  | |
| Object Management Group, OMG | 对象管理组织 |  | |
| Object Relational Mapping, ORM | 对象关系映射 |  | |
| Open Database Connectivity, ODBC | 开放数据库连接 |  | |
| Open Source Initiative, OSI | 开源计划 |  | |
| Open Systems Interconnection, OSI | 开放系统互连 |  | |
| Open Virtualization Format, OVF | 开放虚拟化格式 |  | |
| Perl | Perl 语言 |  | |
| PHP: Hypertext Preprocessor, PHP | PHP 语言 |  | |
| Point-to-Point Protocol, PPP | 点对点协议 |  | |
| Post Office Protocol version 3, POP3 | 邮局协议版本 3 |  | |
| Python | Python 语言 |  | |
| Query Language, QL | 查询语言 |  | |
| Rapid Application Development, RAD | 快速应用开发 |  | |
| Ruby | Ruby 语言 |  | |
| Structured Query Language, SQL | 结构化查询语言 |  | |
| Transmission Control Protocol, TCP | 传输控制协议 |  | |
| Transport Layer Security, TLS | 传输层安全 |  | |
| Uniform Resource Identifier, URI | 统一资源标识符 |  | |
| Uniform Resource Locator, URL | 统一资源定位符 |  | |
| Universal Serial Bus, USB | 通用串行总线 |  | |
| Unix-like | 类 Unix |  | |
| Visual Basic, VB | Visual Basic 语言 |  | |
| Virtual Reality, VR | 虚拟现实 |  | |
| Visual Studio, VS | Visual Studio |  | |
| Wide Area Network, WAN | 广域网 |  | |
| Wireless Application Protocol, WAP | 无线应用协议 |  | |
| Wireless Local Area Network, WLAN | 无线局域网 |  | |
| World Wide Web, WWW | 万维网 |  | |
| eXtensible Business Reporting Language, XBRL | 可扩展商业报告语言 |  | |
| eXtensible Markup Language, XML | 可扩展标记语言 |  | |
| eXtensible Stylesheet Language Transformations, XSLT | 可扩展样式表语言转换 |  | |
| Zend Engine | Zend 引擎 |  | |
"""

def parse_vocabulary(data: str) -> dict:
    """解析词汇表"""
    translations = {}
    pattern = r'\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|'
    matches = re.findall(pattern, data)

    for english, zh1, zh2, zh3 in matches:
        english = english.strip()
        zh1 = zh1.strip()

        if english in ["英文", "**英文**", "---", ""]:
            continue
        if zh1 in ["译法 1", ""]:
            continue

        primary = zh1
        translations[english] = primary

    return translations

def parse_existing(content_js_path: str) -> set:
    """解析现有的翻译"""
    content = Path(content_js_path).read_text(encoding="utf-8")
    pattern = r'\[\s*`([^`]*)`\s*,\s*`([^`]*)`\s*\]'
    matches = re.findall(pattern, content)
    existing = set()
    for eng, zh in matches:
        eng = eng.strip()
        if eng:
            existing.add(eng)
    return existing

def escape_js_string(s: str) -> str:
    """转义 JavaScript 字符串"""
    return s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

def append_translations(content_js_path: str, new_translations: dict, existing: set) -> int:
    """追加新翻译到 content.js"""
    to_add = {}
    for eng, zh in new_translations.items():
        if eng not in existing and zh:
            to_add[eng] = zh

    if not to_add:
        print("没有需要添加的新翻译")
        return 0

    content = Path(content_js_path).read_text(encoding="utf-8")

    pattern = r'(\s*\][,;]?\s*$)'
    match = re.search(pattern, content, re.MULTILINE)

    if not match:
        raise ValueError("无法找到数组结束位置")

    new_entries = ""
    for eng, zh in sorted(to_add.items()):
        eng_escaped = escape_js_string(eng)
        zh_escaped = escape_js_string(zh)
        new_entries += f"  [`{eng_escaped}`, `{zh_escaped}`],\n"

    insert_pos = match.start()
    new_content = content[:insert_pos] + ",\n" + new_entries + content[insert_pos:]

    Path(content_js_path).write_text(new_content, encoding="utf-8")
    print(f"成功添加 {len(to_add)} 条新翻译")
    return len(to_add)

def validate_syntax(content_js_path: str) -> bool:
    """验证 JavaScript 语法"""
    content = Path(content_js_path).read_text(encoding="utf-8")
    open_brackets = content.count("[")
    close_brackets = content.count("]")
    backticks = content.count("`")
    print(f"语法检查: [ {open_brackets}, ] {close_brackets}, ` {backticks}")
    if open_brackets == close_brackets and backticks % 2 == 0:
        print("OK: 语法检查通过")
        return True
    else:
        print("ERROR: 语法检查失败")
        return False

def main():
    content_js_path = r"d:\调取\githubCN-main\src\js\content.js"

    print("解析词汇表 (J-Z)...")
    vocab = parse_vocabulary(VOCAB_DATA)
    print(f"解析到 {len(vocab)} 条词汇")

    print("\n检查现有翻译...")
    existing = parse_existing(content_js_path)
    print(f"现有 {len(existing)} 条翻译")

    new_words = set(vocab.keys()) - existing
    print(f"需要添加 {len(new_words)} 条新翻译")

    new_translations = {k: v for k, v in vocab.items() if k in new_words}

    print("\n添加翻译...")
    added = append_translations(content_js_path, new_translations, existing)

    if added > 0:
        print("\n验证语法...")
        validate_syntax(content_js_path)

    print("\n完成！")

if __name__ == "__main__":
    main()
