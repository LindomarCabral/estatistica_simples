# 📊 Estatística Simples

**Estatística Simples** é um projeto Python desenvolvido para gerar **estatísticas descritivas básicas** a partir de arquivos CSV, utilizando a biblioteca **Pandas**.  
O objetivo é oferecer uma ferramenta prática para análise inicial de dados — ideal para cientistas de dados iniciantes, analistas e desenvolvedores que desejam explorar seus datasets rapidamente.

---

## 🚀 Funcionalidades

- Leitura automática de arquivos `.csv`
- Exibição das **5 primeiras linhas** do dataset
- Exibição das **informações gerais** (colunas, tipos de dados e valores nulos)
- Geração de **estatísticas descritivas** (média, mediana, desvio padrão, mínimo, máximo, etc.)
- Tratamento de erros comuns (arquivo não encontrado, formatação incorreta)

---

## 🧠 Exemplo de Uso

```bash
# Clone o repositório
git clone https://github.com/lindomarcabral/estatistica_simples.git

# Acesse a pasta do projeto
cd estatistica_simples

# Execute o script
python estatistica_simples.py
````

Por padrão, o script busca um arquivo chamado **dados.csv** no mesmo diretório.
Você também pode passar o nome do arquivo como argumento:

```bash
python estatistica_simples.py meu_arquivo.csv
```

---

## 📈 Exemplo de Saída

```
--- Estatísticas Descritivas para o arquivo: dados.csv ---

Visão geral dos dados (primeiras 5 linhas):
     idade  salario  tempo_empresa
0       23    3200.0             2
1       45    8900.0            10
2       31    5000.0             4

Informações gerais sobre as colunas e tipos de dados:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 3 columns):
...

Estatísticas básicas para colunas numéricas:
             idade     salario  tempo_empresa
count   100.000000   100.00000     100.000000
mean     34.520000  5500.34000       6.200000
std       8.900000  2300.10000       3.400000
min      20.000000  2500.00000       1.000000
max      59.000000 10500.00000      15.000000
```

---

## 🛠️ Tecnologias Utilizadas

* [Python 3.9+](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [VS Code](https://code.visualstudio.com/)
* Git e GitHub

---

## 📚 Conceitos Envolvidos

* Leitura e manipulação de dados com **Pandas**
* Estatística descritiva (média, mediana, desvio padrão, etc.)
* Estrutura de projeto em Python (`if __name__ == "__main__":`)
* Boas práticas de documentação e tratamento de erros

---

## 💡 Próximos Passos

Planejo evoluir este projeto para incluir:

* Geração automática de **gráficos** (histogramas, boxplots)
* Exportação de relatórios em `.html` ou `.pdf`
* Interface simples com **Streamlit**

---

## 👨‍💻 Autor

**Lindomar dos Santos Cabral**
📍 Recife - PE
🎓 Pós-graduando em Inteligência Artificial (Facuminas)
🎓 Pós-graduado em Engenharia de Software (Unifaveni)
💼 Desenvolvedor de Sistemas e entusiasta em Inteligência Artificial

📫 [LinkedIn](https://www.linkedin.com/in/lindomar-cabral/)
🐙 [GitHub](https://github.com/lindomarcabral)

---

## 🏷️ Licença

Este projeto é distribuído sob a licença **MIT** — sinta-se à vontade para usar, estudar e melhorar.

