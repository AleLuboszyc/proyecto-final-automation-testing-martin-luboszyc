from selenium.webdriver.common.by import By

class LoginPage:
    
    URL = "https://www.saucedemo.com/" 
    
    USERNAME_FIELD = (By.ID, "user-name") 
    
    PASSWORD_FIELD = (By.ID, "password")
    
    LOGIN_BUTTON = (By.ID, "login-button")
    
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']") 
    
    PRODUCTS_HEADER = (By.XPATH, "//span[@class='title' and text()='Products']")


    def __init__(self, driver):
        self.driver = driver

    def go_to_login_page(self):
        self.driver.get(self.URL)
        return self 

    def enter_credentials(self, username, password): 
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        return self

    def click_sign_in(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def get_error_message(self):
        return self.driver.find_element(*self.ERROR_MESSAGE).text
    
    def is_login_successful(self):
        return self.driver.find_element(*self.PRODUCTS_HEADER).is_displayed()