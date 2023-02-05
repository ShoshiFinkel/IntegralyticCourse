# Check if there are nulls. The arguments are the dataframe and the column.
def count_nulls(df,col):
    sum_nulls = df[col].isnull().sum()
    print(sum_nulls)
    return sum_nulls

# Drop columns. The arguments are the dataframe and column.
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

def print_head(df):
    print(df.head())

def display_info(df):
    print_head(df)
    print(df.info())
    print(df.describe())
    print(df.isnull().sum().sort_values(ascending=False))