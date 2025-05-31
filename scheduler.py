# scheduler.py
import schedule
import time
from main import run_analysis

def run_schedule():
    schedule.every(1).hours.do(run_analysis)
    while True:
        schedule.run_pending()
        time.sleep(1)
