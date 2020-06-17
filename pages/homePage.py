from selenium.webdriver.common.by import By

from PythonFrameowrk_1.Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.tv_link_xpath = Locators.tv_link_xpath
        self.add_product_to_wishList_xpath = Locators.add_product_to_wishList_xpath
        self.share_wishList_xpath = Locators.share_wishList_xpath
        self.share_List_email_id = Locators.share_List_email_id
        self.share_List_message_id = Locators.share_List_message_id
        self.my_wish_link_xpath = Locators.my_wish_link_xpath
        self.email_text_id = Locators.Email_text_id
        self.password_text_id = Locators.Password_text_id
        self.add_to_cart_link_xpath = Locators.add_to_cart_link_xpath

    def click_tv_menu(self):
        self.driver.find_element(By.XPATH, Locators.tv_link_xpath).click()

    def click_to_add_product_WishList(self):
        self.driver.find_element(By.XPATH, Locators.add_product_to_wishList_xpath).click()

    def click_to_share_WishList(self):
        self.driver.find_element(By.XPATH, Locators.share_wishList_xpath).click()

    def enter_WishList_email(self, email):
        self.driver.find_element(By.ID, Locators.share_List_email_id).send_keys(email)

    def enter_WishList_message(self, message):
        self.driver.find_element(By.ID, Locators.share_List_message_id).send_keys(message)

    def click_my_wishList(self):
        self.driver.find_element(By.XPATH, Locators.my_wish_link_xpath).click()

    def click_add_to_cart_link(self):
        self.driver.find_element(By.XPATH, Locators.add_to_cart_link_xpath).click()





