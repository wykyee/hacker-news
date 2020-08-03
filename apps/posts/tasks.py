from HackerNews.celery import app

from apps.posts.services import get_votes_to_posts


@app.task
def delete_all_posts_votes():
    votes = get_votes_to_posts()
    votes.delete()
