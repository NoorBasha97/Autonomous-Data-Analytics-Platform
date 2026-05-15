import matplotlib.pyplot as plt
import seaborn as sns


def plot_histogram(df, column):
    fig, ax = plt.subplots(figsize=(5, 3))  # smaller size
    sns.histplot(df[column], kde=True, ax=ax)
    ax.set_title(f"{column} Distribution")
    return fig


def plot_bar(df, column):
    fig, ax = plt.subplots(figsize=(5, 3))
    df[column].value_counts().plot(kind="bar", ax=ax)
    ax.set_title(f"{column} Count")
    return fig


def plot_correlation_heatmap(df):
    fig, ax = plt.subplots(figsize=(5, 4))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    ax.set_title("Correlation Heatmap")
    return fig