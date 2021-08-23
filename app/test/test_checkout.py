from app.pages.checkout import Checkout


class Testcheckout(Checkout):
    def test_checkout(self):
        headless_status = super().read_config("browser_config", "headless_status")
        driver = super().spawn_driver(headless_status)

        site_url = super().read_config("platform", "site")
        driver.get(site_url)

        # Clear site cookies
        super().clear_cookies(driver)

        # search product
        super().search_product(driver)
        # click item from search result
        super().click_product(driver)
        # Add to cart
        super().add_to_cart(driver)

        driver.quit()
