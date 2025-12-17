import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


def plot_distributions(df: pd.DataFrame, n_cols: int = 4, bins: int = 50):
    cols = df.columns

    n_rows = int(np.ceil(len(cols) / n_cols))

    plt.figure(figsize=(3 * n_cols, 2 * n_rows))

    for i, col in enumerate(cols, start=1):
        plt.subplot(n_rows, n_cols, i)
        if df[col].dtypes == 'object':
            df[col].hist(bins=bins)
            plt.title(col)
            plt.xticks(rotation=45, ha='right')
        else:
            sns.histplot(data=df, x=col, kde=True, bins=bins)
            plt.title(f'{col}\nSkewness: {round(df[col].skew(), 2)}')
        plt.tight_layout()


def plot_target_vs_category(df: pd.DataFrame, target: str, n_cols: int = 4):
    cat_cols = df.select_dtypes(include=['object', 'category']).columns
    cat_cols = [c for c in cat_cols if c != target]

    if len(cat_cols) == 0:
        print('No categorical columns.')
        return

    n_rows = int(np.ceil(len(cat_cols) / n_cols))

    plt.figure(figsize=(5 * n_cols, 4 * n_rows))

    for i, col in enumerate(cat_cols, start=1):
        plt.subplot(n_rows, n_cols, i)

        sns.violinplot(data=df, x=col, y=target)

        plt.title(f'{col} vs {target}')
        plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()


def plot_numerical_boxplots(df, n_cols: int = 3):
    num_cols = df.select_dtypes(include=['number']).columns

    if len(num_cols) == 0:
        print('No numerical columns.')
        return

    n_rows = int(np.ceil(len(num_cols) / n_cols))
    plt.figure(figsize=(5 * n_cols, 4 * n_rows))

    for i, col in enumerate(num_cols, start=1):
        plt.subplot(n_rows, n_cols, i)
        sns.boxplot(data=df, x=col)
        plt.title(col)

    plt.tight_layout()
    plt.show()
