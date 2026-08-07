from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    username_id = "login-email"
    password_id = "login-password"
    login_button_id = "login-button"

    def __init__(self, driver):
        self.driver = driver


    def username(self):
        wait = WebDriverWait(self.driver, 10)
