"""importação das libs."""
import string
import requests
import os
import ast
import pandas as pd
import awswrangler as wr
from datetime import date

"""Função responsavél pelo consumo da API Peak_Condition."""
"""Retornará uma lista com nome e id das montanhas."""
"""Os dados serão utilizados para request na API e consultar as condições."""

###################################
# Variavéis API ###################
###################################
url = os.environ.get("API-URL")
key = os.environ.get('API-KEY')
host = os.environ.get('API-HOST')
###################################
# Variavéis Projeto################
###################################
bucket = os.environ.get("STORAGE")
prefix = os.environ.get("PREFIX")


def api_requests(url):
    """Esta função recebe os argumentos para realizar o request na API\
    e retorna uma lista com nomes e id das montanhas.

    Args:
        url (string): url da API
    Returns:
        list: nomes e id das montanhas
    """
    global key
    global host

    # Uma lista com todas as letras do alfabeto
    initial_mountain_name = list(string.ascii_lowercase)

    mountains = []  # Uma lista que receberá os dados de todas as montanhas
    try:
        for initial in initial_mountain_name:
            querystring = {"query": initial}

            headers = {
                "X-RapidAPI-Key": f"{key}",
                "X-RapidAPI-Host": f"{host}"
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring
                )
            if response.status_code == 200:
                for name in ast.literal_eval(response.text):
                    mountains.append(name)
            else:
                print(f"Response:{response.status_code}")
                return response.status_code

        print(f"Request realizada com sucesso : {len(mountains)} arquivos.")
        save_parquet(mountains, bucket, prefix)
        return "Success"

    except Exception as exc:
        print(f"Erro {exc}")
        return exc


def save_parquet(dados, bucket, prefix):
    """Esta função realiza a escrita dos dados em parquet na bucket de raw.

    Args:
        dados (dataframe): dados
        bucket (string): nome do bucket
        prefix (string): camada/tabela

    Returns:
        dict: retorna um dicionário com os arquivos e partições salvas no s3.
    """
    print("---- Gerando o DF ----")
    df = pd.DataFrame(dados)
    print("---- Salvando Arquivo Parquet no S3 -----")
    response = wr.s3.to_parquet(
        df=df,
        path=f"s3://{bucket}/{prefix}/base/base_{date.today().strftime('%Y%m%d')}.parquet"
    )
    print(f"Arquivos Salvos : {response['paths']}")
    return response


if __name__ == '__main__':
    api_requests("https://peak-conditions.p.rapidapi.com/search")
