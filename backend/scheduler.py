import sys
import os
sys.path.append(os.path.abspath('../scraper'))
from apscheduler.schedulers.background import BackgroundScheduler
from scrapy.crawler import CrawlerProcess
from scraper.spiders.deals_spider import DealsSpider
import time

def scrape_deals():
    process = CrawlerProcess()
    process.crawl(DealsSpider)
    process.start()

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_deals, 'interval', hours=1)  # Run every hour
    scheduler.start()
    print("Scheduler started.")

if __name__ == "__main__":
    start_scheduler()
    while True:
        time.sleep(1)
