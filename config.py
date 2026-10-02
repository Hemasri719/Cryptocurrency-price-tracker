import os
#from dotenv import load_dotenv

#load_dotenv()


# Cryptocurrency settings

TOP_COINS = 10
TOP_GAINERS = 3
TOP_LOSERS = 3

PRICE_THRESHOLD = 100


# Selenium settings

PAGE_LOAD_TIMEOUT = 60
TABLE_WAIT_TIMEOUT = 30

HEADLESS_MODE = False

COINMARKETCAP_URL = "https://coinmarketcap.com/"


# API configuration

CMC_API_KEY = os.getenv("CMC_API_KEY")