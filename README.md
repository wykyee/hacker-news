# hacker-news

**Link for Postman API documentaion**:

``https://documenter.getpostman.com/view/11856566/T1DwatP3?version=latest#733e5894-74d7-5583-4e8c-a7d31188638a``

**Step for running downloaded project**:
*With Docker*:
  1. Set custom settings in .env.dev
  2. sudo docker-compose build
  3. sudo docker-compose up -d
  4. sudo docker-compose exec web python manage.py migrate --noinput
  5. sudo docker-compose exec web python manage.py createsuperuser
  6. sudo docker-compose logs -f
  7. start redis server
  8. celery -A HackerNews worker -B -l INFO    (for daily task)

**Steps for local testing**:
*all data for POST requests is in API documentaion*
1. Create user `http://127.0.0.1:8000/api/user/` POST request
2. User authentication `http://127.0.0.1:8000/api/user/token-auth/` POST request. Token in response will be used for next authentication.
3. Create new post `http://127.0.0.1:8000/api/post/` POST request
4. Check if it is created `http://127.0.0.1:8000/api/post/` GET request
5. Upvote post `http://127.0.0.1:8000/api/post/1/upvote/` POST request.
6. Check this post data `http://127.0.0.1:8000/api/post/1/` GET request
7. Create comment to this post `http://127.0.0.1:8000/api/comments/?post_id=1` POST request.
8. Create nested comment to comment `http://127.0.0.1:8000/api/comments/?post_id=1&parent_id=1` POST request.
9. Upvote some comment `http://127.0.0.1:8000/api/comments/1/upvote/` POST request.
10. Check again data about post.
