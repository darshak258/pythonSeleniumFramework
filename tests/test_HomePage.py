import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from TestData.HomePageData import HomePageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, getData):

        homePage=HomePage(self.driver)
        homePage.getName().send_keys(getData["firstname"])
        homePage.getEmail().send_keys(getData["email"])
        homePage.getPassword().send_keys("12345678")
        homePage.getCheckbox().click()
        self.selectOptionByText(homePage.getGender(),getData["gender"])

        homePage.getCheckbox2().click()
        homePage.getSubmission().click()
        alertText=homePage.getSuccess().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_HomePage_data)
    def getData(self, request):
        return request.param







