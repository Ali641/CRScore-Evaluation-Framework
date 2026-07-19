from utils.github_client import GitHubClient

client = GitHubClient()

data, headers = client.get("/user")

print(data["login"])
print("Connected Successfully!")