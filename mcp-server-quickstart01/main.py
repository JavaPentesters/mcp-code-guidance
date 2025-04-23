from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("QuickStart01")

# 定义了一个名为 add 的工具函数，它接受两个整数参数 a 和 b，并返回它们的和。
# 这个函数被装饰为 mcp.tool()，这意味着它将成为一个可通过 MCP 服务器调用的工具。
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

# 定义了一个名为 get_greeting 的资源函数，它接受一个字符串参数 name，并返回一个问候语。
# 这个函数被装饰为 mcp.resource()，这意味着它将成为一个可通过 MCP 服务器访问的资源。
# 资源的 URL 是 "greeting://{name}"，其中 {name} 是一个占位符，将被实际的 name 参数替换。
# 当客户端访问这个资源时，MCP 服务器将调用这个函数，并将 name 参数替换为实际的值。
# 函数返回的字符串将作为响应体返回给客户端。
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"

@mcp.prompt()
def custom_prompt(name: str) -> str:
    """
    欢迎指定用户
    """
    return f"欢迎，{name}！有什么需要帮助的码?"


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run()
