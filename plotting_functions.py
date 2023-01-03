import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def create_heatmap(df, cols, plot_name):
    sns.heatmap(data=df[cols].corr(),annot=True, cmap='Purples').set(title = plot_name)
    return plt.savefig(plot_name+'.png')

def create_catplot(df, col, col1, plot_name):
    sns.catplot(x=col, kind='count', col=col1, palette='rainbow', data=df).set(title =plot_name)
    plt.savefig(plot_name+'.png')

#def create_catplot(df, xcol, kind1, plot_name, y=None, col=None,  hue=None):
 #   sns.catplot(x=xcol, y=None, kind=kind1, col=None ,hue=None, palette='rainbow', data=df).set(title = plot_name)
  #  plt.savefig(plot_name+'.png')
