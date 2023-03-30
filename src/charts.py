import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# df = pd.read_csv('arquivo2final.csv')

# df = df[(df['LCOM Median'] != 0) | (df['CBO Median'] != 0) | (df['DIT Max'] != 0)]
# df = df[~df['nameWithOwner'].str.contains('javascript', case=False)]

# df.to_csv('arquivo3final.csv', index=False)


df = pd.read_csv('arquivo3final.csv')


plt.scatter(df['Estrelas'], df['DIT Max'])

m, b = np.polyfit(df['Estrelas'], df['DIT Max'], 1)
trendline_x = np.array([min(df['Estrelas']), max(df['Estrelas'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('Estrelas')
plt.ylabel('DIT')
plt.savefig('estrelasXdit.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico


plt.scatter(df['Estrelas'], df['LCOM Median'])

m, b = np.polyfit(df['Estrelas'], df['LCOM Median'], 1)
trendline_x = np.array([min(df['Estrelas']), max(df['Estrelas'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('Estrelas')
plt.ylabel('LCOM')
plt.savefig('estrelasXlcom.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico


plt.scatter(df['Estrelas'], df['CBO Median'])

m, b = np.polyfit(df['Estrelas'], df['CBO Median'], 1)
trendline_x = np.array([min(df['Estrelas']), max(df['Estrelas'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('Estrelas')
plt.ylabel('CBO')
plt.savefig('estrelasXcbo.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico



plt.scatter(df['LOC Total'], df['DIT Max'])

m, b = np.polyfit(df['LOC Total'], df['DIT Max'], 1)
trendline_x = np.array([min(df['LOC Total']), max(df['LOC Total'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('LOC')
plt.ylabel('DIT')
plt.savefig('locXdit.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico


plt.scatter(df['LOC Total'], df['LCOM Median'])

m, b = np.polyfit(df['LOC Total'], df['LCOM Median'], 1)
trendline_x = np.array([min(df['LOC Total']), max(df['LOC Total'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('LOC')
plt.ylabel('LCOM')
plt.savefig('locXlcom.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico


plt.scatter(df['LOC Total'], df['CBO Median'])

m, b = np.polyfit(df['LOC Total'], df['CBO Median'], 1)
trendline_x = np.array([min(df['LOC Total']), max(df['LOC Total'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('LOC')
plt.ylabel('CBO')
plt.savefig('locXcbo.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico


plt.scatter(df['Número de releases'], df['DIT Max'])

m, b = np.polyfit(df['Número de releases'], df['DIT Max'], 1)
trendline_x = np.array([min(df['Número de releases']), max(df['Número de releases'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('Número de releases')
plt.ylabel('DIT')
plt.savefig('releaseXdit.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico



plt.scatter(df['Número de releases'], df['LCOM Median'])

m, b = np.polyfit(df['Número de releases'], df['LCOM Median'], 1)
trendline_x = np.array([min(df['Número de releases']), max(df['Número de releases'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.savefig('releaseXlcom.png') # Salvar o gráfico em um arquivo
plt.xlabel('Número de releases')
plt.ylabel('LCOM')
plt.savefig('releaseXlcom.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico


plt.scatter(df['Número de releases'], df['CBO Median'])

m, b = np.polyfit(df['Número de releases'], df['CBO Median'], 1)
trendline_x = np.array([min(df['Número de releases']), max(df['Número de releases'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('Número de releases')
plt.ylabel('CBO')
plt.savefig('releaseXcbo.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico




plt.scatter(df['Idade (anos)'], df['DIT Max'])

m, b = np.polyfit(df['Idade (anos)'], df['DIT Max'], 1)
trendline_x = np.array([min(df['Idade (anos)']), max(df['Idade (anos)'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')

plt.xlabel('Idade (anos)')
plt.ylabel('DIT')
plt.savefig('idadeXdit.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico



plt.scatter(df['Idade (anos)'], df['LCOM Median'])

m, b = np.polyfit(df['Idade (anos)'], df['LCOM Median'], 1)
trendline_x = np.array([min(df['Idade (anos)']), max(df['Idade (anos)'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')
plt.xlabel('Idade (anos)')
plt.ylabel('LCOM')
plt.savefig('idadeXlcom.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico


plt.scatter(df['Idade (anos)'], df['CBO Median'])

m, b = np.polyfit(df['Idade (anos)'], df['CBO Median'], 1)
trendline_x = np.array([min(df['Idade (anos)']), max(df['Idade (anos)'])])
trendline_y = m * trendline_x + b
plt.plot(trendline_x, trendline_y, 'r')
plt.xlabel('Idade (anos)')
plt.ylabel('CBO')
plt.savefig('idadeXcbo.png') # Salvar o gráfico em um arquivo
plt.show() # Exibir o gráfico

