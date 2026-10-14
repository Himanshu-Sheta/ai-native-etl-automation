import pandas as pd
import numpy as np
from typing import Tuple, List, Dict, Any

class DataHarmonizationCleaner:
    """
    Enterprise data cleaning and standardization engine.
    Applies deterministic transformation rules with vectorised Pandas operations.
    """
    @staticmethod
    def clean_dataframe(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, Any]]:
        initial_rows, initial_cols = df.shape
        metrics = {
            "initial_rows": initial_rows,
            "deduplicated_rows": 0,
            "nulls_imputed": 0,
            "transformed_columns": []
        }
        
        # 1. Deduplication
        pre_dedup = len(df)
        df = df.drop_duplicates().copy()
        metrics["deduplicated_rows"] = pre_dedup - len(df)
        
        # 2. String standardization
        str_cols = df.select_dtypes(include=["object"]).columns
        for c in str_cols:
            df[c] = df[c].astype(str).str.strip()
            # Replace string representations of nulls
            df[c] = df[c].replace({"nan": None, "None": None, "NULL": None, "": None})
            metrics["transformed_columns"].append(c)
            
        # 3. Numeric imputation
        num_cols = df.select_dtypes(include=[np.number]).columns
        for c in num_cols:
            null_count = df[c].isnull().sum()
            if null_count > 0:
                median_val = df[c].median()
                df[c] = df[c].fillna(median_val)
                metrics["nulls_imputed"] += int(null_count)
                
        metrics["final_rows"] = len(df)
        return df, metrics
