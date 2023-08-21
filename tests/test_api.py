import allure
import pytest
from base.API.api import (get_all_user_info, get_random_id_and_email, get_posts_by_user_id, verify_post_id, make_new_post_for_user)
from base.retry import retry
from logging_config import (attach_log_file)
import logging_config
logger = logging_config.setup_custom_logger('root')



@pytest.mark.api
class TestAPI:
    @allure.title('Get random ID and email')
    @retry(max_attempts=2, delay=2) # We could use such libraries as flaky or rerunfailures to rerun flaky tests, or here is my own decorator
    def test_rest_api_test(self, attach_log_file):
        get_user_info_response = get_all_user_info()
        user_id = get_random_id_and_email(get_user_info_response)
        get_posts_response = get_posts_by_user_id(user_id)
        verify_post_id(get_posts_response)
        make_new_post_for_user(user_id)