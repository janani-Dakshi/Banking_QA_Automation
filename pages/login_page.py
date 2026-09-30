
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver=driver
        self.username= (By.NAME, "username")
        self.password=(By.NAME,"password")
        self.login_button=(By.CSS_SELECTOR,'[value="Log In"]')

    def enter_username(self,username):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.username)).send_keys(username)

    def enter_password(self,password):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.password)).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

