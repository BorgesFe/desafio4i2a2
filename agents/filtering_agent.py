import pandas as pd
from agents.validation_agent import encontrar_coluna_id

def apply_exclusions(ativos, aprendizes, estagiarios, afastados, exterior):
    # Detecta automaticamente a coluna de ID em cada planilha
    col_aprendiz = encontrar_coluna_id(aprendizes)
    col_estagiario = encontrar_coluna_id(estagiarios)
    col_afastado = encontrar_coluna_id(afastados)
    col_exterior = encontrar_coluna_id(exterior)
    col_ativos = encontrar_coluna_id(ativos)

    if not all([col_aprendiz, col_estagiario, col_afastado, col_exterior, col_ativos]):
        raise ValueError("⚠️ Uma ou mais planilhas estão sem coluna de identificação válida.")

    # Concatena todas as matrículas a serem excluídas
    excluir = pd.concat([
        aprendizes[col_aprendiz],
        estagiarios[col_estagiario],
        afastados[col_afastado],
        exterior[col_exterior]
    ])

    # Aplica exclusão na base de ativos
    return ativos[~ativos[col_ativos].isin(excluir)]
