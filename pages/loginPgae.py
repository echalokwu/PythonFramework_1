from selenium.webdriver.common.by import By

from PythonFrameowrk_1.Locators.locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.mobile_link_xpath = Locators.mobile_link_xpath
        self.tv_link_xpath = Locators.tv_link_xpath
        self.sony_add_to_compare_link_xpath = Locators.sony_add_to_compare_link_xpath
        self.iphone_add_to_compare_link_xpath = Locators.iphone_add_to_compare_link_xpath
        self.compare_link_xpath = Locators.compare_link_xpath
        self.close_popUp_windows_link_xpath = Locators.close_popUp_windows_link_xpath


    def click_mobile_menu(self):
        self.driver.find_element(By.XPATH, Locators.mobile_link_xpath).click()

    def add_sony_xperia_to_compare(self):
        self.driver.find_element(By.XPATH, "//li[1]//div[1]//div[3]//ul[1]//li[2]//a[1]").click()

    def add_iphone_to_compare(self):
        self.driver.find_element(By.XPATH, "//li[2]//div[1]//div[3]//ul[1]//li[2]//a[1]").click()

    def click_to_compare_button(self):
        self.driver.find_element(By.XPATH, "//button[@class='button']//span//span[contains(text(),'Compare')]").click()

    def close_popup_window(self):
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Close Window')]").click()






