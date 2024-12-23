from apscheduler.schedulers.background import BackgroundScheduler
import time

def scrape_deals():
    print(f"Scraping deals... {time.ctime()}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_deals, 'interval', minutes=60)  # Run every hour
    scheduler.start()
    print("Scheduler started.")

if __name__ == "__main__":
    start_scheduler()
    while True:
        time.sleep(1)
