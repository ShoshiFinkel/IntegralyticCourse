import pandas as pd
df = pd.read_csv('parallel processing\Lesson3\googleplaystore.csv')
categories = df['Category'].unique()
def count_categories():
    count_categories_dict = {}
    for category in categories:
        count_categories = df['Category'].str.count(category).sum()
        count_categories_dict[category]=count_categories
    return count_categories_dict

count_categories()