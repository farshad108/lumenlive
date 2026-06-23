import requests

COINGECKO_URL = "https://api.coingecko.com/api/v3/simple/price"

def get_crypto_price(coin_id: str = "bitcoin", currency: str = "usd") -> float | None:
    """
    Fetches the live price of a cryptocurrency from CoinGecko.
    Example coin_id: bitcoin, ethereum, tether
    """
    params = {
        "ids": coin_id,
        "vs_currencies": currency
    }
    try:
        response = requests.get(COINGECKO_URL, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data[coin_id][currency]
    except Exception as e:
        print(f"Error fetching price: {e}")
        return None