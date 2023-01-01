def explore_data(df):
    print(df.head())
    print(df.info())
    print(df.describe())
    print(df.isnull().sum().sort_values(ascending=False))

def count_nulls(df,col):
    print(df[col].isnull().sum())