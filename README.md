# mcp-code-guidance

### 介绍
*mcp-code-guidance*是一个使用 Python 语言从 0 到 1 学习 MCP 与 A2A 协议的教程。
MCP(Model-Context Protocol,)和A2A(Agent-to-Agent)是大模型应用中两个重要的协议,分别侧重于智能体与外部工具的交互以及智能体之间的协作。

MCP 协议是一种用于模型与外部环境交互的协议,它允许模型通过 API 与外部环境进行通信,并获取外部环境的信息。MCP 协议的主要特点是:
+ 支持多种外部环境,包括文本、图像、音频等。
+ 支持多种模型,包括大模型、小模型等。

[https://modelcontextprotocol.io/introduction](https://modelcontextprotocol.io/introduction
)

## 项目结构

```
mcp-code-guidance/
├── LICENSE
├── README.en.md
├── README.md
├── mcp-server-01quickstart # 最简单 MCP 服务只包含 tools
├── mcp-server-02weather # 查询天气 MCP 服务
├── mcp-server-03stock # 查询股票 MCP 服务
├── my-project
└── tutorial #  MCP与A2A 开发教程
```

## 环境要求
+ python 3.10+


## 安装步骤

1.安装uv
+ 安装 uv 命令
```
 curl -LsSf https://astral.sh/uv/install.sh | sh
```

install.sh 脚本执行时会从 github.com 下载 uv-aarch64-apple-darwin.tar.gz 并解压后然后再安装。github.com 网络不稳定，可以手动下载。这里提供一个技巧，可下载目录启动本地 python http 临时服务用于支持脚本下载文件，同时修改install.sh 脚本中的下载地址为本地服务地址。

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


