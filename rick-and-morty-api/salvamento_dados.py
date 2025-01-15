from extraindo_api_df import extrair_api
import os
import pandas as pd 
import pyarrow as pa # Parquet
import pyarrow.parquet as pq

def salvar_csv(data, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    csv_path = os.path.join(folder, 'data.csv')
    data.to_csv(csv_path, index=False)
    return csv_path

def salvar_excel(data, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    excel_path = os.path.join(folder, 'data.xlsx')
    data.to_excel(excel_path, index=False)
    return excel_path

def salvar_parquet(data, folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

    parquet_path = os.path.join(folder, 'data.parquet')
    table = pa.Table.from_pandas(data)
    pq.write_table(table, parquet_path)
    return parquet_path


if __name__ == '__main__':
    base_url = "https://rickandmortyapi.com/api/character"
    data = extrair_api(base_url)

    # caminho do diretório do arquivo atual
    path = os.path.dirname(os.path.abspath(__file__))
    folder_name = os.path.join(path, 'datasets')

    csv = salvar_csv(data, folder_name)
    print(f"Arquivo CSV salvo em: {csv}")

    excel = salvar_excel(data, folder_name)
    print(f"Arquivo Excel salvo em: {excel}")

    parquet = salvar_parquet(data, folder_name)
    print(f"Arquivo Parquet salvo em: {parquet}")
