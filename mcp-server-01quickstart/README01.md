# Quick Start

## 环境准备
1. 创建项目
```
cd mcp-server-quickstart01
uv init -p3.11 
```

2. 创建虚拟环境
```
uv venv02 --python /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
```

3. 激活虚拟环境
```
source .venv/bin/activate  # Linux/MacOS环境
.venv\Scripts\activate     # Windows环境
```

4. 安装依赖
```
uv add "mcp[cli]" httpx --index-url "https://pypi.tuna.tsinghua.edu.cn/simple/"
uv pip install --python=3.11 "mcp[cli]" httpx --index-url "https://pypi.tuna.tsinghua.edu.cn/simple/"

```
使用默认pipy镜像源可能会由于网速原因无法成功下载安装。此步骤设置为清华镜像源 https://pypi.python.org/simple。


5. 运行服务
```
mcp dev main.py
```

## 快速构建一个提供Tools、Resources、Prompts最简单的MCP服务
快速构建一个简单的MCP服务，以便在客户端（Cursor、Trae 等）中使用。

+ MCP 服务可以提供三种主要类型的功能：
>Resources：客户端可以读取的类似文件的数据（如 API 响应或文件内容）
>Tools：LLM 可以调用的函数
>Prompts：帮助用户完成特定任务的预先编写的模板


构建 MCP 服务
```
mcp: FastMCP = FastMCP(
    name="这是FastMCP的参数name",
    instructions="""
    这是FastMCP的参数instructions.
    """
)
```

官方文档使用 @mcp.tool() 装饰器定义 Tools，使用@mcp.resource() 定义 Resources，使用 @mcp.prompt() 定义 Prompts。

参考:[python sdk](https://github.com/modelcontextprotocol/python-sdk)


