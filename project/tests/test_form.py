import pytest
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.sidebar_page import SideBarPage



def test_login(page : Page):

    login_page = LoginPage(page)
    inventory=InventoryPage(page)
    cartpage = CartPage(page)
    checkoutpage= CheckoutPage(page)
    sidebarpage=SideBarPage(page)
    


    login_page.load()
   
    empty_scenarios = [
        ("", "", "Epic sadface: Username is required"),
        ("", "secret_sauce", "Epic sadface: Username is required"),
        ("standard_user", "", "Epic sadface: Password is required")
    ]

    for user, pwd, error in empty_scenarios:
        login_page.Login(user, pwd)
       
        error_msg = page.locator("[data-test='error']")
        expect(error_msg).to_contain_text(error)
        
        page.reload()
    
    
    login_page.Login("standard_user", "secret_sauce")
    expect(inventory.title_header).to_have_text("Products")
    inventory.add_backpack_to_cart()
    expect(inventory.count_items).to_have_text("1")
    inventory.count_items.click()
    expect(page).to_have_url("https://www.saucedemo.com/cart.html")
    expect(cartpage.inventory_item).to_have_text("Sauce Labs Backpack")
    cartpage.proceed_to_checkout()
    expect(page).to_have_url("https://www.saucedemo.com/checkout-step-one.html")
    checkoutpage.enter_details("john","cena", "12345")
    checkoutpage.finish_checkout()
    sidebarpage.reset()
    



    





    
    
   


