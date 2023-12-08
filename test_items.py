from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_is_visible(browser): 
    browser.get(link)
    button = browser.find_elements(By.CSS_SELECTOR, "button[class~='btn-add-to-basket']")
    browser.implicitly_wait(5)
    assert button, "Button not found"
