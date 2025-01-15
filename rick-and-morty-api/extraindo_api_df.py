import requests
import pandas as pd

def extrair_api(base_url):
    page = 1 # começa na pagina 1
    all_characters = []

    while True:
        response = requests.get(f'{base_url}?page={page}')

        if response.status_code != 200:
            break
    
        data = response.json() # converte para dicionário Python

        all_characters.extend(data['results']) # adiciona personagens na lista de personagens da API
            
        if not data["info"]["next"]:
            break # se não houver proxima pagina
        
        page +=1

    df = pd.DataFrame(all_characters) # transformando em dataframe

    df = df[["id", "name", "status", "species", "gender", "type", "origin", "location"]] # seleciona as colunas relevantes da API

    df["origin_name"] = df["origin"].apply(lambda x: x["name"])
    df["location_name"] = df["location"].apply(lambda x: x["name"])
    df = df.drop(columns=["origin", "location"])
            
    print(df.info)
    return df

if __name__ == "__main__":
    base_url = "https://rickandmortyapi.com/api/character"
    extrair_api(base_url)


        
   

