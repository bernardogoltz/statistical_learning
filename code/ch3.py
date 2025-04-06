# -*- coding: utf-8 -*-
"""
Created on Sat Apr  5 16:00:25 2025

@author: Bernardo
"""

import statsmodels.api as sm 
import pandas as pd 
import numpy as np 
from statsmodels.sandbox.regression.predstd import wls_prediction_std
import matplotlib.pyplot as plt
import seaborn as sns 

# Load data
PATH = 'C:/Users/Bernardo/Documents/ISLP/datasets/Auto.csv'
df = pd.read_csv(PATH)

def criar_scatter_matrix_estilizada(df, colunas, titulo="Scatter Matrix"):
    """
    Cria uma matriz de dispersão estilizada usando seaborn.
    
    Parâmetros:
    df (DataFrame): DataFrame pandas contendo os dados
    colunas (list): Lista de nomes das colunas para incluir na visualização
    titulo (str): Título principal do gráfico
    
    Retorna:
    matplotlib.figure.Figure: Objeto da figura criada
    """
    # Verificar se as colunas existem no DataFrame
    for col in colunas:
        if col not in df.columns:
            raise ValueError(f"Coluna '{col}' não encontrada no DataFrame")
    
    # Configurar o estilo do seaborn
    sns.set_style("whitegrid")
    sns.set_context("notebook", font_scale=1.2)
    

    
    # Criar a matriz de dispersão com seaborn
    g = sns.pairplot(
        df[colunas],
        diag_kind="kde",
        markers="o",
        height=2.5,
        aspect=1,
        plot_kws={
            "s": 60,
            "edgecolor": "navy",
            "linewidth": 0.8,
            "alpha": 0.7
        },
        diag_kws={
            "fill": True,
            "alpha": 0.5,
            "color": "steelblue",
            "linewidth": 1.5
        }
    )
    
    # Adicionar título principal
    g.fig.suptitle(titulo, fontsize=20, fontweight="bold", y=1)
    
    # Personalizar cada subplot
    for i in range(len(colunas)):
        for j in range(len(colunas)):
            # Adicionar linhas de grade menos visíveis
            g.axes[i, j].grid(True, linestyle="--", alpha=0.3)
            
            # Definir rótulos com fonte em negrito
            if i == len(colunas) - 1:  # Última linha
                g.axes[i, j].set_xlabel(colunas[j], fontweight="bold")
            if j == 0:  # Primeira coluna
                g.axes[i, j].set_ylabel(colunas[i], fontweight="bold")
    
    # Ajustar o layout
    plt.tight_layout()
    
    return g.fig


tipos = df.dtypes

def plot_correlation_heatmap(df, columns=None, figsize=(10, 8), cmap='coolwarm',
                            annot=True, fmt='.2f', title='Correlation Matrix'):
    """
    Create and display a correlation heatmap for the specified columns in a dataframe.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        The dataframe containing the data to analyze
    columns : list, optional
        List of column names to include in the correlation matrix.
        If None, all numeric columns will be used.
    figsize : tuple, optional
        Figure size as (width, height) in inches
    cmap : str, optional
        Colormap for the heatmap
    annot : bool, optional
        Whether to annotate cells with correlation values
    fmt : str, optional
        String formatting code for annotations
    title : str, optional
        Title for the plot
    
    Returns:
    --------
    fig : matplotlib.figure.Figure
        The figure object containing the plot
    """
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    # If no columns specified, use all numeric columns
    if columns is None:
        columns = df.select_dtypes(include=['number']).columns.tolist()
    
    # Calculate the correlation matrix
    corr = df[columns].astype(float).corr()
    
    # Create a figure with appropriate size
    fig, ax = plt.subplots(figsize=figsize)
    
    # Create the heatmap
    sns.heatmap(corr, annot=annot, cmap=cmap, vmin=-1, vmax=1, 
                fmt=fmt, linewidths=0.5, ax=ax)
    
    # Add title
    ax.set_title(title, fontsize=14)
    
    # Adjust layout
    plt.tight_layout()
    
    return fig



# Create correlation heatmap on the left subplot
plot_correlation_heatmap(df, columns=['mpg', 'cylinders', 'displacement', 'weight', 
                                      'acceleration', 'year', 'origin'], 
                        figsize=None, title='Correlation Matrix')

criar_scatter_matrix_estilizada(df , colunas=['mpg',  'displacement', 'weight', 
                                      'acceleration'])
