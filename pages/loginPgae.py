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
        self.myAccount_link_xpath = Locators.myAccount_link_xpath
        self.createAccount_link_xpath = Locators.createAccount_link_xpath
        self.FirstName_text_id = Locators.FirstName_text_id
        self.LastName_text_id = Locators.LastName_text_id
        self.Email_text_id = Locators.Email_text_id
        self.Password_text_id = Locators.Password_text_id
        self.PasswordConf_text_id = Locators.PasswordConf_text_id
        self.Register_button_xpath = Locators.Register_button_xpath
        self.login_button_xpath = Locators.login_button_xpath
        self.textRegistered_email_id = Locators.textRegistered_email_id
        self.textRegistered_password_id = Locators.textRegistered_password_id

    def click_mobile_menu(self):
        self.driver.find_element(By.XPATH, Locators.mobile_link_xpath).click()

    def click_tv_menu(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(),'TV')]").click()

    def add_sony_xperia_to_compare(self):
        self.driver.find_element(By.XPATH, Locators.sony_add_to_compare_link_xpath).click()

    def add_iphone_to_compare(self):
        self.driver.find_element(By.XPATH, Locators.iphone_add_to_compare_link_xpath).click()

    def click_to_compare_button(self):
        self.driver.find_element(By.XPATH, Locators.compare_link_xpath).click()

    def close_popup_window(self):
        self.driver.find_element(By.XPATH, Locators.close_popUp_windows_link_xpath).click()

    def click_myAccount_Link(self):
        self.driver.find_element(By.XPATH, Locators.myAccount_link_xpath).click()

    def click_create_account_Link(self):
        self.driver.find_element(By.XPATH, Locators.createAccount_link_xpath).click()

    def enterFirstName(self, firstName):
        self.driver.find_element(By.ID, Locators.FirstName_text_id).clear()
        self.driver.find_element(By.ID, Locators.FirstName_text_id).send_keys(firstName)

    def enterLastName(self, lastName):
        self.driver.find_element(By.ID, Locators.LastName_text_id).clear()
        self.driver.find_element(By.ID, Locators.LastName_text_id).send_keys(lastName)

    def enterEmailAddress(self, email):
        self.driver.find_element(By.ID, Locators.Email_text_id).clear()
        self.driver.find_element(By.ID, Locators.Email_text_id).send_keys(email)

    def enterPassword(self, password):
        self.driver.find_element(By.ID, Locators.Password_text_id).clear()
        self.driver.find_element(By.ID, Locators.Password_text_id).send_keys(password)

    def confPassword(self, password):
        self.driver.find_element(By.ID, Locators.PasswordConf_text_id).clear()
        self.driver.find_element(By.ID, Locators.PasswordConf_text_id).send_keys(password)

    def click_register(self):
        self.driver.find_element(By.XPATH, Locators.Register_button_xpath).click()

    def click_login_button(self):
        self.driver.find_element(By.XPATH, Locators.login_button_xpath).click()

    def enter_registered_email(self, email):
        self.driver.find_element(By.ID, Locators.textRegistered_email_id).send_keys(email)

    def enter_registered_password(self, password):
        self.driver.find_element(By.ID, Locators.textRegistered_password_id).send_keys(password)











