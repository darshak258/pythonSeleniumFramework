from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    country= (By.XPATH, "//input[@id='country']")


    def getCountryname(self):
        return self.driver.find_element(*ConfirmPage.country)

