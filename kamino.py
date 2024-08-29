from playwright.sync_api import sync_playwright
import time
import logging
from logging_config import setup_logging

setup_logging()

def get_apy():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://app.kamino.finance/?filter=main&sort%5B0%5D%5Bid%5D=Supply%20APY&sort%5B0%5D%5Bdesc%5D=true")

        page.wait_for_selector('table', timeout=60000)
        time.sleep(5)

        page.click('//*[@id="BACKGROUND_OVERRIDE"]/div/div[3]/div/div[1]/button[2]')
        time.sleep(2)

        table_xpath = '//*[@id="BACKGROUND_OVERRIDE"]/div/div[4]/div[1]/div[2]'
        table = page.query_selector(table_xpath)
        rows = table.query_selector_all('tbody tr')

        usdt_apy = None
        usdc_apy = None

        for row in rows:
            cells = row.query_selector_all('td')
            asset_name = cells[0].inner_text()


            if asset_name == "USDT":
                usdt_apy = cells[4].inner_text()
            elif asset_name == "USDC":
                usdc_apy = cells[4].inner_text()

        browser.close()
        logging.info("Data fetched successfully from Kamino Finance.")
        return usdt_apy, usdc_apy

if __name__ == "__main__":
    usdt_apy, usdc_apy = get_apy()
    print("USDT Supply APY:", usdt_apy)
    print("USDC Supply APY:", usdc_apy)
