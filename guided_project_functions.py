import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

hotel_bookings = pd.read_csv('hotel_bookings.csv')

def count_nulls(col):
    hotel_bookings[col].isnull().sum()

def create_catplot(col, col1):
    sns.catplot(x=col, kind='count', col=col1,palette='rainbow', data=hotel_bookings).set(title = 'Bar chart of {} column'.format(col))
    plt.show()
