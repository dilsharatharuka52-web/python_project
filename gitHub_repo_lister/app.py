import requests
import os
from  dotenv import load_dotenv

load_dotenv()

URL = "https://api.github.com/user/repos"
token = os.getenv("API_KEY")


if not token:
    print("Error: GitHub API token not fount!")
    exit()


headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    URL,
    headers=headers,
    params={
        "per_page" : 100,
        "sort" : "updated"
    },
    timeout=15
)

if response.status_code == 200:

    repos = response.json()

    print("\n================================")
    print("      MY GITHUB REPOSITORIES")
    print("================================\n")

    for index, repo in enumerate(repos, start=1):
        print(f"{index}. {repo['name']}")
        print(f"   Description: {repo['description']}")
        print(f"   Language: {repo['language'] or 'Not specified'}")
        print(f"   Stars: {repo['stargazers_count']}")
        print(f"   URL: {repo['html_url']}")
        print("-" * 40)

    # 9. Count repositories
    print(f"\nTotal repositories: {len(repos)}")


elif response.status_code == 401:
    print("Error: Invalid GitHub token!")

elif response.status_code == 403:
    print("Error: API access forbidden or rate limit exceeded!")

else:
    print("Error:", response.status_code)
    print(response.text)




