import pytest
import allure
from selenium.webdriver.common.by import By
from utils import Util as Util


@pytest.mark.usefixtures("test_setUp")
class TestDemoGuru99:

    def test_valid_userID_passWord(self):
        driver = self.driver
        # Enter Valid user ID
        driver.find_element(By.NAME, "uid").clear()
        driver.find_element(By.NAME, "uid").send_keys(Util.USER_NAME)

        # Enter Valid password
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys(Util.PASSWORD)

        # Click login button
        driver.find_element(By.NAME, "btnLogin").click()
        # allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)

    def test_verify_valid_login(self):
        driver = self.driver
        # Enter Valid user ID
        driver.find_element(By.NAME, "uid").clear()
        driver.find_element(By.NAME, "uid").send_keys(Util.USER_NAME)

        # Enter Valid password
        driver.find_element(By.NAME, "password").clear()
        driver.find_element(By.NAME, "password").send_keys(Util.PASSWORD)

        # Click login button
        driver.find_element(By.NAME, "btnLogin").click()

        # Verify Output
        actual_title = driver.title
        if actual_title == Util.EXPECTED_TITLE:
            print("TEST CASED PASSED")
        else:
            print("TEST CASE FAILED")
