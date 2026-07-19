from utils.github_client import GitHubClient

client = GitHubClient()

STAR_RANGES = [

    "stars:>=5000",

    "stars:1000..4999",

    "stars:500..999",

    "stars:100..499",

    "stars:50..99"

]

repositories = []

seen = set()

for star_range in STAR_RANGES:

    print(f"\nSearching {star_range}")

    params = {

        "q": f"language:Python fork:false archived:false {star_range}",

        "sort": "stars",

        "order": "desc",

        "per_page": 100,

        "page": 1

    }

    data, headers = client.get(
        "/search/repositories",
        params
    )

    for repo in data["items"]:

        if repo["id"] in seen:
            continue

        seen.add(repo["id"])

        repositories.append(repo)

print(f"\nCollected {len(repositories)} repositories.")