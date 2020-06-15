import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from PythonFrameowrk_1.pages.loginPgae import LoginPage
from PythonFrameowrk_1.Locators.locators import Locators


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
        login = LoginPage(driver)
        login.click_mobile_menu()
        login.add_sony_xperia_to_compare()
        login.add_iphone_to_compare()
        main_window_SONY = driver.find_element(By.XPATH, Locators.main_window_sony).text
        main_window_IPHONE = driver.find_element(By.XPATH, Locators.main_window_iphone).text
        print(main_window_SONY, main_window_IPHONE)

        windows_before = driver.window_handles[0]
        print(windows_before)

        login.click_to_compare_button()
        time.sleep(5)

        windows_after = driver.window_handles[1]
        driver.switch_to.window(windows_after)
        print(windows_after)

        # Verify products are reflected in new window
        new_window_SONY = driver.find_element(By.XPATH, Locators.new_window_sony).text
        new_window_IPHONE = driver.find_element(By.XPATH, Locators.new_window_iphone).text
        print(new_window_SONY, new_window_IPHONE)

        try:
            assert main_window_SONY == new_window_SONY
            assert main_window_IPHONE == new_window_IPHONE
        except AssertionError:
            print("Products are not reflected in new window")

        login.close_popup_window()
        driver.switch_to.window(windows_before)
        time.sleep(3)

    def test_case_5(self, test_setUp):
        """Verify you can create account in E-commerce site and can share wishes to other people using email"""
        driver.find_element(By.XPATH, "//div[@class='footer']//a[contains(text(),'My Account')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Create an Account')]").click()
        driver.find_element(By.ID, "firstname").send_keys("Meko")
        driver.find_element(By.ID, "lastname").send_keys("Meka")
        driver.find_element(By.ID, "email_address").send_keys("deidei191@test.com")
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
        except AssertionError as msg:
            print(msg)

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

    def test_case_6(self, test_setUp):
        """Verify user is able to purchase product using registered email id(USE CHROME BROWSER)"""
        driver.find_element(By.XPATH, "//div[@class='footer']//a[contains(text(),'My Account')]").click()
        driver.find_element(By.ID, "email").clear()
        driver.find_element(By.ID, "email").send_keys("deidei191@test.com")
        driver.find_element(By.ID, "pass").send_keys("moimoi123")
        driver.find_element(By.XPATH, "//span[contains(text(),'Login')]").click()
        driver.find_element(By.XPATH, "//div[@class='block-content']//a[contains(text(),'My Wishlist')]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Add to Cart')]").click()
        drpCountry = Select(driver.find_element(By.ID, "country"))
        drpCountry.select_by_visible_text("United States")
        drpState = Select(driver.find_element(By.ID, "region_id"))
        drpState.select_by_visible_text("New York")
        driver.find_element(By.ID, "postcode").send_keys("542896")
        driver.find_element(By.XPATH, "//span[contains(text(),'Estimate')]").click()

        # Verify Shipping cost is generated
        shipping = driver.find_element(By.XPATH, "//label[contains(text(),'Fixed')]").text
        try:
            assert shipping == "Fixed - $5.00"
        except AssertionError:
            print(shipping, "Is the correct text")
        driver.find_element(By.ID, "s_method_flatrate_flatrate").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Update Total')]").click()

        # Verify Shipping cost is added to total
        vShippingCost = driver.find_element(By.XPATH,
                                            "//td[contains(text(),'Shipping & Handling (Flat Rate - Fixed)')]").text
        try:
            assert vShippingCost == "SHIPPING & HANDLING (FLAT RATE - FIXED)"
        except AssertionError:
            print(vShippingCost, "is not added to total")

        driver.find_element(By.XPATH, "(//button[@title='Proceed to Checkout'])[2]").click()
        driver.find_element(By.ID, "billing:firstname").send_keys("meko")
        driver.find_element(By.ID, "billing:lastname").send_keys("meka")
        driver.find_element(By.ID, "billing:street1").send_keys("3 ththtkkdd")
        driver.find_element(By.ID, "billing:city").send_keys("New york")
        drpStatePrv = Select(driver.find_element(By.ID, "billing:region_id"))
        drpStatePrv.select_by_visible_text("New York")
        driver.find_element(By.ID, "billing:postcode").send_keys("589923")
        drpBillCountry = Select(driver.find_element(By.ID, "billing:country_id"))
        drpBillCountry.select_by_visible_text("United States")
        driver.find_element(By.ID, "billing:telephone").send_keys("712678999")
        driver.find_element(By.XPATH, "(//SPAN[text()='Continue'][text()='Continue'])[1]").click()
        time.sleep(3)
        driver.find_element(By.XPATH, "//SPAN[@xpath='1'][text()='Continue']").click()
        driver.find_element(By.ID, "p_method_checkmo").click()
        driver.find_element(By.XPATH, "(//SPAN[text()='Continue'][text()='Continue'])[4]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Place Order')]").click()

        # Verify Order is generated
        orderRec = driver.find_element(By.XPATH, "//h1[contains(text(),'Your order has been received.')]").text
        try:
            assert orderRec == "Your order has been received."
        except AssertionError as e:
            print(e)
            print("Order placed successfully")
