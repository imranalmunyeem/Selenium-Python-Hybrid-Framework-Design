from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.ID, "Email")
    password = (By.ID, "Password")
    loginButton = (By.XPATH, "/html/body/div[6]/div[3]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button")


    def getEmail(self):
        return self.driver.find_element(*LoginPage.email)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def clickOnlogin(self):
        return self.driver.find_element(*LoginPage.loginButton)



