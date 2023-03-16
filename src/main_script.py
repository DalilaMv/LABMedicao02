
import requests
import os
from datetime import datetime
from dotenv import load_dotenv
import csv

load_dotenv()

token = os.environ["token"]
url = os.environ["github_api_url"]
repositories = []

query = '''
query {
  search(query: "stars:>100, language: Java", type: REPOSITORY, first: 100, after: null) {
    nodes {
      ... on Repository {
        nameWithOwner
        stargazerCount
        createdAt
        url
        releases {
          totalCount
        }
      }
    }
    pageInfo {
      endCursor
      hasNextPage
    }
  }
}
'''

headers = {"Authorization": "Bearer " + token}
count = 0
data = []
cursor = None

while count < 1000:
    if cursor:
        query_with_cursor = query.replace(
            'after: null', 'after: "%s"' % cursor)
        response = requests.post(
            url, json={"query": query_with_cursor}, headers=headers)
    else:
        response = requests.post(url, json={"query": query}, headers=headers)

    if response.status_code == 200:
        repos = response.json()['data']['search']['nodes']
        page_info = response.json()['data']['search']['pageInfo']
        cursor = page_info['endCursor']
        has_next_page = page_info['hasNextPage']
        for repo in repos:
            count += 1
            name = repo['nameWithOwner']
            stars = repo['stargazerCount']
            created_at = datetime.strptime(
                repo['createdAt'], '%Y-%m-%dT%H:%M:%SZ')
            age = round((datetime.utcnow() - created_at).days / 365.25, 2)
            num_releases = repo['releases']['totalCount']
            repo_url = repo['url']
            row = [count, name, stars, age, num_releases, repo_url]
            data.append(row)
        print(count)
    else:
        continue

with open('arquivo1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Número', 'Nome', 'Estrelas',
                    'Idade (anos)', 'Número de releases', 'Url'])
    for row in data:
        writer.writerow(row)
