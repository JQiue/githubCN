#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
从 markdown 词汇表解析并添加到 content.js
"""

import re
import json
from pathlib import Path

VOCAB_DATA = """
### A

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| a block of pointers | 一块指针 | 一组指针 | |
| abbreviation | 缩略语 |  | |
| abstract | 抽象的 |  | |
| abstract syntax tree, AST | 抽象语法树 |  | |
| abstraction | 抽象 |  | |
| abstraction barrier | 抽象屏障 | 抽象阻碍 | |
| abstraction of function calls | 函数调用抽象 |  | |
| access | 访问 | 存取 | |
| access function | 访问函数 | 存取函数 | |
| accumulator | 累加器 |  | |
| activate | 激活 |  | |
| ad hoc | 专设 |  | |
| adapter | 适配器 |  | |
| address | 地址 |  | |
| algebraic data type | 代数数据类型 |  | |
| algorithm | 算法 |  | |
| alias | 别名 |  | |
| allocate | 分配 | 配置 | |
| alternative | 备选 |  | |
| amortized analysis | 平摊分析 |  | |
| anaphoric | 指代 |  | |
| annotation | 注解 |  | |
| anonymous function | 匿名函数 |  | |
| antecedent | 前提 | 前件 | 先决条件 |
| append | 追加 | 拼接 | |
| application | 应用 | 应用程序 | |
| application framework | 应用框架 |  | |
| application program interface, API | 应用程序编程接口 |  | |
| application service provider, ASP | 应用程序服务提供商 |  | |
| applicative | 应用序 |  | |
| argument | 参数 | 自变量 | 实际参数/实参 |
| arithmetic | 算术 |  | |
| array | 数组 |  | |
| artificial intelligence, AI | 人工智能 |  | |
| assemble | 组合 |  | |
| assembly | 汇编 |  | |
| assignment | 赋值 |  | |
| assignment operator | 赋值操作符 |  | |
| associated | 关联的 |  | |
| association list, alist | 关联列表 |  | |
| atom | 原子 |  | |
| atomic | 原子的 |  | |
| atomic value | 原子型值 |  | |
| attribute | 属性 | 特性 | |
| augmented | 扩充 |  | |
| automatic memory management | 自动内存管理 |  | |
| automatically infer | 自动推导 |  | |
| autometa theory | 自动机理论 |  | |
| auxiliary | 辅助 |  | |

### B

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| backquote | 反引用 |  | |
| backtrace | 回溯 |  | |
| backward compatible | 向下兼容 |  | |
| bandwidth | 带宽 |  | |
| base case | 基本情形 |  | |
| base class | 基类 |  | |
| Bayes' theorem | 贝叶斯定理 |  | |
| best viable function | 最佳可行函式 | 最佳可行函数 | |
| Bezier curve | 贝塞尔曲线 |  | |
| bignum | 大数 |  | |
| binary operator | 二元操作符 |  | |
| binary search | 二分查找 | 二分搜索 | 二叉搜索 |
| binary search tree | 二叉搜索树 |  | |
| binary tree | 二叉树 |  | |
| binding | 绑定 |  | |
| binding vector | 绑定向量 |  | |
| bit | 位 | 比特 | |
| bit manipulation | 位操作 |  | |
| black box abstraction | 黑箱抽象 |  | |
| block | 块 | 区块 | |
| block structure | 块结构 | 区块结构 | |
| block name | 代码块名字 |  | |
| Blub paradox | Blub 困境 |  | |
| body | 体 | 主体 | |
| boilerplate | 公式化 | 样板 | |
| bookkeeping | 簿记 |  | |
| boolean | 布尔 |  | |
| border | 边框 |  | |
| bottom-up design | 自底向上的设计 |  | |
| bottom-up programming | 自底向上编程 |  | |
| bound | 边界 |  | |
| bounds checking | 边界检查 |  | |
| box notation | 箱子表示法 |  | |
| brace | 花括弧 | 花括号 | |
| bracket | 方括弧 | 方括号 | |
| branch | 分支 | 跳转 | |
| breadth-first | 广度优先 |  | |
| breadth-first search, BFS | 广度优先搜索 |  | |
| breakpoint | 断点 |  | |
| brevity | 简洁 |  | |
| buffer | 缓冲区 |  | |
| buffer overflow attack | 缓冲区溢出攻击 |  | |
| bug | 臭虫 |  | |
| building | 创建 |  | |
| built-in | 内置 |  | |
| byte | 字节 |  | |
| bytecode | 字节码 |  | |

