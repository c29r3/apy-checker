# fluid.py

import logging
from logging_config import setup_logging
from playwright.sync_api import sync_playwright

setup_logging()

def get_fluid_supply_apr():
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto('https://fluid.instadapp.io/lending/1', timeout=60000)
            page.wait_for_load_state('networkidle')

            # Getting Net APR for USDC
            usdc_apr_element = page.query_selector(
                'xpath=//*[@id="__nuxt"]/div/div[3]/div[1]/section/div/div[1]/div/div[4]/div[3]/div')
            usdc_apr_text = usdc_apr_element.inner_text() if usdc_apr_element else None

            # Getting Net APR for USDT
            usdt_apr_element = page.query_selector(
                'xpath=//*[@id="__nuxt"]/div/div[3]/div[1]/section/div/div[3]/div/div[4]/div[3]/div')
            usdt_apr_text = usdt_apr_element.inner_text() if usdt_apr_element else None

            browser.close()

            result = {}
            if usdt_apr_text:
                usdt_apr = float(usdt_apr_text.replace('%', '').strip())
                result['USDT'] = usdt_apr
            else:
                result['USDT'] = 0.0

            if usdc_apr_text:
                usdc_apr = float(usdc_apr_text.replace('%', '').strip())
                result['USDC'] = usdc_apr
            else:
                result['USDC'] = 0.0

            logging.info("Data fetched successfully from Fluid.")
            return result

    except Exception as e:
        logging.error(f"Failed to fetch data from Fluid: get_fluid_supply_apr: {e}")
        return {}


if __name__ == "__main__":
    data = get_fluid_supply_apr()
    for token, apr in data.items():
        print(f'{token}: {apr:.3f}%')
