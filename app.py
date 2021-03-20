"""
Application for scraping the a2oj.com ladders and storing it in an excel file.
"""

from app.scrapper import Scrapper

# config

URL = "https://a2oj.com/"
LADDERS_URL = "Ladders.html"


if __name__ == "__main__":
    scrapper = Scrapper(URL, LADDERS_URL)
    scrapper.start()

