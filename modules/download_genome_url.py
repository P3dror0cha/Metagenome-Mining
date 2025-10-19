def download_genome_url(input, filtro=".fna"):
    """
    Lê um arquivo .txt OU uma lista de links e baixa apenas os arquivos que você quer filtrando pelo tipo de arquivo.
    
    Parâmetros:
    input: caminho do arquivo .txt contendo os links OU uma lista de links.
    filtro: extensão do arquivo a ser baixado. Default: ".fna"
    """
    if isinstance(input, str):
        with open(input, "r") as f:
            links = [linha.strip() for linha in f if linha.strip()]
    elif isinstance(input, list):
        links = [linha.strip() for linha in input if linha.strip()]
    else:
        raise TypeError("O input deve ser um caminho de arquivo (.txt) ou uma lista de links.")

    fna_links = [link for link in links if link.endswith(filtro)] 

    if not fna_links:
        print(f"Nenhum link {filtro} encontrado.") 
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

        try:
            resposta = requests.get(link, timeout=30)
            resposta.raise_for_status()
            with open(nome_arquivo, "wb") as f:
                f.write(resposta.content)
            print(f"Download concluído: {nome_arquivo}")
        except requests.RequestException as e:
            print(f"Erro ao baixar {nome_arquivo}: {e}")

