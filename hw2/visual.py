import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

visualizations = {}

def add_histogram(df, column, save_path=None):
    plt.figure()
    sns.histplot(df[column].dropna(), kde=False)
    plt.title(f'Гистограмма: {column}')
    if save_path:
        plt.savefig(save_path)
    visualizations[f'hist_{column}'] = plt.gcf()

def add_lineplot(df, x, y, save_path=None):
    plt.figure()
    sns.lineplot(x=df[x], y=df[y])
    plt.title(f'Линейный график: {x} vs {y}')
    if save_path:
        plt.savefig(save_path)
    visualizations[f'line_{x}_{y}'] = plt.gcf()

def add_scatterplot(df, x, y, save_path=None):
    plt.figure()
    sns.scatterplot(x=df[x], y=df[y])
    plt.title(f'Диаграмма рассеяния: {x} vs {y}')
    if save_path:
        plt.savefig(save_path)
    visualizations[f'scatter_{x}_{y}'] = plt.gcf()

def add_survival_countplot(df, save_path=None):
    plt.figure()
    sns.countplot(x='Survived', data=df)
    plt.title('Количество выживших и невыживших')
    if save_path:
        plt.savefig(save_path)
    visualizations['survival_countplot'] = plt.gcf()

def add_survival_by_sex(df, save_path=None):
    plt.figure()
    df_copy = df.copy()
    df_copy['Sex'] = df_copy['Sex'].map({0: 'Женщины', 1: 'Мужчины'})

    sns.countplot(x='Sex', hue='Survived', data=df_copy)
    plt.title('Выживаемость по полу')
    plt.xlabel('Пол')
    plt.ylabel('Количество')

    if save_path:
        plt.savefig(save_path)

    visualizations['survival_by_sex'] = plt.gcf()

def add_survival_heatmap(df, save_path=None):
    survival_matrix = pd.crosstab(df['Pclass'], df['Survived'])
    plt.figure()
    sns.heatmap(survival_matrix, annot=True, cmap='Blues', fmt='g')
    plt.title('Тепловая карта выживаемости по классу')
    if save_path:
        plt.savefig(save_path)
    visualizations['survival_heatmap'] = plt.gcf()

def show_visualizations():
    for fig in visualizations.values():
        fig.show()