from playwright.sync_api import expect,Page

class CartPage():
    def __init__(self, page:Page):
        self.page = page
        self.cart_url = "https://www.saucedemo.com/cart.html"
        self.inventory_item = page.locator("[data-test='inventory-item-name']")
        self.checkout_button = page.locator("[data-test='checkout']")
    
    def load(self):
        self.page.goto(self.cart_url)
    
    def proceed_to_checkout(self):
        self.checkout_button.click()

