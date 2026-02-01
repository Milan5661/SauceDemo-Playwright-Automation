import pytest
from playwright.sync_api import Page, expect


class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = 'https://www.saucedemo.com/'

        self.username_field = page.locator("[data-test='username']")
        self.password_field = page.locator("[data-test='password']")
        self.login_button = page.locator("[data-test='login-button']")



    
    
    # Run the test steps
 
    
    # Assertions

    def load(self):
        self.page.goto(self.url)
    
    def Login(self, username, password):
        self.username_field.fill(username)
        self.password_field.fill(password)
        self.login_button.click()
    
    

