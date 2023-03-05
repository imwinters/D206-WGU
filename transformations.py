import pandas as pd
import numpy as np

def transform_yes_no_to_bit(data_frame, target_feature: str) -> None:
    data_frame[target_feature].replace(("Yes", "No"), (1,0), inplace=True)
    print(f"{target_feature} Yes/No swapped for 1/0")


