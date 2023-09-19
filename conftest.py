import pytest
from selenium import webdriver
from configurations.get_config import get_data
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")
    parser.addoption("--env_name", action='store', default="staging")
    parser.addoption("--product_name", action='store', default="quartz")


@pytest.fixture(scope='class')
def setup_one(request):
    browser = request.config.getoption("browser_name")
    env = request.config.getoption("env_name")
    product = request.config.getoption("product_name")

    test_data = get_data(product)

    if browser == "chrome" and env == "staging":
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(test_data['stage_url'])
        driver.maximize_window()
        request.cls.product = product
        request.cls.driver = driver
        yield
        driver.close()

    elif browser == "mobile_chrome" and env == "staging":
        chrome_options = webdriver.ChromeOptions()
        mobile_emulation = {"deviceName": "Nokia N9"}
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
        service = Service(executable_path=r'C:\Users\harshalashok_warkar\study_codes\bdd_demo\drivers\chromedriver.exe')
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get(test_data['prod_url'])
        request.cls.product = product
        request.cls.driver = driver
        yield
        driver.close()

    elif browser == "firefox" and env == "staging":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.set_preference("dom.webnotifications.enabled", False)
        # firefox_options.headless = True
        driver = webdriver.Firefox(options=firefox_options)
        driver.get(test_data['prod_url'])
        request.cls.product = product
        request.cls.driver = driver
        yield
        driver.close()
