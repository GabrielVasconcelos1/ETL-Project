import pandas as pd
import os  # manipular diretorios do sistema operacional. nativo
import glob  # manipular arquivos em massa globalmente. nativo

# caminho para ler arquivos
folder_path = 'src\\data\\raw'
# isso trará um array com todos os caminhos da pasta.
# listar todos os arquivos excel na pasta especificada
# join - juntar , path - letura da pasta
# pega todos os arquivos na extensão .xlsx dentro do diretorio src/data/raw
excel_files = glob.glob(os.path.join(folder_path, '*.xlsx'))
if not excel_files:
    print("Nenhum arquivo Excel encontrado na pasta especificada.")
else:
    # Data Frame real
    dfs = []
    # tratamento de dados na df_Temp
    for excel_file in excel_files:
        try:
            # lê todos os arquivos excel encontrados na pasta
            # Em um Data Frame Temporário
            df_Temp = pd.read_excel(excel_file)
            # pega o nome do arquivo
            file_name = os.path.basename(excel_file)
            # formata arquivo como uma nova coluna no Data Frame temporario.
            # adicionando a coluna location (local)
            # comparando o termo brasil, frança e italiano no nome do arquivo
            # e atribuindo o valor correspondente a nova coluna location (local)
            if 'brasil' in file_name.lower():
                df_Temp['location'] = 'br'
            elif 'france' in file_name.lower():
                df_Temp['location'] = 'fr'
            elif 'italian' in file_name.lower():
                df_Temp['location'] = 'it'

           # criação coluna campanha
            df_Temp['campaign'] = df_Temp['utm_link'].str.extract(
                r'utm_campaign=(.*)')
            # adiciona o Data Frame temporário a lista de Data Frames
            dfs.append(df_Temp)
        except Exception as e:
            print(f"Erro ao ler o arquivo {excel_file}: {e}")


if dfs:
    # concatena todos os Data Frames temporários em um único Data Frame na memoria !
    result = pd.concat(dfs, ignore_index=True)
    # caminho de saida para salvar o arquivo
    output_file = os.path.join('src', 'data', 'ready', 'clean.xlsx')
    # salva o Data Frame resultante da memoria em um arquivo Excel!
    # motor de escrita do excel configuração. na variavel writer, com o caminho padrão e depois o motor de escrita.
    writer = pd.ExcelWriter(output_file, engine='xlsxwriter')
    # output_path = 'src\\data\\ready\\netflix_data.xlsx'
    # leva os dados do resultado a serem escritos no motor de excel configurado.
    result.to_excel(writer, index=False)
    # salva o arquivo de excel da variavel result.
    writer.close()
else:
    print("nenhum dado a ser salvo")
