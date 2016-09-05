from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from flask import Flask
from scrape_job import scrape_job
from router import routes

def _initialize_scrape_job():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scrape_job, 'cron', hour=0, timezone='UTC')
    scheduler.start()

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug

    # Setup routes
    for route, handler in routes().items():
        app.add_url_rule(route, view_func=handler)

    return app

if __name__ == '__main__':
    # Initialize scrape job here
    _initialize_scrape_job()

    app = create_app(debug=True)
    app.run()
