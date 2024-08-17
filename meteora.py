import requests
import logging
from logging_config import setup_logging

# Setup logging
setup_logging()

METEORA_VAULT_URL = ("https://merv2-api.meteora.ag/vault_info")

TOKENS = ["USDC"]


def meteora_vault_apr():
    try:
        response = requests.get(METEORA_VAULT_URL)
        response.raise_for_status()

        if "symbol" not in str(response.text):
            logging.error(f'Failed to fetch data from Meteora API: {response.status_code=}\n'
                          f'{response.text=}')

        data = response.json()
        result = {}
        for reserve in data:
            for token in TOKENS:
                if token == reserve["symbol"]:
                    closest_apy = reserve['closest_apy']
                    result[token] = float(closest_apy)

        logging.info("Data fetched successfully from Meteora API.")
        return result

    except requests.exceptions.RequestException as req_err:
        logging.error(f"Failed to fetch data from Meteora API: {req_err}")
        return {}


if __name__ == "__main__":
    data = meteora_vault_apr()
    for token, apr in data.items():
        print(f'{token}: {apr:.3f}%')
