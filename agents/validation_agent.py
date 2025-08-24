def encontrar_coluna_id(df):
    nomes_validos = ['ID', 'MATRICULA', 'CADASTRO', 'REGISTRO']
    for col in df.columns:
        nome = col.strip().upper()
        if nome in nomes_validos:
            return col
    return None

def validar_todas_planilhas(planilhas_dict):
    """
    Recebe um dicionário de DataFrames e retorna um dicionário com o nome da coluna de ID encontrada em cada um.
    """
    resultados = {}
    for nome, df in planilhas_dict.items():
        if hasattr(df, "columns"):
            coluna_id = encontrar_coluna_id(df)
            resultados[nome] = coluna_id
        else:
            resultados[nome] = "❌ Não é um DataFrame válido"
    print("🔍 Validação de planilhas:")
    for nome, coluna in resultados.items():
        print(f" - {nome}: {coluna}")


    return resultados

def padronizar_colunas(planilhas_dict):
    """
    Padroniza os nomes das colunas de todos os DataFrames:
    - Remove espaços extras
    - Converte para maiúsculas
    - Remove acentos
    """
    import unicodedata

    def limpar_nome(nome):
     nome = nome.strip().upper()
     nome = unicodedata.normalize('NFKD', nome).encode('ASCII', 'ignore').decode('ASCII')
    
    # Correção manual
     if nome == 'SINDICADO':
        return 'SINDICATO'
    
     return nome  # ← esse return precisa estar dentro da função


    for nome, df in planilhas_dict.items():
        if hasattr(df, "columns"):
            df.columns = [limpar_nome(col) for col in df.columns]

