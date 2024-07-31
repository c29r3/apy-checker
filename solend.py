import requests
import logging
from logging_config import setup_logging

# Setup logging
setup_logging()

SOLEND_URL = ("https://api.solend.fi/v1/reserves?"
              "scope=solend"  # for all tokens scope=all
              "&deployment=production"
              "&ids=BgxfHJDzm44T7XG68MYKx7YisTjZu73tVovyZSjJMpmw,8K9WC8xoh2rtQNY7iEGXtPvfbDCi563SdWhCAhuMP2xE")

TOKENS = {
    'USDC': 'BgxfHJDzm44T7XG68MYKx7YisTjZu73tVovyZSjJMpmw',
    'USDT': '8K9WC8xoh2rtQNY7iEGXtPvfbDCi563SdWhCAhuMP2xE'
}
TOKENS_BY_VALUE = {v: k for k, v in TOKENS.items()}


def get_supply_apr():
    try:
        response = requests.get(SOLEND_URL)
        response.raise_for_status()
        data = response.json()

        result = {}
        for reserve in data['results']:
            mint_pubkey = reserve['reserve']['address']
            if mint_pubkey in TOKENS_BY_VALUE:
                supply_apr = reserve['rates']['supplyInterest']
                result[TOKENS_BY_VALUE[mint_pubkey]] = float(supply_apr)

        logging.info("Data fetched successfully from Solend API.")
        return result

    except requests.exceptions.RequestException as req_err:
        logging.error(f"Failed to fetch data from Solend API: {req_err}")
        return {}


if __name__ == "__main__":
    data = get_supply_apr()
    for token, apr in data.items():
        print(f'{token}: {apr:.3f}%')
