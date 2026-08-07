from selenium.webdriver.support.wait import WebDriverWait


class home_page:

    main_login_button_xpath = "//div[@class='nav-user-section']"
    def __init__(self,driver):
        self.driver = driver

    def login(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located((By.XPATH, self.main_login_button_xpath))).click()