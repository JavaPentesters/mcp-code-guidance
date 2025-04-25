import akshare as ak
import pandas as pd
from typing import List, Dict, Optional


def _convert_to_records(df: pd.DataFrame) -> List[Dict]:
        """转换DataFrame为字典列表"""
        if df.empty:
            return []
        return df.to_dict(orient='records')

def main():
    df = ak.stock_individual_info_em('603171')
    info_dict = _convert_to_records(df)
    print(info_dict)


if __name__ == "__main__":
    main()
