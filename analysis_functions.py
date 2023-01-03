import pandas as pd

def display_info(df):
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.isnull().sum().sort_values(ascending=False))

def count_nulls(df,col):
    sum_nulls = df[col].isnull().sum()
    print(sum_nulls)
    return sum_nulls

def drop_col(df,col):
    df.drop(col,axis=1, inplace = True)
    return df

def clean_nulls(df,col,fillnans):
    sum_nulls = count_nulls(df,col)
    if sum_nulls >500:
        df = drop_col(df,col)
        return df
    else:
        df[col] =df[col].fillna(fillnans)
        return df

def month_in_num(df, month_col):
    df[month_col] = df[month_col].map({'January' : 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November': 11, 'December':12})
    return df

def datetime_col(df, new_col, year_col, month_col, day_col):
    df['dateInt']=df[year_col].astype(str) + df[month_col].astype(str).str.zfill(2)+ df[day_col].astype(str).str.zfill(2)
    df[new_col] = pd.to_datetime(df['dateInt'], format='%Y%m%d')
    return df

def col_value_counts(df,col,head_rows):
    result = df[col].value_counts().head(head_rows)
    print(result)
