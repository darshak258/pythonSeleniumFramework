from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "(//div[@class='card h-100'])")
    cardFooter = (By.CSS_SELECTOR, ".card-footer button")
    addCart = (By.XPATH, "(//button[contains(text(),'Add')])[4]")
    checkOut=(By.XPATH, "//a[@class='nav-link btn btn-primary']")
    finalcheckOut= (By.XPATH, "//button[normalize-space()='Checkout']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def addinginCart(self):
        return self.driver.find_element(*CheckOutPage.addCart)

    def checkOutButton(self):
        return self.driver.find_element(*CheckOutPage.checkOut)

    def finalCheckOutButton(self):
        return self.driver.find_element(*CheckOutPage.finalcheckOut)