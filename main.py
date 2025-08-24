# 1. Importações dos agentes
from agents.ingestion_agent import load_all_data
from agents.validation_agent import validar_todas_planilhas, encontrar_coluna_id, padronizar_colunas
from agents.filtering_agent import apply_exclusions
from agents.calculation_agent import calcular_valores
from agents.export_agent import exportar_planilha

import pandas as pd

# 2. Função principal
def main():
    print("🚀 Iniciando automação de VR/VA...")

    # 3. Carregar e padronizar dados
    data = load_all_data()
    padronizar_colunas(data)
    print("✅ Colunas de dias_uteis:", data['dias_uteis'].columns.tolist())
    print("✅ Colunas de sindicato_valor:", data['sindicato_valor'].columns.tolist())

    # 4. Validar estrutura das planilhas
    validar_todas_planilhas(data)

    # 5. Aplicar regras de exclusão
    base_filtrada = apply_exclusions(
        data['ativos'],
        data['aprendizes'],
        data['estagiarios'],
        data['afastados'],
        data['exterior']
    )
    print(f"🧹 Base filtrada: {len(base_filtrada)} colaboradores elegíveis.")

    # 6. Validar campos obrigatórios
    col_id = encontrar_coluna_id(base_filtrada)

    # Verifica se a coluna 'ESTADO' existe antes de aplicar dropna
    if 'ESTADO' not in base_filtrada.columns:
        raise KeyError("❌ A coluna 'ESTADO' não foi encontrada na base filtrada. Verifique a origem dos dados.")
    
    base_valida = base_filtrada.dropna(subset=[col_id, 'ESTADO'])

    # 7. Calcular valores de VR
    base_valida[['DIAS', 'VR_TOTAL', 'EMPRESA', 'COLABORADOR']] = base_valida.apply(
        lambda row: calcular_valores(
            row,
            data['sindicato_valor'],
            data['dias_uteis'],
            data['ferias'],
            data['desligados']
        ),
        axis=1
    )
    print("🧮 Cálculo de VR concluído.")

    # 8. Exportar planilha final
    exportar_planilha(base_valida)
    print("📤 Planilha final gerada em /output/vr_final.xlsx")

# 9. Executar
if __name__ == "__main__":
    main()
