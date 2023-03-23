from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.XPATH, "//a[@href='/angularpractice/shop']")
    name=(By.XPATH,"//div[@class='form-group']/input[@name='name']")
    email=(By.XPATH, "//div[@class='form-group']/input[@name='email']")
    password=(By.ID, "exampleInputPassword1")
    check1=(By.ID, "exampleCheck1")
    gender=(By.ID,"exampleFormControlSelect1")
    check2=(By.ID, "inlineRadio2")
    submit=(By.XPATH,"//input[@type='submit']")
    success=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")

    def shopItems(self):

        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
    def getName(self):
        return self.driver.find_element(*HomePage.name)
    def getEmail(self):
        return self.driver.find_element(*HomePage.email)
    def getPassword(self):
        return self.driver.find_element(*HomePage.password)
    def getCheckbox(self):
        return self.driver.find_element(*HomePage.check1)
    def getGender(self):
        return self.driver.find_element(*HomePage.gender)
    def getCheckbox2(self):
        return self.driver.find_element(*HomePage.check2)
    def getSubmission(self):
        return self.driver.find_element(*HomePage.submit)
    def getSuccess(self):
        return self.driver.find_element(*HomePage.success)





#