### C

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| cache | 缓存 |  | |
| call | 调用 |  | |
| callback | 回调 |  | |
| CamelCase | 驼峰式大小写 |  | |
| candidate function | 候选函数 |  | |
| capture | 捕捉 |  | |
| case | 分支 |  | |
| character | 字符 |  | |
| checksum | 校验和 |  | |
| child class | 子类 |  | |
| choke point | 滞塞点 |  | |
| chunk | 块 |  | |
| circular definition | 循环定义 |  | |
| clarity | 清晰 |  | |
| class | 类 | 类别 | |
| class declaration | 类声明 |  | |
| class library | 类库 |  | |
| client | 客户 | 客户端 | |
| clipboard | 剪贴板 |  | |
| clone | 克隆 |  | |
| closed world assumption | 封闭世界假定 |  | |
| closure | 闭包 |  | |
| clutter | 杂乱 |  | |
| code | 代码 |  | |
| code bloat | 代码膨胀 |  | |
| collection | 收集器 | 复合类型 | |
| column | 行 | 栏 | |
| column-major order | 行主序 |  | |
| comma | 逗号 |  | |
| command-line | 命令行 |  | |
| command-line interface, CLI | 命令行界面 |  | |
| Common Lisp Object System, CLOS | Common Lisp 对象系统 |  | |
| Common Gateway Interface, CGI | 通用网关接口 |  | |
| compatible | 兼容 |  | |
| compilation | 编译 |  | |
| compilation parameter | 编译参数 |  | |
| compile | 编译 |  | |
| compile inline | 内联编译 |  | |
| compile time | 编译期 |  | |
| compiled form | 编译后的形式 |  | |
| compiler | 编译器 |  | |
| complex | 复杂 |  | |
| complexity | 复杂度 |  | |
| compliment | 补集 |  | |
| component | 组件 |  | |
| composability | 可组合性 |  | |
| composition | 组合 | 组合函数 | |
| compound value | 复合数据 | 复合值 | |
| compression | 压缩 |  | |
| computation | 计算 |  | |
| computer | 计算机 |  | |
| concatenation | 串接 |  | |
| concept | 概念 |  | |
| concrete | 具体 |  | |
| concurrency | 并发 |  | |
| concurrent | 并发 |  | |
| conditional | 条件式 |  | |
| conditional variable | 条件变量 |  | |
| configuration | 配置 |  | |
| connection | 连接 |  | |
| cons | 构造 |  | |
| cons cell | 构元 | cons 单元 | |
| consequent | 结果 | 推论 | |
| consistent | 一致性 |  | |
| constant | 常量 |  | |
| constraint | 约束 |  | |
| constraint programming | 约束式编程 |  | |
| container | 容器 |  | |
| content-based filtering | 基于内容的过滤 |  | |
| context | 上下文 | 语境 | 环境 |
| continuation | 延续性 |  | |
| continuous integration, CI | 持续集成 |  | |
| control | 控件 |  | |
| cooperative multitasking | 协作式多任务 |  | |
| copy | 拷贝 |  | |
| corollary | 推论 |  | |
| coroutine | 协程 |  | |
| corruption | 程序崩溃 |  | |
| crash | 崩溃 |  | |
| create | 创建 |  | |
| crystallize | 固化 |  | |
| curly | 括弧状的 |  | |
| curried | 柯里的 |  | |
| currying | 柯里化 |  | |
| cursor | 光标 |  | |
| curvy | 卷曲的 |  | |
| cycle | 周期 |  | |

