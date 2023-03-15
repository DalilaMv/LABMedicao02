from github import Github
import git
import os
from dotenv import load_dotenv

load_dotenv()

token = os.environ["token"]

g = Github(token)

repo = g.get_repo('apache/rocketmq')

url = repo.clone_url

git.Repo.clone_from(url, 'apache/rocketmq')