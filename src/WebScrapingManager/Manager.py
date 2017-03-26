from Scraper import Scraper
# This manager creates a


def make_scraper(name, age, major):
    scraper = Scraper(name, age, major)
    return scraper


make_scraper(10, "", "")