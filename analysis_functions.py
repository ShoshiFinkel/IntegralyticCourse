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

def clean_nulls(df,col,fillna):
    sum_nulls = count_nulls(df,col)
    print(sum_nulls.dtype)
    if sum_nulls >500:
        df = drop_col(df,col)
        return df
    else:
        df[col] =df[col].fillna(fillna)
        return df

def month_in_num(df, month_col):
    df[month_col] = df[month_col].map({'January' : 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November': 11, 'December':12})

def datetime_col(df, new_col, year_col, month_col, day_col):
    month_in_num(df, month_col)
    df[new_col] =pd.to_datetime(dict(year=df.year_col, month=df.month_col, day=df.day_col))
    return df