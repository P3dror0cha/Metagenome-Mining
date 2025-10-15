import requests
import json 

def MGnify_search():
    '''
    Faz a pesquisa de vários IDs de amostras interessantes.

    Parâmetros:
    url: Link que será utilizado na pesquisa.
    '''
    lista_ids = []
    url_da_pesquisa = "https://www.ebi.ac.uk/metagenomics/api/v1/biomes/root:Environmental:Aquatic:Marine/genomes"
    resposta = requests.get(url_da_pesquisa)

    if resposta.status_code == 200:
        dados_json = resposta.json()
        arquivo = "aquatic_freshwater_ice.download.json"

        with open(arquivo, "w") as i:
            json.dump(dados_json, i, indent=4)
    
        lista_ids = [item["id"] for item in dados_json.get("data", [])]
        print(f"{len(lista_ids)} IDs encontrados")

        arquivo_ids = "aquatic_freshwater_ice_ids.txt"
        with open(arquivo_ids, "w") as f:
            for id_study in lista_ids:
                f.write(id_study + "\n")

        return arquivo, lista_ids
    else:
        print(f"Deu problema no status {resposta.status_code}")

    return None, []
