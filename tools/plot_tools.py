import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column):
    plt.figure()
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribution of {column}")
    return plt

def plot_bar(df, column):
    plt.figure()
    df[column].value_counts().plot(kind="bar")
    plt.title(f"Count of {column}")
    return plt

def plot_correlation_heatmap(df):
    plt.figure()
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
    plt.title("Correlation Heatmap")
    return plt