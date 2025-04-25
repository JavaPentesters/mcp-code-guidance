from fastmcp import FastMCP
from pydantic import BaseModel
from typing import List, Dict, Optional
from datetime import datetime
import akshare as ak
import pandas as pd


mcp = FastMCP(name="股票助手")

@mcp.tool('stock_individual_basic_info')
async def stock_individual_basic_info(stock_code: str):
    """获取股票基本信息"""
    return await StockService().get_stock_basic_info(stock_code)

class StockBasicInfo(BaseModel):
    """股票基本信息数据模型"""
    code: str
    name: str
    industry: Optional[str]
    area: Optional[str]
    market: Optional[str]

class StockRepository:
    """股票数据仓库，负责数据访问层"""

    @staticmethod
    def _convert_to_records(df: pd.DataFrame) -> List[Dict]:
        """转换DataFrame为字典列表"""
        if df.empty:
            return []
        return df.to_dict(orient='records')

    async def get_stock_basic_info(self, stock_code: str) -> StockBasicInfo:
        """获取股票基本信息"""
        df = ak.stock_individual_info_em(symbol=stock_code)
        if df.empty:
            raise RuntimeError("未找到股票信息")
        
        info_dict = self._convert_to_records(df)[0]
        return StockBasicInfo(**info_dict)

class StockService:
    """股票服务类，处理业务逻辑"""

    def __init__(self, repository: Optional[StockRepository] = None):
        """初始化服务，支持依赖注入"""
        self.repository = repository or StockRepository()

    async def get_stock_basic_info(self, stock_code: str) -> StockBasicInfo:
        """获取股票基本信息"""
        return await self.repository.get_stock_basic_info(stock_code)   

if __name__ == "__main__":
    mcp.run()