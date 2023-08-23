import allure
import pytest
from base.API.api import (get_all_user_info, get_random_id_and_email,
                          get_posts_by_user_id, verify_post_id, make_new_post_for_user)
from flaky import flaky


@pytest.mark.api
class TestAPI:
    @allure.title('API test')
    @flaky(max_runs=3, min_passes=1)
    def test_rest_api(self):
        get_user_info_response = get_all_user_info()
        user_id = get_random_id_and_email(get_user_info_response)
        get_posts_response = get_posts_by_user_id(user_id)
        verify_post_id(get_posts_response)
        make_new_post_for_user(user_id)
