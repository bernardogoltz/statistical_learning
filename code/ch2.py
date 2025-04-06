# -*- coding: utf-8 -*-
"""
Created on Fri Apr  4 15:30:56 2025

@author: Bernardo
"""
import pandas as pd 
import numpy as np 
import os 
import matplotlib.pyplot as plt 
import seaborn as sns 

PATH = 'C:/Users/Bernardo/Documents/ISLP/datasets/College.csv'

df = pd.read_csv(PATH)

df.rename({'Unnamed: 0':'College'} , axis = 1 , inplace = True)

df.set_index('College' , inplace = True)


# c

describe = df.describe().T


# d 
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
    
    # Criar a figura e configurar o tamanho
    fig = plt.figure(figsize=(12, 10))
    
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

scatter_fig = criar_scatter_matrix_estilizada(df, ['Top10perc', 'Apps', 'Enroll'])
plt.show()




# e 

sns.boxplot(y='Outstate', x='Private', data=df)
plt.grid(False)



# f

df['Elite'] = np.where(df['Top10perc'] >= 50, 'Yes', 'No')
elite_count = df['Elite'].value_counts()
plt.title('Mensalidade x Elite')
sns.boxplot(y = 'Outstate' , x = 'Elite' , data = df)
plt.grid(alpha = 0.3)


tipos = df.dtypes
colunas_numericas = tipos[tipos.apply(lambda x: np.issubdtype(x, np.number))]

fig , axs = plt.subplots(2,2 , dpi = 120)

axs = axs.flatten()

axs[0].set_title('Valor da Mensalidade')
axs[0].hist(df['Outstate'] , bins = 20 , edgecolor = 'black')

axs[1].set_title('Aplicações e Aprovações')
axs[1].hist(df['Apps'] , bins = 20 , edgecolor = 'black' , label = 'Apps')
axs[1].hist(df['Accept'] , bins = 20 , edgecolor = 'black' , label = 'Aprv.')
axs[1].set_yscale('symlog')
axs[1].legend()

axs[3].set_title("# de estudantes")
axs[3].hist(df['Top10perc'], bins=20, edgecolor='black', alpha=0.3, color='royalblue', label='Top 10%')
axs[3].hist(df['Top25perc'], bins=20, edgecolor='black', alpha=0.3, color='tomato', label='Top 25%')
axs[3].legend()

axs[2].set_title("# de cursos")
axs[2].hist(df['F.Undergrad'] , bins = 20 , alpha = 0.3 , label = 'Integral')
axs[2].hist(df['P.Undergrad'] , bins = 20 , alpha = 0.3 , label = 'Meio Período')
axs[2].legend()
axs[2].set_yscale('log')

for ax in axs:
    ax.grid(alpha = 0.2)
    
plt.tight_layout()