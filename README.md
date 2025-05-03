# mcp-code-guidance

## 介绍
*mcp-code-guidance*是一个使用 Python 语言从 0 到 1 学习 MCP 与 A2A 协议的教程。
MCP(Model-Context Protocol,)和A2A(Agent-to-Agent)是大模型应用中两个重要的协议,分别侧重于智能体与外部工具的交互以及智能体之间的协作。

MCP 协议是一种用于模型与外部环境交互的协议,它允许模型通过 API 与外部环境进行通信,并获取外部环境的信息。MCP 协议的主要特点是:
+ **标准化**: 开发者只需遵循MCP标准，即可快速接入多种AI模型和服务；
+ **安全性**: 提供多层次的安全机制，包括数据加密、身份验证和权限控制等；
+ **灵活性**: 无论是数据库、文件还是 API，MCP 都能提供支持；
+ **跨平台**: MCP 适用于任何系统和编程语言（如Python、TypeScript、Go）

MCP（Model Context Protocol）提供了三种主要能力：Tool、Resource 和 Prompt
+ Tool
通过 Tool，LLM 可以直接调用暴露的函数，从而实现对功能的主动控制。例如，查询数据库、发送消息、调用 API 或执行特定逻辑的任务。
+ Resource
Resource 可用于为 LLM 提供上下文信息，帮助其更好地理解和响应用户需求。
+ Prompt
Prompt 是由服务器定义的可重用指令或者模板，用户可以通过选择提示词来引导或标准化与 LLM 的交互过程，使其更精确和标准化输出。

[官方地址: https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction)

## 项目结构

```
mcp-code-guidance/
├── LICENSE
├── README.md
├── README_ZH.md
├── mcp-server-01quickstart # 最简单 MCP 服务只包含 tools
├── mcp-server-02weather # 查询天气 MCP 服务
├── mcp-server-03stock # 查询股票 MCP 服务
├── my-project
└── tutorial #  MCP与A2A 开发教程
```

## 环境需要
+ python 3.10+
+ FastMCP

## 安装步骤

1.安装uv
+ 安装 uv 命令
```
 curl -LsSf https://astral.sh/uv/install.sh | sh
```

install.sh 脚本执行时从 github.com 下载 uv-aarch64-apple-darwin.tar.gz 文件并解压后再安装。众所周之 github.com 网络不稳定。这里提供一个简单的解决方法，手动下载到install.sh 后，再下载目录启动本地 python http 临时服务用于支持脚本下载文件，同时修改install.sh 脚本中的下载地址为本地服务地址。

```shell
python -m http.server 8181
```
调整后的shell 脚本可以参考: [修改后的uv-install.sh](./tutorial/uv-install.sh)

+ 添加用户本地bin目录到PATH
```shell
vi ~/.bash_profile
export PATH="$HOME/.local/bin:$PATH"
source ~/.bash_profile
```

2.**cd  mcp-code-guidance** 初始化项目，以mcp-server-01quickstart 为例


```shell
# Create a new directory for our project
uv init  mcp-server-01quickstart -p3.11 
cd mcp-server-01quickstart

# Create virtual environment and activate it
uv venv
source .venv/bin/activate

# Install dependencies
uv add "mcp[cli]" httpx

# Create our server file
touch mcp-server-01quickstart.py
```

## 贡献

+ 通过 UV 管理工具为每个功能创建独立的目录。目录名称使用小写字母，README.md文件用于说明项目的主要功能以及详细的安装步骤
+ "turorial/"目录下提供使用 Python 语言从 0 到 1 学习 MCP 与 A2A 协议的详细教程

## 开源许可

mcp-code-guidance 基于 [MIT License](LICENSE)  协议