import pandas as pd
import os
import  glob

#Funcao de extract que le e consolida o json

pasta = 'data'
def extrair_dados(pasta: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


#Funcao que transforma

def calcular_kpi_total_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df["Total"] = df["Quantidade"] * df["Venda"]
    return df


#Parametro que vai ser CSV ou Parquet ou os dois
def carregar_dados(df:pd.DataFrame, format_saida: list):
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv("dados.csv",index=False)
        if formato == 'parquet':
            df.to_parquet("dados.parquet",index=False)



def peipeline_kpi_de_vendas(pasta: str, formato_de_saida: list):
    data_frame = extrair_dados(pasta=pasta_argumento)
    data_frame_calculado = calcular_kpi_total_vendas(data_frame)
    carregar_dados(data_frame_calculado, formato_de_saida)
    
    
