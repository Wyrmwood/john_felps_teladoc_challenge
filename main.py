"""
Teladoc Challenge
"""
import requests
import yaml

URL = "https://jsonmock.hackerrank.com/api/movies/search/"


def query_title(query: str) -> list[str]:
    """
    Query a title at the endpoint, parse the total_pages and retrieve all titles matching the query.

    Args:
        query: A string or substring of a movie title (case-insensitive)

    Returns:
        A sorted list of matching titles in the mock database
    """
    retrieved_titles = []
    response = requests.get(URL, params={"Title": query})
    data = response.json()
    pages = data["total_pages"]
    for page in range(1, pages + 1):
        params = {"Title": query, "page": page}
        response = requests.get(URL, params=params)
        page_data = response.json()["data"]
        retrieved_titles.extend([_["Title"] for _ in page_data])

    return sorted(retrieved_titles)


if __name__ == "__main__":
    for NAME in "batman", "superman", "spiderman":
        TITLES = query_title(NAME)
        print(yaml.safe_dump(TITLES))
        print(len(TITLES))
