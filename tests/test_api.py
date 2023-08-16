import allure
from base.API.api import (get_all_user_info, get_random_id_and_email, get_posts_by_user_id, verify_postid)

class TestAPI:
    @allure.title('Get random ID and email')
    def test_get_random_id(self):
        get_user_info_response = get_all_user_info()
        userID = get_random_id_and_email(get_user_info_response)
        get_posts_response = get_posts_by_user_id(userID)
        verify_postid(get_posts_response)