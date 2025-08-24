def exportar_planilha(df_final):
    df_final.to_excel('output/vr_final.xlsx', index=False)
