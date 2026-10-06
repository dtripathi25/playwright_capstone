from playwright.sync_api import Page, expect


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.products_title = page.get_by_text("Products", exact=True)
        self.product_items = page.locator(".inventory_item")

    def is_products_page_displayed(self):
        expect(self.products_title).to_be_visible()
        return True

    def get_product_count(self):
        return self.product_items.count()

    def add_first_product_to_cart(self):
        self.product_items.first.get_by_role(
            "button", name="Add to cart"
        ).click()

    def get_cart_count(self):
        cart_badge = self.page.locator(".shopping_cart_badge")

        if cart_badge.count() == 0:
            return ""

        return cart_badge.inner_text()

    def remove_first_product(self):
        self.product_items.first.get_by_role(
            "button", name="Remove"
        ).click()
        
    def open_first_product(self):
        self.product_items.first.get_by_text(
        "Sauce Labs Backpack", exact=True
        ).click()
        
    def sort_products(self, option):
        self.page.get_by_role(
        "combobox"
        ).select_option(option)
        
    def complete_checkout(self):
        self.page.locator(".shopping_cart_link").click()
        self.page.get_by_role("button", name="Checkout").click()

        self.page.get_by_label("First Name").fill("Devesh")
        self.page.get_by_label("Last Name").fill("Tripathi")
        self.page.get_by_label("Zip/Postal Code").fill("07960")

        self.page.get_by_role("button", name="Continue").click()
        self.page.get_by_role("button", name="Finish").click()
            
            