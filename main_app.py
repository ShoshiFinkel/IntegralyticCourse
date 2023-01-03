# Final Project

# My plan is to first explore the data. For this purpose, I will print head, info and describe.
#In addition, I will check if there are nulls and I will count the values of some of the columns
#After that I will clean the data. I will delete irrelevant columns and replace the missing values
#After that I will analyze the information with graphs
#I will create graphs that will show me the information in different parallels so that I can analyze the information.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from plotting_functions import create_heatmap, create_catplot
from analysis_functions import display_info, clean_nulls, count_nulls, datetime_col, month_in_num, col_value_counts

# Read the data
df = pd.read_csv("hotel_bookings.csv")

# Display information about the data: head, info, describe and count the nulls. The argument is the dataframe.
display_info(df)
# Clean the null values. if there are more than 500 null values in a column- drop the column, else- fill the nuns with the argument. The arguments are the dataframe, the column, and the value to fill the nulls with.
clean_nulls(df, 'company', 0)
clean_nulls(df, 'agent', 0)
clean_nulls(df, 'children', 0)
clean_nulls(df, 'country', 'PRT')
# Check if there are still nulls. The arguments are the dataframe and the column.
count_nulls(df, 'children')
count_nulls(df, 'country')
# Change the month's names to numbers. The arguments are the dataframe and the column(should be the month column)
month_in_num(df, 'arrival_date_month')
# Create a column of arrival date, including day, month and year. The arguments are the dataframe, new column name, year column, month column, date column.
datetime_col(df, 'arrival_date', 'arrival_date_year', 'arrival_date_month', 'arrival_date_day_of_month')
# Create heatmap to find the correlation between few columns. The arguments are the dataframe, columns as a list, the plot name.
create_heatmap(df, ['lead_time','is_canceled'], 'Heatmap of Lead time Impacting Cancellations')
# Create catplot. The arguments are the dataframe, column for the x parameter, column for the col parameter, and the plot name.
create_catplot(df, 'arrival_date_month', 'hotel', "Booking Per Month")
# Count the values in a column. The arguments are the dataframe, column, and number of rows to print in the .head() function.
col_value_counts(df, 'country', 10)
