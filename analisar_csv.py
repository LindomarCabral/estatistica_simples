import pandas as pd
import sys

def gerar_estatisticas(nome_arquivo):
    """
    Lê um arquivo CSV e imprime estatísticas descritivas básicas.
    """
    try:
        # Carrega o arquivo CSV em um DataFrame do Pandas
        df = pd.read_csv(nome_arquivo)

        print(f"--- Estatísticas Descritivas para o arquivo: {nome_arquivo} ---")
        print("\nVisão geral dos dados (primeiras 5 linhas):")
        print(df.head())

        print("\nInformações gerais sobre as colunas e tipos de dados:")
        print(df.info())

        print("\nEstatísticas básicas para colunas numéricas:")
        # Gera estatísticas descritivas (média, mediana, std, min, max, etc.)
        print(df.describe())

    except FileNotFoundError:
        print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro durante a leitura ou análise do arquivo: {e}")

if __name__ == "__main__":
    # Define o nome do arquivo CSV a ser analisado
    # Você pode alterar para o nome do seu arquivo ou passar como argumento
    nome_do_seu_arquivo_csv = "dados.csv" 
    gerar_estatisticas(nome_do_seu_arquivo_csv)

