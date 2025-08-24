from agents.validation_agent import encontrar_coluna_id
import pandas as pd

df_teste = pd.DataFrame(columns=['Cadastro', 'Nome', 'Valor'])
coluna_id = encontrar_coluna_id(df_teste)
print("🧪 Coluna de identificação encontrada:", coluna_id)
