import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def count_nulls(df,col):
    print(df[col].isnull().sum())

def create_catplot(df, col, col1):
    sns.catplot(x=col, kind='count', col=col1, palette='rainbow', data=df).set(title = 'Bar chart of {} per {}'.format(col,col1))
    plt.show()
