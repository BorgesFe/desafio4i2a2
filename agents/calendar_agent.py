import pandas as pd

def calcular_dias_uteis(row, dias_uteis_df, ferias_df, desligados_df):
    estado = row.get('ESTADO', None)
    matricula = row.get('MATRICULA')

    # 🔍 Busca os dias úteis por estado
    filtro = dias_uteis_df[dias_uteis_df['ESTADO'] == estado]
    dias_uteis = filtro['DIAS UTEIS'].values[0] if not filtro.empty else 0

    # 🏖️ Verifica se está de férias
    if matricula in ferias_df['MATRICULA'].values:
        dias_ferias = ferias_df.loc[
            ferias_df['MATRICULA'] == matricula, 'DIAS DE FERIAS'
        ].values[0]
        dias_uteis -= dias_ferias

    # 📆 Verifica se foi desligado
    if matricula in desligados_df['MATRICULA'].values:
        if 'DATA DEMISSAO' in desligados_df.columns:
            data_desligamento = desligados_df.loc[
                desligados_df['MATRICULA'] == matricula, 'DATA DEMISSAO'
            ].values[0]

            if pd.notnull(data_desligamento):
                data_desligamento = pd.to_datetime(data_desligamento)

                # Protege contra divisão por zero
                if dias_uteis > 0:
                    if data_desligamento.day <= 15:
                        dias_uteis = round(dias_uteis * 0.5, 0)
                    else:
                        proporcao = data_desligamento.day / dias_uteis
                        dias_uteis = round(dias_uteis * proporcao, 0)
                else:
                    print(f"⚠️ Dias úteis = 0 para matrícula {matricula} no estado {estado}.")
        else:
            raise KeyError("Coluna 'DATA DEMISSAO' não encontrada no DataFrame de desligados.")

    # 🔒 Garante que o valor final não seja negativo
    dias_uteis = max(dias_uteis, 0)

    return dias_uteis
