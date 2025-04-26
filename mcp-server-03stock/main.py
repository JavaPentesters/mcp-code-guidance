import akshare as ak
import pandas as pd
from typing import List, Dict, Optional
from pydantic import BaseModel


class StockBasicInfo(BaseModel):
    """股票基本信息数据模型"""
    code: str
    name: str
    industry: Optional[str]
    area: Optional[str]
    market: Optional[str]

#[{'item': '股票代码', 'value': '603171'}, {'item': '股票简称', 'value': '税友股份'}, {'item': '总股本', 'value': 406763250.0}, {'item': '流通股', 'value': 405890000.0}, {'item': '总市值', 'value': 17401331835.0}, {'item': '流通市值', 'value': 17363974200.0}, {'item': '行业', 'value': '互联网服务'}, {'item': '上市时间', 'value': 20210630}]
def _convert_to_records(df: pd.DataFrame) -> Dict:
        """转换DataFrame为字典列表"""
        if df.empty:
            return []
        records = df.to_dict(orient='records')
        mapping = {
            'code': '',
            'name': '',
            'industry': '',
            'area': '',
            'market': ''
        }
        # 转换字段名以匹配StockBasicInfo模型
        for record in records:
            if 'item' in record and record['item'] == '股票代码':
                mapping['code'] = record.pop('value')
            elif 'item' in record and record['item'] == '股票简称':
                mapping['name'] = record.pop('value')
            elif 'item' in record and record['item'] == '行业':
                mapping['industry'] = record.pop('value')
            elif 'item' in record and record['item'] == '地区':
                mapping['area'] = record.pop('value')
            elif 'item' in record and record['item'] == '市场':
                mapping['market'] = record.pop('value')
        return mapping
# [{'item': '股票代码', 'code': '603171'}, {'item': '股票简称', 'name': '税友股份'}, {'item': '总股本', 'value': 406763250.0}, {'item': '流通股', 'value': 405890000.0}, {'item': '总市值', 'value': 17401331835.0}, {'item': '流通市值', 'value': 17363974200.0}, {'item': '行业', 'industry': '互联网服务'}, {'item': '上市时间', 'value': 20210630}]

def main():
    df = ak.stock_individual_info_em('603171')
    info_dict = _convert_to_records(df)
    sb= StockBasicInfo(**info_dict)
    print(sb)


if __name__ == "__main__":
    main()
