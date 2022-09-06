from selenium.webdriver.common.by import By

from pageObjects.RegisterPage import RegisterPage


class RegisterPage:

    def __init__(self, driver):
        self.driver = driver

    gender = (By.ID, "gender")
    firstName = (By.ID, "FirstName")
    lastName = (By.ID, "LastName")
    dateOfBirth = (By.NAME, "DateOfBirthDay")
    email = (By.ID, "Email")
    companyName = (By.ID, "Company")
    newsletter = (By.ID, "Newsletter")
    password = (By.ID, "Password")
    confirmPassword = (By.ID, "ConfirmPassword")
    registerButton = (By.ID, "register-button")

    successMessage = (By.CLASS_NAME, "result")


    def getGender(self):
        return self.driver.find_element(*RegisterPage.gender)

    def getFirstName(self):
        return self.driver.find_element(*RegisterPage.firstName)

    def getLastName(self):
        return self.driver.find_element(*RegisterPage.lastName)

    def getDateOfBirth(self):
        return self.driver.find_element(*RegisterPage.dateOfBirth)

    def getEmail(self):
        return self.driver.find_element(*RegisterPage.email)

    def getCompanyName(self):
        return self.driver.find_element(*RegisterPage.companyName)

    def getNewsletterCheckBox(self):
        return self.driver.find_element(*RegisterPage.newsletter)

    def getPassword(self):
        return self.driver.find_element(*RegisterPage.password)

    def getConfirmPassword(self):
        return self.driver.find_element(*RegisterPage.confirmPassword)

    def clickOnRegister(self):
        return self.driver.find_element(*RegisterPage.registerButton)

    def getSuccessMessage(self):
        return self.driver.find_element(*RegisterPage.successMessage)




