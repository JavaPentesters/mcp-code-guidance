# mcp-code-guidance

#### 介绍
这是一个使用Python 语言从0到1学习MCP Server的编码教程，同时也会学习 Python 语言编程基础。

#### 项目结构
mcp-code-guidance/
├── mcp-server-quickstart01/        # 最简单 MCP 服务只包含 tools
├── tutorial/           # 从 0 到 1 的 MCP 开发教程
└── ...                 # 其他 MCP 服务

#### 安装教程

1.  安装uv
+ 下载 uv-aarch64-apple-darwin.tar.gz
启动本地 python 服务，用于下载
```
python -m http.server 8181
```

2.  添加用户本地bin目录到PATH
```
vi ~/.bash_profile
export PATH="$HOME/.local/bin:$PATH"
source ~/.bash_profile
```

3.  创建虚拟环境
```
 uv venv --python /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
```

