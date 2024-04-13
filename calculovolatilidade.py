import tradingcomdados
from tradingcomdados import alternative_data as ad
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

ad.index_composition('idiv')

codigos = ad.index_composition('idiv')['cod']
codsa = codigos + '.SA'

# Criar um DataFrame vazio para armazenar os dados baixados
dados_acoes = pd.DataFrame()

# Baixar os dados para cada ação
for cod in codsa:
    try:
        # Baixar os dados utilizando yfinance e adicionar à DataFrame
        dados_acao = yf.download(cod, start='2024-01-01', end='2024-04-06')['Adj Close'].to_frame()
        dados_acoes = pd.concat([dados_acoes, dados_acao.rename(columns={'Adj Close': cod})], axis=1)
    except Exception as e:
        print(f"Erro ao baixar dados para {codsa}: {e}")

# Visualizar o DataFrame com os dados baixados
print(dados_acoes)

retornos_diarios = dados_acoes.pct_change().dropna()

desvio_padrao_diario = retornos_diarios.std()
desvio_padrao_diario.index = desvio_padrao_diario.index.str.slice(stop = -3)
print(desvio_padrao_diario)

# Plotar os desvios padrão diários
plt.figure(figsize=(10, 6))
desvio_padrao_diario.plot(kind='bar', color='blue')
plt.title('Desvio Padrão Diário dos Retornos')
plt.xlabel('Código da Ação')
plt.ylabel('Desvio Padrão')
plt.xticks(rotation='vertical')
plt.grid(axis='y')
plt.tight_layout()
plt.show()