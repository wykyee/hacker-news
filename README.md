# hacker-news

**Link for Postman API documentaion**:

``https://documenter.getpostman.com/view/11856566/T1DwatP3?version=latest#733e5894-74d7-5583-4e8c-a7d31188638a``

**Step for running project**:
1. pyhton3 manage.py migrate
2. pyhton3 manage.py createsuperuser
3. pyhton3 manage.py runserver

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
