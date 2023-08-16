import allure
import requests
from base.API.api_routes import APIRoutes
import random
import json

@allure.step("Getting all users info")
def get_all_user_info():
    get_user_info_response = requests.get(APIRoutes.users_url)
    assert get_user_info_response.status_code == 200, f'Status code != 200, actual status_code = {get_user_info_response.status_code}'
    return get_user_info_response

@allure.step(f"Getting random userID and it's email")
def get_random_id_and_email(get_user_info_response):
    data = json.loads(get_user_info_response.text)
    # Выбор случайного объекта из списка
    random_user_id_data = random.choice(data)
    # Получение email для выбранного случайного id
    userID = random_user_id_data['id']
    email = random_user_id_data['email']
    # Вывод email
    allure.attach(f"{email}", name="Email", attachment_type=allure.attachment_type.TEXT)
    return userID

@allure.step(f"Getting posts for userID")
def get_posts_by_user_id(userID):
    get_posts_response = requests.get(APIRoutes.posts_url + f'?userId={userID}')
    assert get_posts_response.status_code == 200, f'Status code != 200, actual status_code = {get_posts_response.status_code}'
    return get_posts_response

@allure.step(f"Verify postID's for user posts")
def verify_postid(get_posts_response):
    data = json.loads(get_posts_response.text)
    for postID in data:
        post_id_value = postID["id"]
        assert 1 <= post_id_value <= 100, f"actual postID value = {post_id_value} not in the range from 1 to 100"
