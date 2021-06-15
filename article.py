import requests

from typing import List, Dict


class Article:
    articles_api_url = "https://jsonmock.hackerrank.com/api/articles"

    @classmethod
    def get_page_data(cls, page: int) -> Dict:
        response = requests.get(f"{cls.articles_api_url}?page={page}")
        return response.json()

    @classmethod
    def sort_articles_by_number_of_comments(cls, articles: List[Dict]) -> List[Dict]:
        return sorted(articles, key=lambda i: i["number_of_comments"], reverse=True)
