from playwright.sync_api import Page

class SideBarPage:
    def __init__(self ,page:Page):
        self.page=page
        self.menu_bar=page.locator("#react-burger-menu-btn")
        self.logout_button=page.locator("[data-test='logout-sidebar-link']")
        self.reset_link=page.locator("[data-test='reset-sidebar-link']")
    
    def logout(self):
        self.menu_bar.click()
        self.logout_button.click()
    
    def reset(self):
        self.menu_bar.click()
        self.reset_link.click()