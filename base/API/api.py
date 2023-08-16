import allure
import requests
from base.API.api_routes import APIRoutes
import random
import json


@allure.step("Getting all users info")
def get_all_user_info():
    # Get all users info
    get_user_info_response = requests.get(APIRoutes.users_url)

    # Check status code value
    assert get_user_info_response.status_code == 200, f'Status code != 200, actual status_code = {get_user_info_response.status_code}'
    return get_user_info_response


@allure.step("Getting random user_id and it's email")
def get_random_id_and_email(get_user_info_response):
    data = json.loads(get_user_info_response.text)

    # Selecting a random object from a list
    random_user_id_data = random.choice(data)

    # Getting user_id and email for selected random id
    user_id = random_user_id_data['id']
    email = random_user_id_data['email']

    # Attacking email to allure report
    allure.attach(f"{email}", name="Email", attachment_type=allure.attachment_type.TEXT)
    return user_id


@allure.step("Getting posts for user_id")
def get_posts_by_user_id(user_id: int):
    # Get all posts for selected user_id
    params = {"userId": user_id}
    get_posts_response = requests.get(APIRoutes.posts_url, params=params)

    # Check status code value
    assert get_posts_response.status_code == 200, f'Status code != 200, actual status_code = {get_posts_response.status_code}'
    return get_posts_response


@allure.step("Verify post_id's for user posts")
def verify_post_id(get_posts_response):
    # Check that post id has correct value
    data = json.loads(get_posts_response.text)
    for post_id in data:
        post_id_value = post_id["id"]
        assert 1 <= post_id_value <= 100, f"actual post_id value = {post_id_value} not in the range from 1 to 100"

@allure.step("Make a new post for user")
def make_new_post_for_user(user_id: int):
    # Define parameters for new post request
    headers = {'Content-Type': 'application/json'}
    data = {
        "userId": user_id,
        "title": "Test title for user's post",
        "body": "This is the text for my post. I hope I did everything right :)"
            }

    # Make a post request
    response_for_post_request = requests.post(APIRoutes.posts_url, json=data, headers=headers)

    # Check status code value
    assert response_for_post_request.status_code == 201, f'Status code != 201, actual status_code = {response_for_post_request.status_code}'