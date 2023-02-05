import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Create heatmap to find the correlation between few columns. The arguments are the dataframe, columns as a list, the plot name.
def create_heatmap(df, cols, plot_name):
    sns.heatmap(data=df[cols].corr(),annot=True, cmap='Purples').set(title = plot_name)
    return plt.savefig(plot_name+'.png')

# Create catplot. The arguments are the dataframe, column for the x parameter, column for the col parameter, and the plot name.
def create_catplot(df, col, col1, plot_name):
    sns.catplot(x=col, kind='count', col=col1, palette='rainbow', data=df).set(title =plot_name)
    plt.savefig(plot_name+'.png')

