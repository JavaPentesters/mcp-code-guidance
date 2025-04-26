# mcp-code-guidance

#### 介绍
这是一个使用Python 语言从0到1学习MCP Server的编码教程，同时也会学习 Python 语言编程基础。

#### 项目结构
>mcp-code-guidance/
>├── mcp-server-quickstart01/        # 最简单 MCP 服务只包含 tools
>├── tutorial/           # 从 0 到 1 的 MCP 开发教程
>└── ...                 # 其他 MCP 服务

#### 安装教程

1.  安装uv
+ 安装 uv 命令
```
 curl -LsSf https://astral.sh/uv/install.sh | sh
```

install.sh 脚本执行时会从 github.com 下载 uv-aarch64-apple-darwin.tar.gz 并解压后然后再安装。github.com 网络不稳定，可以手动下载。这里提供一个技巧，可下载目录启动本地 python http 临时服务用于支持脚本下载文件，同时修改install.sh 脚本中的下载地址为本地服务地址。

```
python -m http.server 8181
```
调整后的shell 脚本可以参考:
[修改后的uv-install.sh](./tutorial/uv-install.sh)


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

## gitee与github同步

1.git remote add github https://github.com/JavaPentesters/mcp-code-guidance.git 
作用是添加一个名为"github"的远程仓库地址到本地Git仓库配置中。
主要功能包括：
+ 添加一个新的远程仓库引用
+ 命名为"github"（可自定义）
+ 指向指定的Git仓库URL

2.git pull origin master

3.git push -u github main --verbose
JavaPentesters