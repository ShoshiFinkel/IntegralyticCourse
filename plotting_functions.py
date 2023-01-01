def create_heatmap(df, cols):
    sns.heatmap(data=df[cols].corr(),annot=True, cmap='Purples')
    plt.suptitle("Heatmap of", cols)