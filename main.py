from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from datetime import datetime
import os
import time


# ============================================================
# CRYPTOCURRENCY PRICE TRACKER
# ============================================================

print("=" * 80)
print("             CRYPTOCURRENCY PRICE TRACKER")
print("=" * 80)


# ============================================================
# 1. CHROME SETUP
# ============================================================

options = Options()

options.add_argument("--start-maximized")
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")

# Let Chrome start displaying the page without waiting
# for every resource to finish loading.
options.page_load_strategy = "eager"


# ============================================================
# 2. START CHROME
# ============================================================

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# IMPORTANT:
# Set timeout BEFORE driver.get()
driver.set_page_load_timeout(60)


try:

    # ========================================================
    # 3. OPEN COINMARKETCAP WITH RETRIES
    # ========================================================

    print("\nOpening CoinMarketCap...")

    website_opened = False

    for attempt in range(1, 4):

        try:

            print(f"Connection attempt {attempt}/3...")

            driver.get("https://coinmarketcap.com/")

            website_opened = True

            print("CoinMarketCap opened successfully!")

            break

        except TimeoutException:

            print(
                f"Attempt {attempt} timed out."
            )

            if attempt < 3:

                print("Retrying...")

                time.sleep(5)

            else:

                raise Exception(
                    "CoinMarketCap could not be opened after 3 attempts."
                )


    # ========================================================
    # 4. WAIT FOR CRYPTOCURRENCY TABLE
    # ========================================================

    print("\nWaiting for cryptocurrency data...")

    wait = WebDriverWait(driver, 30)

    rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "table tbody tr")
        )
    )

    print(
        f"Rows found on CoinMarketCap: {len(rows)}"
    )


    # ========================================================
    # 5. SCRAPE TOP 10 CRYPTOCURRENCIES
    # ========================================================

    crypto_data = []

    crypto_count = 0

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )


    for row in rows:

        cells = row.find_elements(
            By.TAG_NAME,
            "td"
        )

        # Ignore incomplete rows
        if len(cells) < 8:
            continue


        # ----------------------------------------------------
        # Get name and symbol
        # ----------------------------------------------------

        coin_text = cells[2].text.strip()


        # Ignore rows without name + symbol
        if "\n" not in coin_text:
            continue


        # Ignore CoinMarketCap 20 Index
        if "CMC20" in coin_text:
            continue


        name_symbol = coin_text.split("\n")


        if len(name_symbol) < 2:
            continue


        name = name_symbol[0].strip()

        symbol = name_symbol[1].strip()


        # ----------------------------------------------------
        # Get price
        # ----------------------------------------------------

        price = cells[3].text.strip()


        # ----------------------------------------------------
        # Get 24h change
        # ----------------------------------------------------

        change_24h = cells[4].text.strip()


        # ----------------------------------------------------
        # Get market cap
        # ----------------------------------------------------

        market_cap = cells[7].text.strip()


        # ----------------------------------------------------
        # Convert price to numeric value
        # ----------------------------------------------------

        try:

            price_value = float(
                price
                .replace("$", "")
                .replace(",", "")
            )

        except ValueError:

            price_value = 0.0


        # ----------------------------------------------------
        # Convert 24h change to numeric value
        # ----------------------------------------------------

        try:

            change_value = float(
                change_24h
                .replace("%", "")
                .replace(",", "")
            )

        except ValueError:

            change_value = 0.0


        crypto_count += 1


        # ----------------------------------------------------
        # Store record
        # ----------------------------------------------------

        crypto_data.append({

            "timestamp": timestamp,

            "name": name,

            "symbol": symbol,

            "price_usd": price_value,

            "change_24h_pct": change_value,

            "market_cap_usd": market_cap

        })


        # Stop after 10 actual cryptocurrencies
        if crypto_count == 10:
            break


    # ========================================================
    # 6. CHECK SCRAPED DATA
    # ========================================================

    if len(crypto_data) != 10:

        raise Exception(
            f"Expected 10 cryptocurrencies, "
            f"but collected {len(crypto_data)}."
        )


    # ========================================================
    # 7. CREATE DATAFRAME
    # ========================================================

    df = pd.DataFrame(crypto_data)


    # ========================================================
    # 8. DISPLAY TOP 10
    # ========================================================

    print("\n")

    print("=" * 100)

    print("                    TOP 10 CRYPTOCURRENCIES")

    print("=" * 100)


    for index, row in df.iterrows():

        print()

        print(f"Rank       : {index + 1}")

        print(f"Name       : {row['name']}")

        print(f"Symbol     : {row['symbol']}")

        print(
            f"Price      : ${row['price_usd']:,.2f}"
        )

        print(
            f"24h Change : {row['change_24h_pct']:.2f}%"
        )

        print(
            f"Market Cap : {row['market_cap_usd']}"
        )


    print("\n" + "=" * 100)

    print(
        f"Total cryptocurrencies collected: {len(df)}"
    )

    print("=" * 100)


    # ========================================================
    # 9. SAVE TO CSV
    # ========================================================

    csv_file = "crypto_data.csv"

    file_exists = os.path.exists(csv_file)


    df.to_csv(

        csv_file,

        mode="a",

        header=not file_exists,

        index=False

    )


    print(
        f"\nData saved successfully to: {csv_file}"
    )


    # ========================================================
    # 10. TOP 3 GAINERS
    # ========================================================

    print("\n")

    print("=" * 80)

    print("                       TOP 3 GAINERS")

    print("=" * 80)


    top_gainers = (

        df
        .sort_values(
            by="change_24h_pct",
            ascending=False
        )
        .head(3)

    )


    for _, row in top_gainers.iterrows():

        print(
            f"{row['name']} ({row['symbol']}) "
            f"--> {row['change_24h_pct']:.2f}%"
        )


    # ========================================================
    # 11. PRICE THRESHOLD FILTER
    # ========================================================

    print("\n")

    print("=" * 80)

    print("                    COINS ABOVE $100")

    print("=" * 80)


    coins_above_100 = df[
        df["price_usd"] > 100
    ]


    if coins_above_100.empty:

        print(
            "No cryptocurrencies currently above $100."
        )

    else:

        for _, row in coins_above_100.iterrows():

            print(
                f"{row['name']} ({row['symbol']}) "
                f"--> ${row['price_usd']:,.2f}"
            )


    # ========================================================
    # 12. FINAL PROJECT STATUS
    # ========================================================

    print("\n")

    print("=" * 80)

    print("                    PROJECT STATUS")

    print("=" * 80)

    print("Data Source       : CoinMarketCap")

    print("Scraping Tool     : Selenium")

    print("Data Format       : CSV")

    print(
        f"Records Collected: {len(df)}"
    )

    print(
        f"Timestamp         : {timestamp}"
    )

    print("Status            : SUCCESS")

    print("=" * 80)


except Exception as e:

    print("\nERROR OCCURRED:")

    print(e)


finally:

    time.sleep(3)

    driver.quit()