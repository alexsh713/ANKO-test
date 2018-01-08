from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

target_url = 'https://dev2.revetinc.com/'

def handle_element(driver, attribute, attribute_value, timeout):
    """
        Waiting for element and identify it on the web page.
        :param driver: class
        :param attribute: str
        :param attribute_value: str
        :param timeout: int
        :return: webdriver element for success, None otherwise
        :rtype: webdriver element

    """
    try:
        element = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((attribute, attribute_value)))
        return element
    
    except TimeoutException:
        return None


# initial webdriver
driver = webdriver.Firefox()
# navigate to target url
driver.get(target_url)
# click "Join now"
handle_element(driver, By.XPATH, '//a[@href="/join-now/simple"]', 10).click()
# click "join via your email address"
handle_element(driver, By.XPATH, '//a[@href="/join-now"]', 10).click()
# find first name field and type value in it
handle_element(driver, By.NAME, 'FirstName', 10).send_keys('test')
# find last name field and type value in it
handle_element(driver, By.NAME, 'LastName', 10).send_keys('test')
# find email field and type value in it
handle_element(driver, By.NAME, 'UserName', 10).send_keys('test@test.com')
# find password field and type value in it
handle_element(driver, By.NAME, 'Password', 10).send_keys('Qwerty123$')
# submit the form
handle_element(driver, By.NAME, 'Password', 10).submit()





