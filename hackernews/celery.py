import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hackernews.settings")

app = Celery("hackernews")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


app.conf.beat_schedule = {
    "delete-all-upvotes-everyday": {
        "task": "apps.posts.tasks.delete_all_posts_votes",
        "schedule": crontab(minute=0, hour=0),
    },
}
