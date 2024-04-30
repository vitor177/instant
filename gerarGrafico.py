import matplotlib.pyplot as plt
import numpy as np
from sender import Sender

import pandas as pd

dataframe = pd.read_csv('prescricao_resumo.csv')

labels = ['Entre 1 ano e 2', 'Entre 2 anos e 3', 'Acima de 3 anos']

for i in range(len(dataframe)):
    y = np.array(dataframe.iloc[i][-3:].tolist())
    plt.figure()
    plt.pie(y, labels=labels, autopct='%1.1f%%')
    plt.title(f'Quantidade de processos em improbidade administrativa SJ {str(dataframe.iloc[i][0])}')
    plt.savefig(f'./graficos/chart{i}.png')

