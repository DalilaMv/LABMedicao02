from github import Github
import git
import os
from dotenv import load_dotenv
import subprocess

def delete_repo(nameWithOwner): 
    os.system(f'rm -rf src/{nameWithOwner.split("/")[0]}')
    
    return

def summarize(): 
    #ler o class.csv e pegar as metricas 
    #calcular mediana de cada uma das metricas desejadas
    #salvar os dados do repositorio num csv final
    return

def run_ck(nameWithOwner):
    os.system(f'java -jar ../../Downloads/ck.jar src/{nameWithOwner}')
    return

def clone_repo(nameWithOwner, url):

    load_dotenv()

    token = os.environ["token"]

    g = Github(token)

    repo = g.get_repo(nameWithOwner)

    url = repo.clone_url

    git.Repo.clone_from(url, nameWithOwner)

def main():


# ler o csv1 e pra cara repositorio:
    # chama clone_repo passando a url do repositorio
    # chama o ck passando o namewithowner e ele gera o class.csv
    # ler o class.csv e chamar a func de sumarizaçao
    # chamar func de delete 
# ir para o proximo repositorio
