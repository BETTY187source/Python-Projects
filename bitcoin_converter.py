"""
This program calculates the cost of a specified number of Bitcoins in a given currency.

It accepts two command-line arguments:
1. The number of Bitcoins (a decimal number).
2. The desired currency (GBP, USD, or EUR).

The program performs the following steps:
- Validates the input to ensure the number of Bitcoins is a valid number
  and the currency is one of the supported options.
- Fetches the current Bitcoin prices from the CoinDesk API.
- Calculates the cost in the specified currency.
- Displays the result formatted with four decimal places and ',' as a thousands separator.

If there are any errors, such as invalid input or issues with the API, 
the program exits with an appropriate error message.
"""

import sys
import requests

def validate_input():
    """Validate command-line arguments for Bitcoin quantity and desired currency."""
    if len(sys.argv) != 3:
        sys.exit("Usage: python bitcoin_converter.py <quantity_of_bitcoins> <target_currency>")

    try:
        bitcoin_quantity = float(sys.argv[1])  # Validate the first argument as a float
    except ValueError:
        sys.exit("Error: The first argument must be a valid number representing the number of Bitcoins.")

    target_currency = sys.argv[2].upper()  # Ensure currency is uppercase
    supported_currencies = ["GBP", "USD", "EUR"]

    if target_currency not in supported_currencies:
        sys.exit(f"Error: Unsupported currency. Available options are {', '.join(supported_currencies)}.")

    return bitcoin_quantity, target_currency

def get_bitcoin_exchange_rates():
    """Retrieve the latest Bitcoin exchange rates from CoinDesk API."""
    api_url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Handle HTTP errors
        exchange_data = response.json()
        return {
            "GBP": exchange_data["bpi"]["GBP"]["rate_float"],
            "USD": exchange_data["bpi"]["USD"]["rate_float"],
            "EUR": exchange_data["bpi"]["EUR"]["rate_float"]
        }
    except requests.RequestException as error:
        sys.exit(f"Error: Unable to retrieve Bitcoin prices. {error}")

def calculate_bitcoin_cost():
    """Main function to compute and display the cost of Bitcoins in the specified currency."""
    bitcoin_quantity, target_currency = validate_input()
    exchange_rates = get_bitcoin_exchange_rates()

    if target_currency not in exchange_rates:
        sys.exit(f"Error: Currency '{target_currency}' not available in the API response.")

    # Compute the cost in the target currency
    total_cost = bitcoin_quantity * exchange_rates[target_currency]
    # Display the result formatted with 4 decimal places and ',' as a thousands separator
    print(f"The cost of {bitcoin_quantity} Bitcoin(s) in {target_currency} is: {total_cost:,.4f} {target_currency}")

if __name__ == "__main__":
    calculate_bitcoin_cost()
