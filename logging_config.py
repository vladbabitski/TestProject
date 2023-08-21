import logging
import os
import allure
import pytest

def setup_custom_logger(name):
    # Set formatting for log messages
    formatter = logging.Formatter(fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')

    # Creating a handler for outputting logs to the console
    handler = logging.StreamHandler()
    handler.setFormatter(formatter)

    # Creating a handler for outputting logs to the log file
    logs_dir = os.path.dirname(__file__)
    log_file_path = os.path.join(logs_dir, 'TestProject.log')
    filehandler = logging.FileHandler(log_file_path)
    filehandler.setLevel(logging.DEBUG)

    # Creating a logger object
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(handler)
    logger.addHandler(filehandler)
    return logger


@pytest.fixture(scope="session", autouse=True)
def attach_log_file():
    # Define log file path
    log_file_path = os.path.join(os.path.dirname(__file__)+'\\TestProject.log')

    # Read the log file
    with open(log_file_path, "r") as log_file:
        log_content = log_file.read()
        log_file.close()
    # Attach log to allure
    allure.attach(log_content, name="Log File", attachment_type=allure.attachment_type.TEXT)

    # Clear the log
    with open(log_file_path, "w") as log_file:
        log_file.write("")
        log_file.close()