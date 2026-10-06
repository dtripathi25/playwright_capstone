import json
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from utils.logger import logger

@pytest.mark.smoke
def test_valid_login(browser_page):
    browser_page.goto("https://www.saucedemo.com/")
    logger.info("Opening SauceDemo login page")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")
    logger.info("Login completed successfully")

    expect(browser_page).to_have_url(
        "https://www.saucedemo.com/inventory.html"
    )
    
@pytest.mark.regression
def test_invalid_login(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("invalid_user", "wrong_password")
    logger.warning("Invalid login credentials were rejected as expected")

    error_message = browser_page.locator("[data-test='error']")
    expect(error_message).to_be_visible()
    
    
    
@pytest.mark.readonly
def test_products_are_displayed(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser_page)

    assert products_page.is_products_page_displayed()
    assert products_page.get_product_count() > 0
    
@pytest.mark.regression
def test_add_product_to_cart(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser_page)
    products_page.add_first_product_to_cart()

    assert products_page.get_cart_count() == "1"
    
    
@pytest.mark.regression
def test_remove_product_from_cart(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser_page)
    products_page.add_first_product_to_cart()
    products_page.remove_first_product()

    assert products_page.get_cart_count() == ""    
    
@pytest.mark.readonly
def test_product_details(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser_page)
    products_page.open_first_product()

    expect(browser_page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()
    
    
@pytest.mark.readonly
def test_sort_products(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser_page)
    products_page.sort_products("za")

    expect(
        browser_page.get_by_text("Sauce Labs Fleece Jacket", exact=True)
    ).to_be_visible()
    
    
@pytest.mark.regression
def test_checkout_order(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(browser_page)
    products_page.add_first_product_to_cart()
    products_page.complete_checkout()

    expect(
        browser_page.get_by_text(
            "Thank you for your order!",
            exact=True
        )
    ).to_be_visible()
    
    
# Data-driven login test
with open("testdata/login_data.json") as file:
    login_data = json.load(file)


@pytest.mark.regression
@pytest.mark.parametrize("data", login_data)
def test_login_data_driven(browser_page, data):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login(data["username"], data["password"])

    if data["expected"] == "success":
        expect(browser_page).to_have_url(
            "https://www.saucedemo.com/inventory.html"
        )
    else:
        error_message = browser_page.locator("[data-test='error']")
        expect(error_message).to_be_visible()
        
        
def test_wait_handling(browser_page):
    browser_page.goto("https://www.saucedemo.com/")

    login_page = LoginPage(browser_page)
    login_page.login("standard_user", "secret_sauce")

    browser_page.wait_for_url("**/inventory.html")
    browser_page.wait_for_load_state("domcontentloaded")

    products_page = ProductsPage(browser_page)
    products_page.products_title.wait_for(state="visible")

    assert products_page.is_products_page_displayed()
    
    