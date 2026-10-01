from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Chrome options
options = Options()
options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")

# Start Chrome
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

try:
    print("Opening CoinMarketCap...")

    # Open CoinMarketCap
    driver.get("https://coinmarketcap.com/")

    # Wait for cryptocurrency table
    wait = WebDriverWait(driver, 20)

    rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "table tbody tr")
        )
    )

    print("\nCoinMarketCap opened successfully!")

    crypto_count = 0

    print("\n" + "=" * 80)
    print("TOP 10 CRYPTOCURRENCIES")
    print("=" * 80)

    for row in rows:

        cells = row.find_elements(By.TAG_NAME, "td")

        # Skip rows that do not contain enough data
        if len(cells) < 8:
            continue

        # Get coin name and symbol
        coin_text = cells[2].text.strip()

        # Skip CMC20 Index and non-crypto rows
        if "\n" not in coin_text or "CMC20" in coin_text:
            continue

        name_symbol = coin_text.split("\n")

        if len(name_symbol) < 2:
            continue

        name = name_symbol[0]
        symbol = name_symbol[1]

        # Get required data
        price = cells[3].text.strip()
        change_24h = cells[4].text.strip()
        market_cap = cells[7].text.strip()

        crypto_count += 1

        print(f"\nRank       : {crypto_count}")
        print(f"Name       : {name}")
        print(f"Symbol     : {symbol}")
        print(f"Price      : {price}")
        print(f"24h Change : {change_24h}")
        print(f"Market Cap : {market_cap}")

        # Stop after 10 real cryptocurrencies
        if crypto_count == 10:
            break

    print("\n" + "=" * 80)
    print(f"Total cryptocurrencies collected: {crypto_count}")
    print("=" * 80)

except Exception as e:
    print("\nError:")
    print(e)

finally:
    time.sleep(3)
    driver.quit()