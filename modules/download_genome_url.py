import requests

def download_genome_url(entrada):
    """
    Lê um arquivo .txt OU uma lista de links e baixa apenas os arquivos .fna.
    """
    if isinstance(entrada, str):
        with open(entrada, "r") as f:
            links = [linha.strip() for linha in f if linha.strip()]
    elif isinstance(entrada, list):
        links = [linha.strip() for linha in entrada if linha.strip()]
    else:
        raise TypeError("A entrada deve ser um caminho de arquivo (.txt) ou uma lista de links.")

    fna_links = [link for link in links if link.endswith(".fna")] # Change here the ending if needed

    if not fna_links:
        print("Nenhum link .fna encontrado.") # Change here the ending if needed
        return

    for link in fna_links:
        nome_arquivo = link.split("/")[-1]
        print(f"Baixando {nome_arquivo} ...")

        try:
            resposta = requests.get(link, timeout=30)
            resposta.raise_for_status()
            with open(nome_arquivo, "wb") as f:
                f.write(resposta.content)
            print(f"Download concluído: {nome_arquivo}")
        except requests.RequestException as e:
            print(f"Erro ao baixar {nome_arquivo}: {e}")
