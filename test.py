import unittest

from article import Article


class TestArticle(unittest.TestCase):
    def test_get_page_data(self):
        page_data = Article.get_page_data(1)
        self.assertTrue(page_data["page"])
        self.assertEqual(page_data["page"], 1)
        self.assertTrue(page_data["per_page"])
        self.assertTrue(page_data["total"])
        self.assertTrue(page_data["total_pages"])
        self.assertTrue(page_data["data"])

    def test_sort_articles_by_number_of_comments(self):
        articles = [
            {"title": "This is my first article", "number_of_comments": 123},
            {"title": "This is my second article", "number_of_comments": 456},
            {"title": "This is my third article", "number_of_comments": 789}
        ]
        sorted_articles = Article.sort_articles_by_number_of_comments(articles)
        self.assertEqual(sorted_articles[0]["number_of_comments"], 789)
        self.assertEqual(sorted_articles[1]["number_of_comments"], 456)
        self.assertEqual(sorted_articles[2]["number_of_comments"], 123)


