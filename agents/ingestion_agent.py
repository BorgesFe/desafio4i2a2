import pandas as pd

def padronizar_colunas(df):
    df.columns = (
        df.columns
        .str.strip()                      # remove espaços extras
        .str.upper()                     # coloca tudo em maiúsculas
        .str.normalize('NFKD')           # remove acentos
        .str.encode('ascii', errors='ignore')
        .str.decode('utf-8')
    )
    return df


def load_all_data():
    arquivos = {
        "ativos": pd.read_excel("data/ATIVOS.xlsx"),
        "ferias": pd.read_excel("data/FÉRIAS.xlsx"),
        "desligados": pd.read_excel("data/DESLIGADOS.xlsx"),
        "admitidos": pd.read_excel("data/ADMISSÃO ABRIL.xlsx"),
        "sindicato_valor": pd.read_excel("data/sindicato_valor.xlsx"),
        "dias_uteis": pd.read_excel("data/dias_uteis.xlsx"),
        "aprendizes": pd.read_excel("data/APRENDIZ.xlsx"),
        "estagiarios": pd.read_excel("data/ESTÁGIO.xlsx"),
        "afastados": pd.read_excel("data/AFASTAMENTOS.xlsx"),
        "exterior": pd.read_excel("data/EXTERIOR.xlsx")
    }

    # Padroniza todas as colunas de todos os arquivos
    return {k: padronizar_colunas(v) for k, v in arquivos.items()}

