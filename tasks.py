from celery import Celery
import organize_and_store as org
from celery.schedules import crontab

app = Celery('tasks', broker='amqp://localhost//')

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    # Calls test('hello') every 10 seconds.
    sender.add_periodic_task(60.0, add(), name='add every 60')


@app.task
# Runs the actual task
def add():
    org.get_stock_data("btc", "usd", 60, True)
