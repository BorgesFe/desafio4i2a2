import pandas as pd

import pandas as pd
from agents.calendar_agent import calcular_dias_uteis

def calcular_valores(row, sindicato_valor_df, dias_uteis_df, ferias_df, desligados_df):
    dias = calcular_dias_uteis(row, dias_uteis_df, ferias_df, desligados_df)

    filtro = sindicato_valor_df[sindicato_valor_df['ESTADO'] == row['ESTADO']]
    valor_dia = filtro['VALOR'].values[0] if not filtro.empty else 0

    total = dias * valor_dia
    empresa = round(total * 0.8, 2)
    colaborador = round(total * 0.2, 2)

    return pd.Series([dias, total, empresa, colaborador])
