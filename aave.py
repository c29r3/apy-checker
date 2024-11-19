from playwright.sync_api import sync_playwright
import time
import logging
from logging_config import setup_logging

setup_logging()

def get_apy_aave():
    with sync_playwright() as p:
        apy_xpath = '//*[@id="__next"]/main/div[2]/div/div[2]/div[1]/div/div[3]/div/div[1]/div[3]/div/p'
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://app.aave.com/reserve-overview/?underlyingAsset=0xdac17f958d2ee523a2206206994597c13d831ec7"
                  "&marketName=proto_mainnet_v3")
        page.wait_for_selector('#__next > main > div.MuiBox-root.css-159pi92 > div > div.MuiBox-root.css-k008qs > '
                               'div.MuiBox-root.css-14g9wgc > div > div:nth-child(3) > div > '
                               'div.MuiBox-root.css-1dtnjt5 > div:nth-child(3) > div > p', timeout=10000)

        usdt_apy = page.query_selector(apy_xpath).inner_text().replace('\n%', '')

        page.goto("https://app.aave.com/reserve-overview/?underlyingAsset=0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48&marketName=proto_mainnet_v3")
        page.wait_for_selector(
            '#__next > main > div.MuiBox-root.css-159pi92 > div > div.MuiBox-root.css-k008qs > '
            'div.MuiBox-root.css-14g9wgc > div > div:nth-child(3) > div > div.MuiBox-root.css-1dtnjt5 > '
            'div:nth-child(3) > div > p', timeout=10000)
        usdc_apy = page.query_selector(apy_xpath).inner_text().replace('\n%', '')

        browser.close()
        logging.info("Data fetched successfully from Aave.")
        # return usdt_apy, usdc_apy
        return {'USDT': float(usdt_apy), 'USDC': float(usdc_apy)}

if __name__ == "__main__":
    usdt_apy, usdc_apy = get_apy_aave()
    print("USDT:", usdt_apy)
    print("USDC:", usdc_apy)
