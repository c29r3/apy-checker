from playwright.sync_api import sync_playwright
import time
import logging
from logging_config import setup_logging

# Setup logging
setup_logging()

def get_apy():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://app.kamino.finance/?filter=main&sort%5B0%5D%5Bid%5D=Supply%20APY&sort%5B0%5D%5Bdesc%5D=true")

        # Increase wait time for page load and data
        page.wait_for_selector('table', timeout=60000)

        # Additional delay for assurance
        time.sleep(5)

        # Scroll down the page to make element visible
        page.evaluate("window.scrollBy(0, window.innerHeight)")
        time.sleep(2)  # Wait for the page to scroll

        # Ensure we are in the Main Market section and click it
        page.click("text=Main Market")

        # Refresh rows after navigating to the desired section
        tables = page.query_selector_all('._tableWrapper_1a0p6_31')

        # Ensure we selected the Main Market table
        main_market_table = tables[1]  # Index 1 for the second table

        rows = main_market_table.query_selector_all('tbody tr')

        usdt_apy = None
        usdc_apy = None

        for row in rows:
            cells = row.query_selector_all('td')
            asset_name = cells[0].inner_text()  # Asset name in the first column

            # Extract APY values for USDT and USDC
            if asset_name == "USDT":
                usdt_apy = cells[4].inner_text()  # Assuming APY in the fifth column
            elif asset_name == "USDC":
                usdc_apy = cells[4].inner_text()

        browser.close()
        logging.info("Data fetched successfully from Kamino Finance.")
        return usdt_apy, usdc_apy


if __name__ == "__main__":
    usdt_apy, usdc_apy = get_apy()
    print("USDT Supply APY:", usdt_apy)
    print("USDC Supply APY:", usdc_apy)
