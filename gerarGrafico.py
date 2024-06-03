import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

dataframe = pd.read_csv('prescricao_resumo.csv')

# Definindo as novas cores para cada categoria

#         AZUL        AMARELO   VERMELHO
cores = ['#669BBC', '#f0bd00', '#780000']

# Ajustando as labels para corresponderem às cores
labels = ['Maior que 2 anos', 'Entre 1 ano e 2', 'Menor que 1 ano']

for i in range(len(dataframe)):
    y = np.array(dataframe.iloc[i].iloc[-3:].tolist())
    
    # Definindo o tamanho da figura e criando o gráfico
    plt.figure(figsize=(6, 6))
    
    titulo = f'SJ {dataframe.iloc[i].iloc[0]}'  # Usando iloc[] para acessar por posição
    
    # Configurando o estilo da fonte para os valores
    fonte_valores = {'fontsize': 16, 'fontweight': 'bold'}
    
    # Criando o gráfico de pizza sem labels
    plt.pie(y, colors=cores, autopct='%1.1f%%', textprops=fonte_valores)
    
    # Criando a legenda com as cores correspondentes
    plt.legend(labels=labels, loc='upper right', fontsize=16, title='Legenda')
    
    # Configurando o estilo da fonte para o título do gráfico
    plt.title(titulo, fontsize=16, fontweight='bold')
    
    plt.axis('equal')  # Ajusta a proporção do gráfico para ser circular
    plt.savefig(f'./graficos/chart{i}.png')
    plt.close()  # Fecha a figura para liberar memória
