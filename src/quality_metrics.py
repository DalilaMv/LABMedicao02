import statistics
from github import Github
import git
import os
from dotenv import load_dotenv
import pandas as pd

def handle_metrics(nameWithOwner, url, df_arq2, stars, age, releases):
    print("1. CLONE DO REPOSITORIO")
    load_dotenv()
    token = os.environ["token"]

    g = Github(token)
    repo = g.get_repo(nameWithOwner)
    url = repo.clone_url
    if os.path.isdir(nameWithOwner):
        print("A pasta existe!")
    else:
        git.Repo.clone_from(url, nameWithOwner)

    print("2. RODA O CK")
    os.system(f'java -jar ../../Downloads/ck.jar {nameWithOwner}')

    print("3. SUMARIZA OS DADOS")
    df = pd.read_csv("class.csv")
    if not df.empty:
        cbo_median = statistics.median(df["cbo"])
        dit_max = df["dit"].max()
        lcom_median = statistics.median(df["lcom"])
        total_loc = df["loc"].sum()
    else:
        print("arquivo class.csv vazio...")
        cbo_median = 0
        dit_max = 0
        lcom_median = 0
        total_loc = 0
    
    results_df = pd.DataFrame({
        "nameWithOwner": nameWithOwner,
        "Url": url,
        "Estrelas": stars,
        "Idade (anos)": age,
        "Número de releases": releases,
        "CBO Median": [cbo_median],
        "DIT Max": [dit_max],
        "LCOM Median": [lcom_median],
        "LOC Total": [total_loc]
    })
    df_concatenado = pd.concat([results_df, df_arq2], ignore_index=True)
    df_concatenado.to_csv("arquivo2.csv", index=False)

    print("4. DELETA OS DADOS")
    os.system(f'rm -rf {nameWithOwner.split("/")[0]}')

    return df_concatenado

def main():
    colunas = ["nameWithOwner", "CBO Median", "DIT Max", "LCOM Median", "LOC Total"]
    df_arq2 = pd.DataFrame(columns=colunas)

    if not os.path.isfile("arquivo2.csv"):
        # Se o arquivo não existir, cria um novo arquivo vazio (condição criada para evitar erro na primeira execução)
        with open("arquivo2.csv", "w") as arquivo:
            arquivo.write("")
    else:
        df_arq2 = pd.read_csv("arquivo2.csv")

    df = pd.read_csv("arquivo1.csv")
    for index, row in df.iterrows():
        if not df_arq2.empty and row['Nome'] in df_arq2["nameWithOwner"].values:
            pass
        else:
            nameWithOwner = row['Nome']
            url = row['Url']
            stars = row['Estrelas']
            age = row['Idade (anos)']
            releases = row['Número de releases']
            df_arq2 = handle_metrics(nameWithOwner, url, df_arq2, stars, age, releases)


main()