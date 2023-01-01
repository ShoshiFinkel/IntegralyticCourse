import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def create_heatmap(df, cols):
    sns.heatmap(data=df[cols].corr(),annot=True, cmap='Purples').set(title = 'Heatmap of {} columns'.format(cols))
    plt.savefig('heatmap.png')