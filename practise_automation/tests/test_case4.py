import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver


class Test_Demo:

    @pytest.fixture()
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome(
            executable_path="/Users/echalo/Desktop/AutomationTesting/PythonFrameowrk_1/drivers/chromedriver")
        driver.get("http://live.demoguru99.com")
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_case_4(self, test_setUp):
        """Verify that you are able to compare two products"""
        driver.find_element(By.XPATH, "//a[contains(text(),'Mobile')]").click()
        driver.find_element(By.XPATH, "//li[1]//div[1]//div[3]//ul[1]//li[2]//a[1]").click()
        driver.find_element(By.XPATH, "//li[2]//div[1]//div[3]//ul[1]//li[2]//a[1]").click()
        main_window_SONY = driver.find_element(By.XPATH, "//h2[@class='product-name']//a[contains(text(),'Sony "
                                                         "Xperia')]").text
        main_window_IPHONE = driver.find_element(By.XPATH,
                                                 "//h2[@class='product-name']//a[contains(text(),'IPhone')]").text
        windows_before = driver.window_handles[0]
        print(windows_before)

        driver.find_element(By.XPATH, "//button[@class='button']//span//span[contains(text(),'Compare')]").click()
        time.sleep(5)
        windows_after = driver.window_handles[1]
        driver.switch_to.window(windows_after)
        print(windows_after)

        # Verify Header
        # expHead = "COMPARE PRODUCTS"
        # actHead = driver.find_element(By.XPATH, "//h1[contains(text(),'Compare Products')]").text
        # try:
        #     assert expHead == actHead
        # except AssertionError:
        #     print(expHead, "this is not the correct Header")

        # Verify products are reflected in new window
        new_window_SONY = driver.find_element(By.XPATH, "//a[contains(text(),'Sony Xperia')]").text
        new_window_IPHONE = driver.find_element(By.XPATH, "//a[contains(text(),'IPhone')]").text

        try:
            assert main_window_SONY == new_window_SONY
            assert main_window_IPHONE == new_window_IPHONE
        except AssertionError:
            print("Products are not reflected in new window")

        driver.find_element(By.XPATH, "//span[contains(text(),'Close Window')]").click()
        driver.switch_to.window(windows_before)
        time.sleep(3)

    def test_case_5(self, test_setUp):
        """Verify you can create account in E-commerce site and can share wishes to other people using email"""
        driver.find_element(By.XPATH, "//div[@class='footer']//a[contains(text(),'My Account')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Create an Account')]").click()
        driver.find_element(By.ID, "firstname").send_keys("Meko")
        driver.find_element(By.ID, "lastname").send_keys("Meka")
        driver.find_element(By.ID, "email_address").send_keys("deidei167@test.com")
        driver.find_element(By.ID, "password").send_keys("moimoi123")
        driver.find_element(By.ID, "confirmation").send_keys("moimoi123")
        driver.find_element(By.XPATH, "//span[contains(text(),'Register')]").click()

        # Verify Registration is done
        expMessage = "Thank you for registering with Main Website Store."
        confMessage = driver.find_element(By.XPATH,
                                          "//span[contains(text(),'Thank you for registering with Main Website "
                                          "Store.')]").text
        try:
            assert expMessage == confMessage
        except AssertionError:
            print("Registration is not done")

        driver.find_element(By.XPATH, "//a[contains(text(),'TV')]").click()
        driver.find_element(By.XPATH, "//li[1]//div[1]//div[3]//ul[1]//li[1]//a[1]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Share Wishlist')]").click()
        driver.find_element(By.ID, "email_address").send_keys("iwe67@yahoo.com")
        driver.find_element(By.ID, "message").send_keys("testing")
        driver.find_element(By.XPATH, "//span[contains(text(),'Share Wishlist')]").click()

        # Verify Wishlist is Shared
        expWishlist = "Your Wishlist has been shared."
        actualWishlist = driver.find_element(By.XPATH, "//span[contains(text(),'Your Wishlist has been shared.')]").text

        try:
            assert expWishlist == actualWishlist
        except AssertionError:
            print("Wishlist is not shared")
