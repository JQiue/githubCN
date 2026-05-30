#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
GitHub 自动翻译工具
功能：
1. 从可靠数据源获取英语单词（支持英式/美式拼写）
2. 自动翻译为中文
3. 去重后添加到 content.js 文件
4. 验证 JavaScript 语法正确性
"""

import json
import re
import time
import os
import sys
import argparse
from typing import Dict, List, Tuple, Set, Optional
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class WordFetcher:
    """从可靠数据源获取英语单词"""

    WORD_SOURCES = {
        "github_common": [
            "repository", "commit", "branch", "merge", "pull", "push", "fork",
            "clone", "star", "watch", "issue", "pull request", "code review",
            "workflow", "action", "pipeline", "deployment", "release", "tag",
            "markdown", "readme", "license", "gitignore", "dockerfile",
            "contributor", "maintainer", "collaborator", "organization",
            "dashboard", "insights", "settings", "appearance", "notification",
            "security", "analysis", "vulnerability", "secret", "dependabot",
            "environment", "variable", "secret", "runner", "cache", "artifact",
            "checkout", "matrix", "workflow_dispatch", "schedule", "cron",
            "milestone", "label", "assignee", "reviewer", "comment",
            "reaction", "emoji", "thread", "conversation", "mention",
            "wiki", "discussion", "project", "board", "sprint", "epic",
            "roadmap", "backlog", "kanban", "gantt", "timeline",
            "public", "private", "internal", "visibility", "permission",
            "admin", "write", "read", "triage", "maintain", "owner",
            "sso", "saml", "oauth", "ssh", "gpg", "2fa", "passkey",
            "webhook", "api", "graphql", "rest", "endpoint", "payload",
            "rate limit", "pagination", "cursor", "token", "scope",
            "github pages", "github actions", "github copilot", "github codespaces",
            "codespace", "devcontainer", "container", "registry", "package",
            "npm", "maven", "nuget", "rubygems", "docker", "container",
            "lfs", "large file storage", "submodule", "subtree",
            "conflict", "resolve", "rebase", "cherry-pick", "squash",
            "amend", "reset", "revert", "stash", "checkout",
            "fetch", "origin", "remote", "upstream", "downstream",
            "blame", "annotate", "diff", "patch", "compare",
            "raw", "blame", "history", "permalink", "line range",
            "snippet", "gist", "template", "boilerplate", "scaffold",
            "monorepo", "polyrepo", "microservice", "monolith",
            "semver", "versioning", "changelog", "breaking change",
            "deprecated", "sunset", "archive", "unarchive",
            "transfer", "ownership", "rename", "transfer",
            "sponsor", "sponsorship", "backer", "patron",
            "badge", "shield", "status", "check", "ci", "cd",
            "lint", "format", "test", "coverage", "quality",
            "sonarqube", "codeql", "static analysis", "dynamic analysis",
            "fuzzing", "penetration testing", "security audit",
            "cve", "cwe", "exploit", "patch", "hotfix",
            "feature flag", "a/b testing", "canary", "blue-green",
            "rollback", "rollout", "deployment strategy",
            "observability", "monitoring", "alerting", "logging",
            "metrics", "tracing", "opentelemetry", "slo", "sla",
            "incident", "postmortem", "root cause", "rca",
            "blameless", "retrospective", "standup", "sprint",
            "agile", "scrum", "kanban", "waterfall", "lean",
            "devops", "devsecops", "shift-left", "shift-right",
            "infrastructure as code", "terraform", "ansible",
            "kubernetes", "k8s", "pod", "node", "cluster",
            "serverless", "lambda", "cloud function", "edge",
            "cdn", "load balancer", "reverse proxy", "nginx",
            "ssl", "tls", "certificate", "domain", "dns",
            "cors", "csrf", "xss", "sql injection", "injection",
            "authentication", "authorization", "oauth2", "openid",
            "jwt", "session", "cookie", "local storage",
            "cache", "cdn", "etag", "last-modified", "expires",
            "compression", "gzip", "brotli", "minification",
            "bundler", "webpack", "vite", "rollup", "esbuild",
            "transpiler", "babel", "typescript", "swc",
            "polyfill", "shim", "fallback", "graceful degradation",
            "progressive enhancement", "responsive", "mobile-first",
            "accessibility", "a11y", "wcag", "aria", "semantic",
            "internationalization", "i18n", "localization", "l10n",
            "rtl", "ltr", "unicode", "utf-8", "encoding",
            "endianness", "big-endian", "little-endian",
            "serialization", "deserialization", "marshal", "unmarshal",
            "encoding", "decoding", "encryption", "decryption",
            "hashing", "checksum", "digest", "signature",
            "asymmetric", "symmetric", "public key", "private key",
            "certificate", "ca", "certificate authority",
            "hsts", "hpkp", "csp", "content security policy",
            "sri", "subresource integrity", "cors", "preflight",
            "websocket", "sse", "server-sent events", "long polling",
            "graphql", "rest", "grpc", "soap", "rpc",
            "api gateway", "service mesh", "sidecar", "ambassador",
            "circuit breaker", "retry", "backoff", "exponential",
            "idempotent", "atomic", "consistent", "available",
            "partition tolerance", "cap theorem", "acid", "base",
            "eventual consistency", "strong consistency",
            "cache invalidation", "cache stampede", "thundering herd",
            "race condition", "deadlock", "livelock", "starvation",
            "mutex", "semaphore", "lock", "spinlock",
            "concurrent", "parallel", "distributed", "decentralized",
            "centralized", "federated", "peer-to-peer", "p2p",
            "blockchain", "smart contract", "web3", "dapp",
            "machine learning", "ml", "ai", "neural network",
            "deep learning", "llm", "gpt", "transformer",
            "prompt", "context window", "token", "embedding",
            "vector database", "rag", "finetuning", "pretraining",
            "supervised", "unsupervised", "reinforcement learning",
            "overfitting", "underfitting", "generalization",
            "feature engineering", "hyperparameter", "epoch", "batch",
            "gradient descent", "backpropagation", "optimizer",
            "learning rate", "momentum", "adam", "sgd",
            "activation function", "relu", "sigmoid", "tanh",
            "softmax", "dropout", "batch normalization",
            "convolution", "pooling", "cnn", "rnn", "lstm", "gru",
            "attention", "self-attention", "multi-head attention",
            "transformer", "bert", "gpt", "llama", "mistral",
            "fine-tuning", "lora", "qlora", "prompt engineering",
            "chain-of-thought", "few-shot", "zero-shot",
            "agent", "autonomous agent", "multi-agent system",
            "tool use", "function calling", "retrieval augmented generation",
            "vector store", "embedding model", "semantic search",
            "hallucination", "grounding", "fact checking",
            "alignment", "rlhf", "constitutional ai",
            "red teaming", "adversarial testing", "prompt injection",
            "model card", "datasheet", "responsible ai", "ethical ai",
            "bias", "fairness", "transparency", "accountability",
            "explainability", "interpretability", "xai",
            "computer vision", "image recognition", "object detection",
            "semantic segmentation", "instance segmentation",
            "natural language processing", "nlp", "text generation",
            "text classification", "named entity recognition", "ner",
            "sentiment analysis", "topic modeling", "summarization",
            "translation", "transliteration", "localization",
            "speech recognition", "text-to-speech", "tts", "stt",
            "multimodal", "vision-language", "audio-visual",
        ],
        "british_american": [
            ("color", "colour"),
            ("center", "centre"),
            ("defense", "defence"),
            ("license", "licence"),
            ("organization", "organisation"),
            ("realize", "realise"),
            ("recognize", "recognise"),
            ("traveled", "travelled"),
            ("traveling", "travelling"),
            ("canceled", "cancelled"),
            ("canceling", "cancelling"),
            ("favorite", "favourite"),
            ("behavior", "behaviour"),
            ("flavor", "flavour"),
            ("honor", "honour"),
            ("humor", "humour"),
            ("labor", "labour"),
            ("neighbor", "neighbour"),
            ("apologize", "apologise"),
            ("customize", "customise"),
            ("optimize", "optimise"),
            ("specialize", "specialise"),
            ("analyze", "analyse"),
            ("catalog", "catalogue"),
            ("dialog", "dialogue"),
            ("draft", "draught"),
            ("gray", "grey"),
            ("inquire", "enquire"),
            ("inquiry", "enquiry"),
            ("jewelry", "jewellery"),
            ("judgment", "judgement"),
            ("kilogram", "kilogramme"),
            ("liter", "litre"),
            ("meter", "metre"),
            ("program", "programme"),
            ("sabotage", "sabotage"),
            ("savvy", "savvy"),
            ("theater", "theatre"),
            ("tire", "tyre"),
            ("toward", "towards"),
            ("whiskey", "whisky"),
            (" Wool ", " Wool "),
            ("artifact", "artefact"),
            ("check", "cheque"),
            ("curb", "kerb"),
            ("draft", "draught"),
            ("mold", "mould"),
            ("plow", "plough"),
            ("skeptic", "sceptic"),
            ("sulfur", "sulphur"),
        ]
    }

    def fetch_from_datamuse(self, limit: int = 1000) -> List[str]:
        """从 Datamuse API 获取常用单词"""
        words = []
        try:
            url = f"https://api.datamuse.com/words?max={limit}&sp=*"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()
            words = [item["word"] for item in data if "word" in item]
            print(f"从 Datamuse 获取到 {len(words)} 个单词")
        except Exception as e:
            print(f"Datamuse API 调用失败: {e}")
        return words

    def fetch_github_terms(self) -> List[str]:
        """获取 GitHub 相关术语"""
        return self.WORD_SOURCES.get("github_common", [])

    def fetch_british_american_pairs(self) -> List[Tuple[str, str]]:
        """获取英式-美式拼写对"""
        return self.WORD_SOURCES.get("british_american", [])

    def get_all_words(
        self,
        include_datamuse: bool = False,
        datamuse_limit: int = 100,
        include_github: bool = True,
        include_british_american: bool = True
    ) -> Set[str]:
        """获取所有单词（去重）"""
        all_words: Set[str] = set()

        if include_github:
            github_words = self.fetch_github_terms()
            all_words.update(github_words)
            print(f"添加了 {len(github_words)} 个 GitHub 相关术语")

        if include_british_american:
            ba_pairs = self.fetch_british_american_pairs()
            for us, uk in ba_pairs:
                all_words.add(us)
                all_words.add(uk)
            print(f"添加了 {len(ba_pairs) * 2} 个 英式/美式拼写对")

        if include_datamuse:
            datamuse_words = self.fetch_from_datamuse(datamuse_limit)
            all_words.update(datamuse_words)
            print(f"添加了 {len(datamuse_words)} 个 通用单词")

        return all_words


class Translator:
    """翻译模块 - 使用多个免费翻译 API 和本地词典"""

    LOCAL_DICTIONARY = {
        "repository": "仓库",
        "commit": "提交",
        "branch": "分支",
        "merge": "合并",
        "pull": "拉取",
        "push": "推送",
        "fork": "复刻",
        "clone": "克隆",
        "star": "星标",
        "watch": "关注",
        "issue": "问题",
        "pull request": "合并请求",
        "code review": "代码评审",
        "workflow": "工作流程",
        "action": "动作",
        "pipeline": "流水线",
        "deployment": "部署",
        "release": "发布",
        "tag": "标签",
        "markdown": "Markdown",
        "readme": "自述文件",
        "license": "许可证",
        "gitignore": "Git 忽略文件",
        "dockerfile": "Docker 配置文件",
        "contributor": "贡献者",
        "maintainer": "维护者",
        "collaborator": "合作者",
        "organization": "组织",
        "dashboard": "仪表盘",
        "insights": "统计",
        "settings": "设置",
        "appearance": "外观",
        "notification": "通知",
        "security": "安全",
        "analysis": "分析",
        "vulnerability": "漏洞",
        "secret": "密钥",
        "dependabot": "Dependabot",
        "environment": "环境",
        "variable": "变量",
        "runner": "运行器",
        "cache": "缓存",
        "artifact": "构件",
        "checkout": "检出",
        "matrix": "矩阵",
        "workflow_dispatch": "工作流调度",
        "schedule": "调度",
        "cron": "定时任务",
        "milestone": "里程碑",
        "label": "标签",
        "assignee": "经办人",
        "reviewer": "审查者",
        "comment": "评论",
        "reaction": "回应",
        "emoji": "表情",
        "thread": "线程",
        "conversation": "对话",
        "mention": "提及",
        "wiki": "维基",
        "discussion": "讨论",
        "project": "项目",
        "board": "看板",
        "sprint": "冲刺",
        "epic": "史诗",
        "roadmap": "路线图",
        "backlog": "待办事项",
        "kanban": "看板",
        "gantt": "甘特图",
        "timeline": "时间线",
        "public": "公开",
        "private": "私有",
        "internal": "内部",
        "visibility": "可见性",
        "permission": "权限",
        "admin": "管理员",
        "write": "写入",
        "read": "读取",
        "triage": "分类",
        "maintain": "维护",
        "owner": "所有者",
        "sso": "单点登录",
        "saml": "安全断言标记语言",
        "oauth": "开放授权",
        "ssh": "安全外壳协议",
        "gpg": "GNU 隐私卫士",
        "2fa": "双因素认证",
        "passkey": "通行密钥",
        "webhook": "Webhook",
        "api": "应用程序接口",
        "graphql": "GraphQL",
        "rest": "REST",
        "endpoint": "端点",
        "payload": "负载",
        "rate limit": "速率限制",
        "pagination": "分页",
        "cursor": "游标",
        "token": "令牌",
        "scope": "范围",
        "github pages": "GitHub Pages",
        "github actions": "GitHub Actions",
        "github copilot": "GitHub Copilot",
        "github codespaces": "GitHub Codespaces",
        "codespace": "云端开发环境",
        "devcontainer": "开发容器",
        "container": "容器",
        "registry": "注册表",
        "package": "包",
        "npm": "Node.js 包管理器",
        "maven": "Maven",
        "nuget": "NuGet",
        "rubygems": "RubyGems",
        "docker": "Docker",
        "lfs": "大文件存储",
        "large file storage": "大文件存储",
        "submodule": "子模块",
        "subtree": "子树",
        "conflict": "冲突",
        "resolve": "解决",
        "rebase": "变基",
        "cherry-pick": "遴选",
        "squash": "压缩",
        "amend": "修正",
        "reset": "重置",
        "revert": "还原",
        "stash": "暂存",
        "fetch": "获取",
        "origin": "源",
        "remote": "远程",
        "upstream": "上游",
        "downstream": "下游",
        "blame": "追溯",
        "annotate": "注解",
        "diff": "差异",
        "patch": "补丁",
        "compare": "比较",
        "raw": "原始",
        "history": "历史",
        "permalink": "永久链接",
        "line range": "行范围",
        "snippet": "代码片段",
        "gist": "Gist",
        "template": "模板",
        "boilerplate": "样板代码",
        "scaffold": "脚手架",
        "monorepo": "单体仓库",
        "polyrepo": "多仓库",
        "microservice": "微服务",
        "monolith": "单体应用",
        "semver": "语义化版本",
        "versioning": "版本控制",
        "changelog": "变更日志",
        "breaking change": "破坏性变更",
        "deprecated": "已弃用",
        "sunset": "终止",
        "archive": "归档",
        "unarchive": "取消归档",
        "transfer": "转移",
        "ownership": "所有权",
        "rename": "重命名",
        "sponsor": "赞助",
        "sponsorship": "赞助",
        "backer": "支持者",
        "patron": "赞助人",
        "badge": "徽章",
        "shield": "护盾",
        "status": "状态",
        "check": "检查",
        "ci": "持续集成",
        "cd": "持续部署",
        "lint": "代码检查",
        "format": "格式化",
        "test": "测试",
        "coverage": "覆盖率",
        "quality": "质量",
        "sonarqube": "SonarQube",
        "codeql": "CodeQL",
        "static analysis": "静态分析",
        "dynamic analysis": "动态分析",
        "fuzzing": "模糊测试",
        "penetration testing": "渗透测试",
        "security audit": "安全审计",
        "cve": "通用漏洞披露",
        "cwe": "通用弱点枚举",
        "exploit": "漏洞利用",
        "patch": "补丁",
        "hotfix": "热修复",
        "feature flag": "功能开关",
        "a/b testing": "A/B 测试",
        "canary": "金丝雀发布",
        "blue-green": "蓝绿部署",
        "rollback": "回滚",
        "rollout": "推出",
        "deployment strategy": "部署策略",
        "observability": "可观测性",
        "monitoring": "监控",
        "alerting": "告警",
        "logging": "日志",
        "metrics": "指标",
        "tracing": "链路追踪",
        "opentelemetry": "OpenTelemetry",
        "slo": "服务水平目标",
        "sla": "服务水平协议",
        "incident": "事件",
        "postmortem": "事后复盘",
        "root cause": "根本原因",
        "rca": "根本原因分析",
        "blameless": "无指责",
        "retrospective": "回顾",
        "standup": "站会",
        "agile": "敏捷",
        "scrum": "Scrum",
        "waterfall": "瀑布模型",
        "lean": "精益",
        "devops": "开发运维一体化",
        "devsecops": "开发安全运维一体化",
        "shift-left": "左移",
        "shift-right": "右移",
        "infrastructure as code": "基础设施即代码",
        "terraform": "Terraform",
        "ansible": "Ansible",
        "kubernetes": "Kubernetes",
        "k8s": "K8s",
        "pod": "Pod",
        "node": "节点",
        "cluster": "集群",
        "serverless": "无服务器",
        "lambda": "Lambda",
        "cloud function": "云函数",
        "edge": "边缘",
        "cdn": "内容分发网络",
        "load balancer": "负载均衡器",
        "reverse proxy": "反向代理",
        "nginx": "Nginx",
        "ssl": "安全套接层",
        "tls": "传输层安全",
        "certificate": "证书",
        "domain": "域名",
        "dns": "域名系统",
        "cors": "跨域资源共享",
        "csrf": "跨站请求伪造",
        "xss": "跨站脚本",
        "sql injection": "SQL 注入",
        "injection": "注入",
        "authentication": "认证",
        "authorization": "授权",
        "oauth2": "OAuth 2.0",
        "openid": "OpenID",
        "jwt": "JSON Web 令牌",
        "session": "会话",
        "cookie": "Cookie",
        "local storage": "本地存储",
        "etag": "ETag",
        "last-modified": "最后修改",
        "expires": "过期",
        "compression": "压缩",
        "gzip": "Gzip",
        "brotli": "Brotli",
        "minification": "压缩",
        "bundler": "打包工具",
        "webpack": "Webpack",
        "vite": "Vite",
        "rollup": "Rollup",
        "esbuild": "esbuild",
        "transpiler": "转译器",
        "babel": "Babel",
        "typescript": "TypeScript",
        "swc": "SWC",
        "polyfill": "Polyfill",
        "shim": "垫片",
        "fallback": "降级",
        "graceful degradation": "优雅降级",
        "progressive enhancement": "渐进增强",
        "responsive": "响应式",
        "mobile-first": "移动优先",
        "accessibility": "无障碍",
        "a11y": "无障碍",
        "wcag": "网页内容无障碍指南",
        "aria": "无障碍富互联网应用",
        "semantic": "语义化",
        "internationalization": "国际化",
        "i18n": "国际化",
        "localization": "本地化",
        "l10n": "本地化",
        "rtl": "从右到左",
        "ltr": "从左到右",
        "unicode": "Unicode",
        "utf-8": "UTF-8",
        "encoding": "编码",
        "decoding": "解码",
        "endianness": "字节序",
        "big-endian": "大端",
        "little-endian": "小端",
        "serialization": "序列化",
        "deserialization": "反序列化",
        "marshal": "编组",
        "unmarshal": "解组",
        "encryption": "加密",
        "decryption": "解密",
        "hashing": "哈希",
        "checksum": "校验和",
        "digest": "摘要",
        "signature": "签名",
        "asymmetric": "非对称",
        "symmetric": "对称",
        "public key": "公钥",
        "private key": "私钥",
        "ca": "证书颁发机构",
        "certificate authority": "证书颁发机构",
        "hsts": "HTTP 严格传输安全",
        "hpkp": "HTTP 公钥固定",
        "csp": "内容安全策略",
        "content security policy": "内容安全策略",
        "sri": "子资源完整性",
        "subresource integrity": "子资源完整性",
        "preflight": "预检",
        "websocket": "WebSocket",
        "sse": "服务器发送事件",
        "server-sent events": "服务器发送事件",
        "long polling": "长轮询",
        "grpc": "gRPC",
        "soap": "SOAP",
        "rpc": "远程过程调用",
        "api gateway": "API 网关",
        "service mesh": "服务网格",
        "sidecar": "边车",
        "ambassador": "大使",
        "circuit breaker": "断路器",
        "retry": "重试",
        "backoff": "退避",
        "exponential": "指数",
        "idempotent": "幂等",
        "atomic": "原子",
        "consistent": "一致",
        "available": "可用",
        "partition tolerance": "分区容错",
        "cap theorem": "CAP 定理",
        "acid": "ACID",
        "base": "BASE",
        "eventual consistency": "最终一致性",
        "strong consistency": "强一致性",
        "cache invalidation": "缓存失效",
        "cache stampede": "缓存惊群",
        "thundering herd": "惊群效应",
        "race condition": "竞态条件",
        "deadlock": "死锁",
        "livelock": "活锁",
        "starvation": "饥饿",
        "mutex": "互斥锁",
        "semaphore": "信号量",
        "lock": "锁",
        "spinlock": "自旋锁",
        "concurrent": "并发",
        "parallel": "并行",
        "distributed": "分布式",
        "decentralized": "去中心化",
        "centralized": "中心化",
        "federated": "联邦",
        "peer-to-peer": "点对点",
        "p2p": "点对点",
        "blockchain": "区块链",
        "smart contract": "智能合约",
        "web3": "Web3",
        "dapp": "去中心化应用",
        "machine learning": "机器学习",
        "ml": "机器学习",
        "ai": "人工智能",
        "neural network": "神经网络",
        "deep learning": "深度学习",
        "llm": "大语言模型",
        "gpt": "生成式预训练Transformer",
        "transformer": "Transformer",
        "prompt": "提示词",
        "context window": "上下文窗口",
        "token": "令牌",
        "embedding": "嵌入",
        "vector database": "向量数据库",
        "rag": "检索增强生成",
        "finetuning": "微调",
        "pretraining": "预训练",
        "supervised": "有监督",
        "unsupervised": "无监督",
        "reinforcement learning": "强化学习",
        "overfitting": "过拟合",
        "underfitting": "欠拟合",
        "generalization": "泛化",
        "feature engineering": "特征工程",
        "hyperparameter": "超参数",
        "epoch": "轮次",
        "batch": "批次",
        "gradient descent": "梯度下降",
        "backpropagation": "反向传播",
        "optimizer": "优化器",
        "learning rate": "学习率",
        "momentum": "动量",
        "adam": "Adam",
        "sgd": "随机梯度下降",
        "activation function": "激活函数",
        "relu": "ReLU",
        "sigmoid": "Sigmoid",
        "tanh": "Tanh",
        "softmax": "Softmax",
        "dropout": "Dropout",
        "batch normalization": "批归一化",
        "convolution": "卷积",
        "pooling": "池化",
        "cnn": "卷积神经网络",
        "rnn": "循环神经网络",
        "lstm": "长短期记忆网络",
        "gru": "门控循环单元",
        "attention": "注意力",
        "self-attention": "自注意力",
        "multi-head attention": "多头注意力",
        "bert": "BERT",
        "llama": "Llama",
        "mistral": "Mistral",
        "fine-tuning": "微调",
        "lora": "LoRA",
        "qlora": "QLoRA",
        "prompt engineering": "提示词工程",
        "chain-of-thought": "思维链",
        "few-shot": "少样本",
        "zero-shot": "零样本",
        "agent": "智能体",
        "autonomous agent": "自主智能体",
        "multi-agent system": "多智能体系统",
        "tool use": "工具使用",
        "function calling": "函数调用",
        "retrieval augmented generation": "检索增强生成",
        "vector store": "向量存储",
        "embedding model": "嵌入模型",
        "semantic search": "语义搜索",
        "hallucination": "幻觉",
        "grounding": "接地",
        "fact checking": "事实核查",
        "alignment": "对齐",
        "rlhf": "基于人类反馈的强化学习",
        "constitutional ai": "宪法 AI",
        "red teaming": "红队测试",
        "adversarial testing": "对抗测试",
        "prompt injection": "提示词注入",
        "model card": "模型卡片",
        "datasheet": "数据表",
        "responsible ai": "负责任 AI",
        "ethical ai": "伦理 AI",
        "bias": "偏见",
        "fairness": "公平",
        "transparency": "透明",
        "accountability": "问责",
        "explainability": "可解释性",
        "interpretability": "可理解性",
        "xai": "可解释 AI",
        "computer vision": "计算机视觉",
        "image recognition": "图像识别",
        "object detection": "目标检测",
        "semantic segmentation": "语义分割",
        "instance segmentation": "实例分割",
        "natural language processing": "自然语言处理",
        "nlp": "自然语言处理",
        "text generation": "文本生成",
        "text classification": "文本分类",
        "named entity recognition": "命名实体识别",
        "ner": "命名实体识别",
        "sentiment analysis": "情感分析",
        "topic modeling": "主题建模",
        "summarization": "摘要",
        "translation": "翻译",
        "transliteration": "音译",
        "speech recognition": "语音识别",
        "text-to-speech": "文本转语音",
        "tts": "文本转语音",
        "stt": "语音转文本",
        "multimodal": "多模态",
        "vision-language": "视觉-语言",
        "audio-visual": "音视频",
        "color": "颜色",
        "colour": "颜色",
        "center": "中心",
        "centre": "中心",
        "defense": "防御",
        "defence": "防御",
        "license": "许可证",
        "licence": "许可证",
        "organization": "组织",
        "organisation": "组织",
        "realize": "实现",
        "realise": "实现",
        "recognize": "识别",
        "recognise": "识别",
        "traveled": "旅行过的",
        "travelled": "旅行过的",
        "traveling": "旅行的",
        "travelling": "旅行的",
        "canceled": "已取消",
        "cancelled": "已取消",
        "canceling": "取消中",
        "cancelling": "取消中",
        "favorite": "最喜欢的",
        "favourite": "最喜欢的",
        "behavior": "行为",
        "behaviour": "行为",
        "flavor": "风味",
        "flavour": "风味",
        "honor": "荣誉",
        "honour": "荣誉",
        "humor": "幽默",
        "humour": "幽默",
        "labor": "劳动",
        "labour": "劳动",
        "neighbor": "邻居",
        "neighbour": "邻居",
        "apologize": "道歉",
        "apologise": "道歉",
        "customize": "自定义",
        "customise": "自定义",
        "optimize": "优化",
        "optimise": "优化",
        "specialize": "专业化",
        "specialise": "专业化",
        "analyze": "分析",
        "analyse": "分析",
        "catalog": "目录",
        "catalogue": "目录",
        "dialog": "对话框",
        "dialogue": "对话",
        "draft": "草稿",
        "draught": "草稿",
        "gray": "灰色",
        "grey": "灰色",
        "inquire": "询问",
        "enquire": "询问",
        "inquiry": "查询",
        "enquiry": "查询",
        "jewelry": "珠宝",
        "jewellery": "珠宝",
        "judgment": "判断",
        "judgement": "判断",
        "kilogram": "千克",
        "kilogramme": "千克",
        "liter": "升",
        "litre": "升",
        "meter": "米",
        "metre": "米",
        "program": "程序",
        "programme": "节目",
        "theater": "剧院",
        "theatre": "剧院",
        "tire": "轮胎",
        "tyre": "轮胎",
        "toward": "朝向",
        "towards": "朝向",
        "whiskey": "威士忌",
        "whisky": "威士忌",
        "artifact": "人工制品",
        "artefact": "人工制品",
        "check": "检查",
        "cheque": "支票",
        "curb": "路边",
        "kerb": "路边",
        "mold": "模具",
        "mould": "模具",
        "plow": "犁",
        "plough": "犁",
        "skeptic": "怀疑论者",
        "sceptic": "怀疑论者",
        "sulfur": "硫",
        "sulphur": "硫",
        "sabotage": "破坏",
        "savvy": "精明的",
        "artifact": "构件",
        "artefact": "构件",
        "continuous integration": "持续集成",
        "continuous deployment": "持续部署",
        "code quality": "代码质量",
        "test coverage": "测试覆盖率",
        "unit test": "单元测试",
        "integration test": "集成测试",
        "end-to-end test": "端到端测试",
        "e2e test": "端到端测试",
        "smoke test": "冒烟测试",
        "regression test": "回归测试",
        "performance test": "性能测试",
        "load test": "负载测试",
        "stress test": "压力测试",
        "security test": "安全测试",
        "user acceptance test": "用户验收测试",
        "uat": "用户验收测试",
        "bug fix": "修复 bug",
        "hot fix": "热修复",
        "cold fix": "冷修复",
        "feature branch": "功能分支",
        "release branch": "发布分支",
        "hotfix branch": "热修复分支",
        "main branch": "主分支",
        "master branch": "主分支",
        "develop branch": "开发分支",
        "trunk-based development": "基于主干的开发",
        "git flow": "Git 工作流",
        "github flow": "GitHub 工作流",
        "trunk": "主干",
        "merge conflict": "合并冲突",
        "merge queue": "合并队列",
        "squash merge": "压缩合并",
        "rebase merge": "变基合并",
        "fast-forward": "快进",
        "three-way merge": "三方合并",
    }

    def __init__(self, cache_file: str = "translation_cache.json"):
        self.cache_file = cache_file
        self.cache: Dict[str, str] = self._load_cache()
        self.rate_limit_delay = 0.5
        self.session = self._create_session()

    def _create_session(self) -> requests.Session:
        """创建带有重试机制的会话"""
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        session.verify = False
        requests.packages.urllib3.disable_warnings()
        return session

    def _load_cache(self) -> Dict[str, str]:
        """加载翻译缓存"""
        if os.path.exists(self.cache_file):
            try:
                with open(self.cache_file, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception as e:
                print(f"加载缓存失败: {e}")
        return {}

    def _save_cache(self) -> None:
        """保存翻译缓存"""
        try:
            with open(self.cache_file, "w", encoding="utf-8") as f:
                json.dump(self.cache, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"保存缓存失败: {e}")

    def translate_local(self, text: str) -> Optional[str]:
        """使用本地词典翻译"""
        text_lower = text.lower().strip()
        return self.LOCAL_DICTIONARY.get(text_lower)

    def translate_mymemory(self, text: str, source: str = "en", target: str = "zh-CN") -> Optional[str]:
        """使用 MyMemory API 翻译"""
        try:
            url = "https://api.mymemory.translated.net/get"
            params = {
                "q": text,
                "langpair": f"{source}|{target}"
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            translation = data.get("responseData", {}).get("translatedText")
            if translation and translation != text:
                return translation
        except Exception as e:
            print(f"MyMemory 翻译失败: {e}")
        return None

    def translate_google_free(self, text: str, source: str = "en", target: str = "zh-CN") -> Optional[str]:
        """使用 Google 免费翻译端点"""
        try:
            url = "https://translate.googleapis.com/translate_a/single"
            params = {
                "client": "gtx",
                "sl": source,
                "tl": target,
                "dt": "t",
                "q": text
            }
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            if data and data[0]:
                translations = [item[0] for item in data[0] if item[0]]
                return " ".join(translations)
        except Exception as e:
            print(f"Google 翻译失败: {e}")
        return None

    def translate(self, text: str, source: str = "en", target: str = "zh-CN") -> Optional[str]:
        """翻译文本（优先使用缓存和本地词典）"""
        text = text.strip()
        if not text:
            return None

        cache_key = f"{source}:{target}:{text}"
        if cache_key in self.cache:
            return self.cache[cache_key]

        local_translation = self.translate_local(text)
        if local_translation:
            self.cache[cache_key] = local_translation
            self._save_cache()
            return local_translation

        translation = None

        translation = self.translate_google_free(text, source, target)
        time.sleep(self.rate_limit_delay)

        if not translation:
            translation = self.translate_mymemory(text, source, target)
            time.sleep(self.rate_limit_delay)

        if translation:
            self.cache[cache_key] = translation
            self._save_cache()

        return translation

    def translate_batch(self, words: List[str], source: str = "en", target: str = "zh-CN") -> Dict[str, str]:
        """批量翻译单词"""
        results: Dict[str, str] = {}
        total = len(words)
        for i, word in enumerate(words, 1):
            print(f"翻译中 ({i}/{total}): {word}", end="\r")
            translation = self.translate(word, source, target)
            if translation:
                results[word] = translation
            else:
                print(f"\n警告: 无法翻译 '{word}'")
        print(f"\n翻译完成，成功 {len(results)}/{total} 个")
        return results


class ContentJSManager:
    """管理 content.js 文件的读写"""

    def __init__(self, content_js_path: str):
        self.path = Path(content_js_path)
        if not self.path.exists():
            raise FileNotFoundError(f"找不到文件: {content_js_path}")

    def parse_existing_translations(self) -> Dict[str, str]:
        """解析 content.js 中已有的翻译"""
        content = self.path.read_text(encoding="utf-8")
        translations: Dict[str, str] = {}

        pattern = r'\[\s*`([^`]*)`\s*,\s*`([^`]*)`\s*\]'
        matches = re.findall(pattern, content)

        for english, chinese in matches:
            english = english.strip()
            chinese = chinese.strip()
            if english and english not in translations:
                translations[english] = chinese

        print(f"解析到 {len(translations)} 条现有翻译")
        return translations

    def _escape_js_string(self, s: str) -> str:
        """转义 JavaScript 字符串"""
        return s.replace("\\", "\\\\").replace("`", "\\`").replace("$", "\\$")

    def append_translations(self, new_translations: Dict[str, str]) -> int:
        """追加新翻译到 content.js"""
        existing = self.parse_existing_translations()

        to_add: List[Tuple[str, str]] = []
        for english, chinese in new_translations.items():
            english = english.strip()
            chinese = chinese.strip()
            if english and chinese and english not in existing:
                to_add.append((english, chinese))

        if not to_add:
            print("没有需要添加的新翻译")
            return 0

        content = self.path.read_text(encoding="utf-8")

        pattern = r'(\s*\][,;]?\s*$)'
        match = re.search(pattern, content, re.MULTILINE)

        if not match:
            raise ValueError("无法找到数组结束位置")

        new_entries = ""
        for english, chinese in to_add:
            eng_escaped = self._escape_js_string(english)
            zh_escaped = self._escape_js_string(chinese)
            if " " in english or len(english.split()) > 1 or "’" in english or "—" in english:
                new_entries += f"  [`{eng_escaped}`, `{zh_escaped}`],\n"
            else:
                new_entries += f"  [`{eng_escaped}`, `{zh_escaped}`],\n"

        insert_pos = match.start()
        new_content = content[:insert_pos] + ",\n" + new_entries + content[insert_pos:]

        self.path.write_text(new_content, encoding="utf-8")
        print(f"成功添加 {len(to_add)} 条新翻译")
        return len(to_add)

    def validate_syntax(self) -> bool:
        """验证 JavaScript 语法"""
        try:
            import subprocess
            result = subprocess.run(
                ["node", "--check", str(self.path)],
                capture_output=True,
                text=True,
                timeout=10
            )
            if result.returncode == 0:
                print("OK: JavaScript syntax validation passed")
                return True
            else:
                print(f"ERROR: JavaScript syntax error: {result.stderr}")
                return False
        except FileNotFoundError:
            print("Warning: Node.js not found, skipping syntax validation")
            content = self.path.read_text(encoding="utf-8")
            open_brackets = content.count("[")
            close_brackets = content.count("]")
            backticks = content.count("`")
            print(f"Basic syntax check: [ {open_brackets}, ] {close_brackets}, ` {backticks}")
            if open_brackets == close_brackets and backticks % 2 == 0:
                print("OK: Basic syntax check passed")
                return True
            else:
                print("ERROR: Basic syntax check failed")
                return False
        except Exception as e:
            print(f"❌ 语法验证失败: {e}")
            return False

    def sort_translations(self) -> None:
        """对翻译进行排序（可选）"""
        content = self.path.read_text(encoding="utf-8")

        pattern = r'(const allData = \[)(.*?)(\];)'
        match = re.search(pattern, content, re.DOTALL)

        if not match:
            print("无法找到 allData 数组")
            return

        array_content = match.group(2)
        entry_pattern = r'\s*\[\s*`([^`]*)`\s*,\s*`([^`]*)`\s*\],?'
        entries = re.findall(entry_pattern, array_content)

        seen = set()
        unique_entries = []
        for eng, zh in entries:
            if eng not in seen:
                seen.add(eng)
                unique_entries.append((eng, zh))

        unique_entries.sort(key=lambda x: x[0].lower())

        new_array_content = "\n"
        for eng, zh in unique_entries:
            eng_escaped = self._escape_js_string(eng)
            zh_escaped = self._escape_js_string(zh)
            new_array_content += f"  [`{eng_escaped}`, `{zh_escaped}`],\n"

        new_content = match.group(1) + new_array_content + match.group(3) + content[match.end():]

        self.path.write_text(new_content, encoding="utf-8")
        print(f"已排序，共 {len(unique_entries)} 条翻译")


def main():
    parser = argparse.ArgumentParser(description="GitHub 自动翻译工具")
    parser.add_argument("--content-js", default="src/js/content.js", help="content.js 文件路径")
    parser.add_argument("--datamuse", action="store_true", help="是否从 Datamuse 获取通用单词")
    parser.add_argument("--datamuse-limit", type=int, default=100, help="Datamuse 获取单词数量")
    parser.add_argument("--no-github", action="store_true", help="不包含 GitHub 相关术语")
    parser.add_argument("--no-ba", action="store_true", help="不包含英式/美式拼写对")
    parser.add_argument("--dry-run", action="store_true", help="只显示将要添加的翻译，不写入文件")
    parser.add_argument("--sort", action="store_true", help="对现有翻译进行排序")
    parser.add_argument("--validate-only", action="store_true", help="仅验证语法")
    parser.add_argument("--custom-words", nargs="*", help="自定义要翻译的单词列表")
    parser.add_argument("--cache-file", default="translation_cache.json", help="翻译缓存文件路径")
    parser.add_argument("--yes", "-y", action="store_true", help="跳过确认提示，自动执行")

    args = parser.parse_args()

    content_js_path = Path(args.content_js)
    if not content_js_path.is_absolute():
        content_js_path = Path.cwd() / content_js_path

    manager = ContentJSManager(str(content_js_path))

    if args.validate_only:
        manager.validate_syntax()
        return

    if args.sort:
        manager.sort_translations()
        manager.validate_syntax()
        return

    print("=" * 60)
    print("GitHub 自动翻译工具")
    print("=" * 60)

    fetcher = WordFetcher()
    translator = Translator(cache_file=args.cache_file)

    words_to_translate: Set[str] = set()

    if args.custom_words:
        words_to_translate.update(args.custom_words)
        print(f"添加了 {len(args.custom_words)} 个自定义单词")
    else:
        words_to_translate = fetcher.get_all_words(
            include_datamuse=args.datamuse,
            datamuse_limit=args.datamuse_limit,
            include_github=not args.no_github,
            include_british_american=not args.no_ba
        )

    existing = manager.parse_existing_translations()
    new_words = [w for w in words_to_translate if w not in existing]

    print(f"\n总单词数: {len(words_to_translate)}")
    print(f"已有翻译: {len(words_to_translate) - len(new_words)}")
    print(f"需要翻译: {len(new_words)}")

    if not new_words:
        print("\n没有需要翻译的新单词！")
        return

    if not args.yes:
        confirm = input(f"\n是否开始翻译 {len(new_words)} 个单词？(y/n): ").lower()
        if confirm != "y":
            print("已取消")
            return
    else:
        print(f"\n自动确认翻译 {len(new_words)} 个单词")

    print("\n开始翻译...")
    translations = translator.translate_batch(new_words)

    if args.dry_run:
        print("\n=== 预览（不写入文件）===")
        for eng, zh in sorted(translations.items()):
            print(f"  [`{eng}`, `{zh}`],")
        print(f"\n共 {len(translations)} 条翻译将被添加")
        return

    added = manager.append_translations(translations)

    if added > 0:
        manager.validate_syntax()

    print("\n" + "=" * 60)
    print(f"任务完成！添加了 {added} 条新翻译")
    print("=" * 60)


if __name__ == "__main__":
    main()
