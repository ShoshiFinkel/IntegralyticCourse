import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

hotel_bookings = pd.read_csv('hotel_bookings.csv')

def count_nulls(col):
    hotel_bookings[col].isnull().sum().sort_values(ascending=False)

