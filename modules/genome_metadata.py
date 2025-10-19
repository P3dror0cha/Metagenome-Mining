import pandas as pd

def genome_metadata(dados_json, lista_ids):
    """
    Carrega o JSON do arquivo e processa os genomas.
    
    Parâmetros:
    caminho_arquivo (str): Caminho para o arquivo JSON
    lista_ids (list): Lista de IDs para filtrar
    """
    dados_processados = []
    
    for amostra in dados_json['data']:
        if amostra['id'] in lista_ids:
            linha = {'id': amostra['id']}
            if 'attributes' in amostra:
                linha.update(amostra['attributes'])
            dados_processados.append(linha)
    
    return pd.DataFrame(dados_processados)
