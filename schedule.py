from celery import Celery
from celery.schedules import crontab
from countdown.tasks import update_cover


app = Celery()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(),
        update_cover.s(),
    )