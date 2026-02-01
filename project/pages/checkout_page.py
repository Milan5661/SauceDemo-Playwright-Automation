from playwright.sync_api import Page,expect

class CheckoutPage:
    def __init__(self, page:Page):
        self.page=page
        self.first_name=page.locator("[data-test='firstName']")
        self.last_name=page.locator("[data-test='lastName']")
        self.zip_code=page.locator("[data-test='postalCode']")
        self.continue_button=page.locator("[data-test='continue']")
        self.finish_button=page.locator("[data-test='finish']")
        self.back_home_button=page.locator("[data-test='back-to-products']")
    
    def enter_details(self,first ,last ,zip):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.zip_code.fill(zip)
    
    def finish_checkout(self):
        self.continue_button.click()
        self.finish_button.click()
        self.back_home_button.click()