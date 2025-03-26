# The Number of Rich Customers

import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    rich_count = store[store['amount'] > 500]['customer_id'].unique()
    df = pd.DataFrame(rich_count).rename(columns = {0:'rich_count'}).count()
    df = pd.DataFrame(df).rename(columns = {0:'rich_count'})
    print(df)
    return df

data = [[6, 1, 549], [8, 1, 834], [4, 2, 394], [11, 3, 657], [13, 3, 257]]
store = pd.DataFrame(data, columns=['bill_id', 'customer_id', 'amount']).astype({'bill_id':'int64', 'customer_id':'int64', 'amount':'int64'})

count_rich_customers(store)