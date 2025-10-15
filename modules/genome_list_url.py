import requests

def genome_list_url(lista_ids, arquivo_saida="links_download.txt"):
    '''
    Faz a pesquisa das urls associadas com cada uma das amostras. Junta tudo em um txt único.
    '''
    lista_download = []
    for ids in lista_ids:
        print(f"Baixando links para o ID {ids}")
        url = f"https://www.ebi.ac.uk/metagenomics/api/v1/genomes/{ids}/downloads"
        resposta =requests.get(url)
        print(resposta.status_code)
        print(resposta.text[:1000])
        if resposta.status_code == 200:
            url_ids = [item["links"]["self"] for item in resposta.json().get("data", [])]
            lista_download.extend(url_ids)
        else:
            print("Erro na requisição.")
    with open(arquivo_saida, "w") as f:
        for link in lista_download:
            f.write(link + "\n")
    print (lista_download)
    return lista_download