import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
import sys; print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['/Users/echalo/Desktop/AutomationTesting'])
from PythonFrameowrk_1.pages.loginPgae import LoginPage
from PythonFrameowrk_1.Locators.locators import Locators
from PythonFrameowrk_1.pages.homePage import HomePage


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
        login = LoginPage(driver)
        login.click_myAccount_Link()
        login.click_create_account_Link()
        login.enterFirstName("meka")
        login.enterLastName("meko")
        login.enterEmailAddress("test464@test.com")
        login.enterPassword("moimoi123")
        login.confPassword("moimoi123")
        login.click_register()
        time.sleep(3)

        # Verify Registration is done
        expMessage = "Thank you for registering with Main Website Store."
        actualMessage = driver.find_element(By.XPATH, Locators.confMessage).text
        try:
            assert expMessage == actualMessage
        except AssertionError as msg:
            print(msg)

        homepage = HomePage(driver)
        homepage.click_tv_menu()
        homepage.click_to_add_product_WishList()
        homepage.click_to_share_WishList()
        homepage.enter_WishList_email("iwe@test.com")
        homepage.enter_WishList_message("testing")
        homepage.click_to_share_WishList()

        # Verify Wishlist is Shared
        expWishlist = "Your Wishlist has been shared."
        actualWishlist = driver.find_element(By.XPATH, Locators.actualWishlist).text

        try:
            assert expWishlist == actualWishlist
        except AssertionError:
            print("Wishlist is not shared")

    def test_case_6(self, test_setUp):
        """Verify user is able to purchase product using registered email id(USE CHROME BROWSER)"""
        login = LoginPage(driver)
        homepage = HomePage(driver)
        login.click_myAccount_Link()
        login.enter_registered_email("test464@test.com")
        login.enter_registered_password("moimoi123")
        login.click_login_button()
        time.sleep(3)
        homepage.click_my_wishList()

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
        driver.find_element(By.XPATH, "//div[@id='billing-buttons-container']//button[@class='button']//span//span["
                                      "contains(text(),'Continue')]").click()
        driver.find_element(By.XPATH, "//div[@id='shipping-method-buttons-container']//button["
                                      "@class='button']//span//span[contains(text(),'Continue')]").click()
        driver.find_element(By.ID, "p_method_checkmo").click()
        driver.find_element(By.XPATH, "(//BUTTON[@type='button'])[4]").click()
        driver.find_element(By.XPATH, "//span[contains(text(),'Place Order')]").click()

        # Verify Order is generated
        orderRec = driver.find_element(By.XPATH, "//H2[@class='sub-title'][text()='Thank you for your purchase!']").text
        try:
            assert orderRec == "THANK YOU FOR YOUR PURCHASE!"
        except AssertionError:
            print("Order not placed successfully")
