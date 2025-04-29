
  

# Projeto de Estudo de ETL

Este projeto é uma aplicação prática de ETL (Extract, Transform, Load), desenvolvido com o objetivo de consolidar conhecimentos sobre, extração, manipulação de dados usando Python.
algumas pastas não foram colocadas dentro do repositório afim de não pesar o arquivo, porém todos foram criados.
  
## Estrutura do Projeto
#### 1. Pastas:
##### 1.1 Pasta  - src/data/raw: 
Contém os arquivos originais do tipo .xlsx que serão processados, e transformados pelo programa main.py

##### 1.2 Pasta - src/data/ready: 
Será o destino dos arquivos processados e transformados, que estaram em um arquivo de nome Clean.

##### 1.3 Pasta - Venv
pasta criada para criar um espaço virtual dedicado ao projeto.

##### 1.4 Pasta - Doc
pasta criada para colocar arquivos de documentos importantes para o programa.
#### 2. Tecnologias Utilizadas

- Python: Linguagem de programação principal do projeto.

#### 3.Bibliotecas, extensões e módulos :

- pandas: Manipulação e transformação de dados tabulares. (Biblioteca)
- Xlsxwriter: Escrita de arquivos Excel. (Biblioteca)
- os: Gerenciamento de diretórios(acessos ) e manipulação de arquivos. (Módulo do Python)
- glob: Identificação e seleção de arquivos em massa no diretorio.(Módulo do Python)


  
#### 4. Funcionalidades.

##### 4.1 Extração de Dados.
Identifica todos os arquivos Excel na pasta src/data/raw.
##### 4.2 Lê os arquivos encontrados.

##### 4.3 Transformação de Dados.
###### 4.3.1 Criação de uma coluna location.
Tendo como base o nome do arquivo, afim de garantir rastreabilidade e confiabilidade dos dados foi criado no arquivo novo uma coluna location para que possamos rastrear e saber de onde vem os dados.
Exemplos: 
 - 'br' para arquivos que vieram da base de dados "brasil"
 - 'fr' para arquivos que vieram da base de dados "france" 
 - 'it' para arquivos que vieram da base de dados "italian".
###### 4.3.2Criação de uma coluna campaign .
Afim de conseguir melhor visualização dos dados e poder ter melhor aproveitamento das informações ao importar esses dados para criação de um relatório, extraindo informações da coluna utm_link através da expressão.
```python
	 df_Temp['campaign'] = df_Temp['utm_link'].str.extract(r'utm_campaign=(.*)')
```

##### 4.4 Carregamento de Dados.
Consolida todos os arquivos Excel em um único DataFrame, após isso o código salva o resultado transformado em um arquivo Excel chamado clean.xlsx na pasta src/data/ready.

##### 4.5 Tratamento de Erros.
Mensagem exibida caso nenhum arquivo Excel seja encontrado por meio do código.
fazendo assim o tratamento de exceções ao ler arquivos, garantindo que  o processamento continue para os demais arquivos. 
```python
	 except Exception as e:

            print(f"Erro ao ler o arquivo {excel_file}: {e}")
```


  

### Como Executar

1. Certifique-se de ter Python e as bibliotecas necessárias instaladas.
2. Importe os arquivos .xlsx na pasta src/data/raw.
3. Execute o script Python.
4. O arquivo resultante estará na pasta src/data/ready com o nome clean.xlsx.


  

### Propósito

Este projeto foi desenvolvido como parte de um estudo pessoal para entender e implementar os princípios de ETL utilizando Python, assim como garantir aprendizado quanto as boas práticas da criação de um projeto.

A base de dados RAW utilizadas são meramente fictícias e adquiridas por meio de repositório publico no GitHub 