### D

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| dangling pointer | 迷途指针 | 野指针 | |
| Defense Advanced Research Projects Agency, DARPA | 美国国防部高级研究计划局 |  | |
| data | 数据 |  | |
| data structure | 数据结构 |  | |
| data type | 数据类型 |  | |
| data-driven | 数据驱动 |  | |
| database | 数据库 |  | |
| database schema | 数据库模式 |  | |
| datagram | 数据报文 |  | |
| dead lock | 死锁 |  | |
| debug | 调试 |  | |
| debugger | 调试器 |  | |
| debugging | 调试 |  | |
| declaration | 声明 |  | |
| declaration forms | 声明形式 |  | |
| declarative | 声明式 | 说明式 | |
| declarative knowledge | 声明式知识 | 说明式知识 | |
| declarative programming | 声明式编程 | 说明式编程 | |
| declarativeness | 可声明性 |  | |
| declaring | 声明 |  | |
| deconstruction | 解构 |  | |
| deduction | 推导 | 推断 | |
| default | 缺省 | 默认 | |
| defer | 推迟 |  | |
| deficiency | 缺陷 | 不足 | |
| define | 定义 |  | |
| definition | 定义 |  | |
| delegate | 委托 |  | |
| dellocate | 释放 |  | |
| demarshal | 散集 |  | |
| deprecated | 废弃 |  | |
| depth-first | 深度优先 |  | |
| depth-first search, BFS | 深度优先搜索 |  | |
| derived | 派生 |  | |
| derived class | 派生类 |  | |
| design pattern | 设计模式 |  | |
| designator | 指示符 |  | |
| destructive | 破坏性的 |  | |
| destructive function | 破坏性函数 |  | |
| destructuring | 解构 |  | |
| device driver | 硬件驱动程序 |  | |
| dimensions | 维度 |  | |
| directive | 指令 |  | |
| directory | 目录 |  | |
| disk | 盘 |  | |
| dispatch | 分派 | 派发 | |
| distributed computing | 分布式计算 |  | |
| DLL hell | DLL 地狱 |  | |
| document | 文档 |  | |
| dotted list | 点状列表 |  | |
| dotted-pair notation | 带点尾部表示法 | 带点尾部记法 | |
| duplicate | 复本 |  | |
| dynamic binding | 动态绑定 |  | |
| dynamic extent | 动态范围 |  | |
| dynamic languages | 动态语言 |  | |
| dynamic scope | 动态作用域 |  | |
| dynamic type | 动态类型 |  | |

### E

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| effect | 效果 |  | |
| efficiency | 效率 |  | |
| efficient | 高效 |  | |
| embedded language | 嵌入式语言 |  | |
| emulate | 仿真 |  | |
| encapsulation | 封装 |  | |
| enum | 枚举 |  | |
| enumeration type | 枚举类型 |  | |
| enumrators | 枚举器 |  | |
| environment | 环境 |  | |
| equal | 相等 |  | |
| equality | 相等性 |  | |
| equation | 方程 |  | |
| equivalence | 等价性 |  | |
| error message | 错误信息 |  | |
| error-checking | 错误检查 |  | |
| escaped | 逃脱 | 溢出 | |
| escape character | 转义字符 |  | |
| evaluate | 求值 | 评估 | |
| evaluation | 求值 |  | |
| event | 事件 |  | |
| event driven | 事件驱动 |  | |
| exception | 异常 |  | |
| exception handling | 异常处理 |  | |
| exception specification | 异常规范 |  | |
| exit | 退出 |  | |
| expendable | 可扩展的 |  | |
| explicit | 显式 |  | |
| exploratory programming | 探索式编程 |  | |
| export | 导出 | 引出 | |
| expression | 表达式 |  | |
| expressive power | 表达能力 |  | |
| extensibility | 可扩展性 |  | |
| extent | 范围 | 程度 | |
| external representation | 外部表示法 |  | |
| extreme programming | 极限编程 |  | |

