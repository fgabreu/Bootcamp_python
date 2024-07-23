from etl import peipeline_kpi_de_vendas

pasta_argumento = 'data'
formato_de_saida: list = ["csv", "parquet"]

peipeline_kpi_de_vendas(pasta_argumento, formato_de_saida)