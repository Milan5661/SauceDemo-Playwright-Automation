from playwright.sync_api import Page

class InventoryPage():
    def __init__(self, page: Page):
        self.page = page
        self.title_header = page.locator("[data-test='title']")
        self.add_to_cart = page.locator("[data-test='add-to-cart-sauce-labs-backpack']")
        self.count_items = page.locator("[data-test='shopping-cart-badge']")
 

    def add_backpack_to_cart(self):
        self.add_to_cart.click()
    
    def get_count(self):
        return self.count_items.inner_text()
    
    