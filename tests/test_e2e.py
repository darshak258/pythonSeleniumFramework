import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.ConfirmPage import ConfirmPage
from utilities.BaseClass import BaseClass


from selenium.webdriver.support import expected_conditions as EC

from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass





class TestOne(BaseClass):

    def test_e2e(self):
        #log=self.getLogger()
        homePage= HomePage(self.driver)
        checkOutPage=homePage.shopItems()
        #log.info("getting all items")


        cards = checkOutPage.getCardTitles()
        i =-1
        for card in cards:
            i = i+1
            cardText = card.text
            #log.info(cardText)
            if cardText == "Blackberry":
                checkOutPage.cardFooter()[i].click()
        time.sleep(4)
        checkOutPage.addinginCart().click()
        checkOutPage.checkOutButton().click()
        checkOutPage.finalCheckOutButton().click()
        confirmPage = ConfirmPage(self.driver)
        #log.info("entering country name india")
        confirmPage.getCountryname().send_keys("ind")
        time.sleep(6)
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        textMatch = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        #log.info("text receive from the application")
        assert("Success! Thank you!" in textMatch)







