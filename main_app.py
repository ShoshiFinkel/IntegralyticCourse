# Final Project

# My plan is to first explore the data. For this purpose, I will print head, info and describe.
#In addition, I will check if there are nulls and I will count the values of some of the columns
#After that I will clean the data. I will delete irrelevant columns and replace the missing values
#After that I will analyze the information with graphs
#I will create graphs that will show me the information in different parallels so that I can analyze the information.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotting_functions import create_heatmap
from analysis_functions import display_info, clean_nulls, count_nulls, datetime_col

df = pd.read_csv("hotel_bookings.csv")

display_info(df)
clean_nulls(df, 'company', 0)
clean_nulls(df, 'agent', 0)
clean_nulls(df, 'children', 0)
clean_nulls(df, 'country', 'PRT')
count_nulls(df, 'children')
count_nulls(df, 'country')
datetime_col(df, 'arrival_date', 'arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month')
create_heatmap(df, ['lead_time','is_canceled'])


