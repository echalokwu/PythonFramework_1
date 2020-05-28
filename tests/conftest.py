import pytest
from selenium import webdriver


@pytest.fixture()
def test_setUp(request):
    driver = webdriver.Chrome(executable_path="/Users/echalo/Desktop/Automation Testing/PythonFrameowrk_1/drivers/chromedriver")
    driver.get("http://www.demo.guru99.com/V4/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")


    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("--headless")
    # driver = webdriver.Chrome(chrome_options=chrome_options, executable_path="../drivers/chromedriver")
