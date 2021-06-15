#!/usr/bin/env python3

import argparse

from typing import List, Dict
from article import Article

# Initialize parser
parser = argparse.ArgumentParser(description="Return top commented articles from jsonmock.hackerrank.com")

# Adding optional argument
parser.add_argument("-r", "--Results", help="Number of results")

# Read arguments from command line
args = parser.parse_args()

NUMBER_OF_RESULTS = 10  # Number of results to return

if args.Results:
    print(f"Number of results: {args.Results}")
    NUMBER_OF_RESULTS = int(args.Results)

articles = []


def show_top_result_table(results: List[Dict]) -> None:
    print(f"TOP {NUMBER_OF_RESULTS}:")
    for index, item in enumerate(results):
        print(f"{index+1}. {item['title']} | {item['number_of_comments']}")


def get_page_articles(page_data: List[Dict]) -> None:
    for article in page_data:
        if article["title"] or article["story_title"]:
            articles.append({
                "title": article["title"] if article["title"] else article["story_title"],
                "number_of_comments": article["num_comments"] if article["num_comments"] else 0
            })


def get_suitable_articles() -> None:
    first_page_data = Article.get_page_data(1)
    get_page_articles(first_page_data["data"])
    for i in range(2, first_page_data["total_pages"] + 1):
        page_data = Article.get_page_data(i)
        get_page_articles(page_data["data"])

    # Show statistics
    print(f"Total articles: {first_page_data['total']}")
    print(f"Total pages: {first_page_data['total_pages']}")
    print(f"Total suitable articles: {len(articles)}")


# Connect to Hacker rank and get suitable articles
try:
    get_suitable_articles()
    sorted_articles = Article.sort_articles_by_number_of_comments(articles)
    top_articles = sorted_articles[0:NUMBER_OF_RESULTS]
    show_top_result_table(top_articles)
except Exception as e:
    print(f"Something went really wrong. Error: {str(e)}")
