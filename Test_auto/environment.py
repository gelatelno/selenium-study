import logging

from selenium import webdriver


def before_all(context):
    selenium_logger = logging.getLogger(
        'selenium.webdriver.remote.remote_connection')
    selenium_logger.setLevel(logging.WARN)

    context.driver = webdriver.Chrome(executable_path='/Users/berryhooerry/Desktop/Test_auto/chromedriver')
    context.driver.implicitly_wait(3)


def after_all(context):
    context.driver.quit()