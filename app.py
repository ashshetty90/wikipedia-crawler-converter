
from src.crawler import Crawler
from src.converter import Converter


def start():
    crawler = Crawler()
    crawler_results = crawler.crawl()
    for crawler_result in crawler_results:
        attribute_string = crawler_result.get('attribute_string')
        attribute_usd_price = crawler_result.get('attribute_usd_price')
        attribute = crawler_result.get('attribute')
        converter = Converter()
        print attribute,converter.convert(attribute_usd_price,attribute_string)

if __name__ == "__main__":
    start()