### F

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| factorial | 阶乘 |  | |
| family | （类型的）系 |  | |
| feasible | 可行的 |  | |
| feature | 特色 |  | |
| field | 字段 | 栏位 | |
| file | 文件 |  | |
| file handle | 文件句柄 |  | |
| fill pointer | 填充指针 |  | |
| fineo-grained | 细粒度 |  | |
| firmware | 固件 |  | |
| first-class | 第一类的 | 第一级的 | 一等的 |
| first-class function | 第一级函数 | 第一类函数 | 一等函数 |
| first-class object | 第一类的对象 | 第一级的对象 | 一等公民 |
| fixed-point | 不动点 |  | |
| fixnum | 定长数 | 定点数 | |
| flag | 标记 |  | |
| flash | 闪存 |  | |
| flexibility | 灵活性 |  | |
| floating-point | 浮点数 |  | |
| floating-point notation | 浮点数表示法 |  | |
| flush | 刷新 |  | |
| fold | 折叠 |  | |
| font | 字体 |  | |
| force | 迫使 |  | |
| form | 形式 |  | |
| form | 表单 |  | |
| formal parameter | 形参 |  | |
| formal relation | 形式关系 |  | |
| forward | 转发 |  | |
| fractal | 分形 |  | |
| fractions | 派系 |  | |
| framework | 框架 |  | |
| freeware | 自由软件 |  | |
| function | 函数 |  | |
| function literal | 函数字面常量 |  | |
| function object | 函数对象 |  | |
| functional arguments | 函数型参数 |  | |
| functional programming | 函数式编程 |  | |
| functionality | 功能性 |  | |

### G

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| game | 游戏 |  | |
| garbage | 垃圾 |  | |
| garbage collection | 垃圾回收 |  | |
| garbage collector | 垃圾回收器 |  | |
| generalized | 泛化 |  | |
| generalized variable | 广义变量 |  | |
| generate | 生成 |  | |
| generator | 生成器 |  | |
| generic | 通用的 | 泛化的 | |
| generic algorithm | 通用算法 | 泛型算法 | |
| generic function | 通用函数 |  | |
| generic programming | 通用编程 | 泛型编程 | |
| genrative programming | 生产式编程 |  | |
| global | 全局的 |  | |
| global declaration | 全局声明 |  | |
| glue program | 胶水程序 |  | |
| goto | 跳转 |  | |
| graphical user interface, GUI | 图形用户界面 |  | |
| greatest common divisor | 最大公因数 |  | |
| Greenspun's tenth rule | 格林斯潘第十定律 |  | |

### H

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| hack | 破解 |  | |
| hacker | 黑客 |  | |
| handle | 处理器 | 处理程序 | 句柄 |
| hard disk | 硬盘 |  | |
| hardware | 硬件 |  | |
| hash tables | 哈希表 | 散列表 | |
| header | 头部 |  | |
| header file | 头文件 |  | |
| heap | 堆 |  | |
| helper | 辅助函数 | 辅助方法 | |
| heuristic | 启发式 |  | |
| high-order | 高阶 |  | |
| higher-order function | 高阶函数 |  | |
| higher-order procedure | 高阶过程 |  | |
| hyperlink | 超链接 |  | |
| HyperText Markup Language, HTML | 超文本标记语言 |  | |
| HyperText Transfer Protocol, HTTP | 超文本传输协议 |  | |

### I

| **英文** | **译法 1** | 译法 2 | 译法 3 |
|---|---|---|---|
| identical | 一致 |  | |
| identifier | 标识符 |  | |
| identity | 同一性 |  | |
| ill type | 类型不正确 |  | |
| illusion | 错觉 |  | |
| imperative | 命令式 |  | |
| imperative programming | 命令式编程 |  | |
| implement | 实现 |  | |
| implementation | 实现 |  | |
| implicit | 隐式 |  | |
| import | 导入 |  | |
| incremental testing | 增量测试 |  | |
| indent | 缩排 | 缩进 | |
| indentation | 缩排 | 缩进 | |
| indented | 缩排 | 缩进 | |
| indention | 缩排 | 缩进 | |
| infer | 推导 |  | |
| infinite loop | 无限循环 |  | |
| infinite recursion | 无限递归 |  | |
| infinite precision | 无限精度 |  | |
| infix | 中序 |  | |
| information | 信息 |  | |
| information technology, IT | 信息技术 |  | |
| inheritance | 继承 |  | |
| initialization | 初始化 |  | |
| initialize | 初始化 |  | |
| inline | 内联 |  | |
| inline expansion | 内联展开 |  | |
| inner class | 内嵌类 |  | |
| inner loop | 内层循环 |  | |
| input | 输入 |  | |
| instances | 实例 |  | |
| instantiate | 实例化 |  | |
| instructive | 教学性的 |  | |
| instrument | 记录仪 |  | |
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

    print("解析词汇表...")
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
