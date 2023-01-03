import pandas as pd

# Display information about the data: head, info, describe and count the nulls. The argument is the dataframe.
def display_info(df):
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.isnull().sum().sort_values(ascending=False))

# Check if there are nulls. The arguments are the dataframe and the column.
def count_nulls(df,col):
    sum_nulls = df[col].isnull().sum()
    print(sum_nulls)
    return sum_nulls

# Drop columns. The arguments are the dataframe and column.
def drop_col(df,col):
    df.drop(col,axis=1, inplace = True)
    return df

# Clean the null values. if there are more than 500 null values in a column- drop the column, else- fill the nuns with the argument. The arguments are the dataframe, the column, and the value to fill the nulls with.
def clean_nulls(df,col,fillnans):
    sum_nulls = count_nulls(df,col)
    if sum_nulls >500:
        df = drop_col(df,col)
        return df
    else:
        df[col] =df[col].fillna(fillnans)
        return df

# Change the month's names to numbers. The arguments are the dataframe and the column(should be the month column)
def month_in_num(df, month_col):
    df[month_col] = df[month_col].map({'January' : 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June':6, 'July':7, 'August':8, 'September':9, 'October':10, 'November': 11, 'December':12})
    return df

# Create a column of arrival date, including day, month and year. The arguments are the dataframe, new column name, year column, month column, date column.
def datetime_col(df, new_col, year_col, month_col, day_col):
    df['dateInt']=df[year_col].astype(str) + df[month_col].astype(str).str.zfill(2)+ df[day_col].astype(str).str.zfill(2)
    df[new_col] = pd.to_datetime(df['dateInt'], format='%Y%m%d')
    return df

# Count the values in a column. The arguments are the dataframe, column, and number of rows to print in the .head() function.
def col_value_counts(df,col,head_rows):
    result = df[col].value_counts().head(head_rows)
    print(result)
