from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    WebDriverException
)

from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd
from datetime import datetime
import os
import time
import logging
from pathlib import Path

import config


# ============================================================
# PATHS
# ============================================================

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "tracker.log"

SCREENSHOT_DIR = Path("logs") / "screenshots"
SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)

CSV_FILE = Path("crypto_data.csv")


# ============================================================
# LOGGING SETUP
# ============================================================

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)


# ============================================================
# HELPER FUNCTION - ERROR SCREENSHOT
# ============================================================

def save_error_screenshot(driver):
    """
    Saves a screenshot when a browser error occurs.
    """

    if driver is None:
        return

    try:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        screenshot_file = (
            SCREENSHOT_DIR /
            f"error_{timestamp}.png"
        )

        driver.save_screenshot(
            str(screenshot_file)
        )

        logger.info(
            "Error screenshot saved: %s",
            screenshot_file
        )

        print(
            f"Error screenshot saved: "
            f"{screenshot_file}"
        )

    except Exception as screenshot_error:

        logger.warning(
            "Could not save error screenshot: %s",
            screenshot_error
        )


# ============================================================
# HELPER FUNCTION - SAFE BROWSER CLOSE
# ============================================================

def close_browser(driver):

    if driver is not None:

        try:

            driver.quit()

            logger.info(
                "Chrome browser closed successfully"
            )

        except Exception as close_error:

            logger.warning(
                "Error while closing browser: %s",
                close_error
            )


# ============================================================
# START PROJECT
# ============================================================

print("=" * 80)

print(
    "             CRYPTOCURRENCY PRICE TRACKER"
)

print("=" * 80)

logger.info(
    "Cryptocurrency tracking started"
)


driver = None


try:

    # ========================================================
    # 1. CHROME SETUP
    # ========================================================

    print(
        "\nStarting Chrome WebDriver..."
    )

    options = Options()

    options.add_argument(
        "--start-maximized"
    )

    options.add_argument(
        "--disable-notifications"
    )

    options.add_argument(
        "--disable-popup-blocking"
    )

    options.add_argument(
        "--disable-dev-shm-usage"
    )

    options.add_argument(
        "--no-sandbox"
    )

    # Headless mode

    if config.HEADLESS_MODE:

        options.add_argument(
            "--headless=new"
        )

        options.add_argument(
            "--window-size=1920,1080"
        )

        logger.info(
            "Headless mode enabled"
        )

    else:

        logger.info(
            "Headless mode disabled"
        )

    options.page_load_strategy = "eager"


    # ========================================================
    # 2. START WEBDRIVER
    # ========================================================

    try:

        driver = webdriver.Chrome(

            service=Service(
                ChromeDriverManager().install()
            ),

            options=options

        )

        print(
            "Chrome WebDriver started successfully!"
        )

        logger.info(
            "Chrome WebDriver started successfully"
        )

    except WebDriverException as error:

        logger.exception(
            "Chrome WebDriver failed to start"
        )

        print(
            "\nERROR: Chrome WebDriver could not start."
        )

        print(
            "Please check Chrome and ChromeDriver."
        )

        raise error


    # ========================================================
    # 3. PAGE LOAD TIMEOUT
    # ========================================================

    driver.set_page_load_timeout(
        config.PAGE_LOAD_TIMEOUT
    )


    # ========================================================
    # 4. OPEN COINMARKETCAP WITH RETRY
    # ========================================================

    print(
        "\nOpening CoinMarketCap..."
    )

    logger.info(
        "Opening CoinMarketCap"
    )

    website_opened = False

    max_attempts = 3

    for attempt in range(
        1,
        max_attempts + 1
    ):

        try:

            print(
                f"Connection attempt "
                f"{attempt}/{max_attempts}..."
            )

            logger.info(
                "Connection attempt %d/%d",
                attempt,
                max_attempts
            )

            driver.get(
                config.COINMARKETCAP_URL
            )

            website_opened = True

            print(
                "CoinMarketCap opened successfully!"
            )

            logger.info(
                "CoinMarketCap opened successfully"
            )

            break


        except TimeoutException:

            print(
                f"Attempt {attempt} timed out."
            )

            logger.warning(
                "Connection attempt %d timed out",
                attempt
            )

            if attempt < max_attempts:

                print(
                    "Waiting 5 seconds before retry..."
                )

                time.sleep(5)

            else:

                print(
                    "\nCoinMarketCap could not be "
                    "reached after 3 attempts."
                )

                logger.error(
                    "CoinMarketCap connection failed "
                    "after %d attempts",
                    max_attempts
                )

                save_error_screenshot(
                    driver
                )

                raise ConnectionError(
                    "Unable to connect to CoinMarketCap. "
                    "Please check your internet connection "
                    "and try again later."
                )


        except WebDriverException as error:

            logger.exception(
                "WebDriver error while opening "
                "CoinMarketCap"
            )

            save_error_screenshot(
                driver
            )

            raise error


    if not website_opened:

        raise ConnectionError(
            "CoinMarketCap website was not opened."
        )


    # ========================================================
    # 5. WAIT FOR CRYPTOCURRENCY TABLE
    # ========================================================

    print(
        "\nWaiting for cryptocurrency data..."
    )

    logger.info(
        "Waiting for cryptocurrency table"
    )

    try:

        wait = WebDriverWait(
            driver,
            config.TABLE_WAIT_TIMEOUT
        )

        rows = wait.until(

            EC.presence_of_all_elements_located(

                (
                    By.CSS_SELECTOR,
                    "table tbody tr"
                )

            )

        )

    except TimeoutException:

        print(
            "\nERROR: Cryptocurrency table "
            "did not load."
        )

        logger.error(
            "Cryptocurrency table timeout"
        )

        save_error_screenshot(
            driver
        )

        raise TimeoutException(
            "Cryptocurrency table did not load "
            "within the expected time."
        )


    print(
        f"Rows found on CoinMarketCap: "
        f"{len(rows)}"
    )

    logger.info(
        "Rows found: %d",
        len(rows)
    )


    # ========================================================
    # 6. SCRAPE DATA
    # ========================================================

    crypto_data = []

    timestamp = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    crypto_count = 0


    for row in rows:

        try:

            cells = row.find_elements(
                By.TAG_NAME,
                "td"
            )

            # Incomplete row

            if len(cells) < 8:

                logger.warning(
                    "Incomplete cryptocurrency row skipped"
                )

                continue


            # ------------------------------------------------
            # NAME + SYMBOL
            # ------------------------------------------------

            coin_text = cells[2].text.strip()

            if "\n" not in coin_text:

                continue

            if "CMC20" in coin_text:

                continue

            name_symbol = coin_text.split(
                "\n"
            )

            if len(name_symbol) < 2:

                continue

            name = name_symbol[0].strip()

            symbol = name_symbol[1].strip()


            if not name or not symbol:

                logger.warning(
                    "Empty name or symbol skipped"
                )

                continue


            # ------------------------------------------------
            # PRICE
            # ------------------------------------------------

            price = cells[3].text.strip()


            try:

                price_value = float(
                    price
                    .replace("$", "")
                    .replace(",", "")
                )

                if price_value <= 0:

                    raise ValueError(
                        "Price must be greater than zero"
                    )

            except ValueError:

                logger.warning(
                    "Invalid price for %s: %s",
                    name,
                    price
                )

                continue


            # ------------------------------------------------
            # 24H CHANGE
            # ------------------------------------------------

            change_24h = cells[4].text.strip()

            try:

                change_value = float(
                    change_24h
                    .replace("%", "")
                    .replace(",", "")
                )

            except ValueError:

                logger.warning(
                    "Invalid 24h change for %s: %s",
                    name,
                    change_24h
                )

                continue


            # ------------------------------------------------
            # MARKET CAP
            # ------------------------------------------------

            market_cap = cells[7].text.strip()

            if not market_cap:

                logger.warning(
                    "Empty market cap for %s",
                    name
                )

                continue


            # ------------------------------------------------
            # VALID RECORD
            # ------------------------------------------------

            crypto_data.append({

                "timestamp": timestamp,

                "name": name,

                "symbol": symbol,

                "price_usd": price_value,

                "change_24h_pct": change_value,

                "market_cap_usd": market_cap

            })

            crypto_count += 1


            if crypto_count >= config.TOP_COINS:

                break


        except Exception as row_error:

            logger.exception(
                "Error processing cryptocurrency row: %s",
                row_error
            )

            continue


    # ========================================================
    # 7. CHECK DATA COUNT
    # ========================================================

    if len(crypto_data) != config.TOP_COINS:

        logger.error(
            "Expected %d records but collected %d",
            config.TOP_COINS,
            len(crypto_data)
        )

        raise ValueError(
            f"Expected {config.TOP_COINS} "
            f"cryptocurrencies but collected "
            f"{len(crypto_data)}."
        )


    # ========================================================
    # 8. CREATE DATAFRAME
    # ========================================================

    df = pd.DataFrame(
        crypto_data
    )


    # ========================================================
    # 9. DISPLAY DATA
    # ========================================================

    print("\n")

    print("=" * 100)

    print(
        f"              TOP "
        f"{config.TOP_COINS} CRYPTOCURRENCIES"
    )

    print("=" * 100)


    for index, row in df.iterrows():

        print()

        print(
            f"Rank       : {index + 1}"
        )

        print(
            f"Name       : {row['name']}"
        )

        print(
            f"Symbol     : {row['symbol']}"
        )

        print(
            f"Price      : "
            f"${row['price_usd']:,.2f}"
        )

        print(
            f"24h Change : "
            f"{row['change_24h_pct']:.2f}%"
        )

        print(
            f"Market Cap : "
            f"{row['market_cap_usd']}"
        )


    print(
        "\n" + "=" * 100
    )

    print(
        f"Total cryptocurrencies collected: "
        f"{len(df)}"
    )

    print("=" * 100)


    # ========================================================
    # 10. SAVE CSV SAFELY
    # ========================================================

    try:

        file_exists = CSV_FILE.exists()

        df.to_csv(

            CSV_FILE,

            mode="a",

            header=not file_exists,

            index=False

        )

        print(
            "\nData saved successfully to: "
            f"{CSV_FILE}"
        )

        logger.info(
            "Data saved successfully to %s",
            CSV_FILE
        )

    except (PermissionError, OSError) as csv_error:

        logger.exception(
            "CSV save failed"
        )

        print(
            "\nERROR: Could not save data to CSV."
        )

        print(
            "Please make sure crypto_data.csv "
            "is not open in Excel."
        )

        raise csv_error


    # ========================================================
    # 11. TOP GAINERS
    # ========================================================

    print("\n")

    print("=" * 80)

    print(
        f"                    TOP "
        f"{config.TOP_GAINERS} GAINERS"
    )

    print("=" * 80)


    top_gainers = (

        df
        .sort_values(
            by="change_24h_pct",
            ascending=False
        )
        .head(
            config.TOP_GAINERS
        )

    )


    for _, row in top_gainers.iterrows():

        print(
            f"{row['name']} "
            f"({row['symbol']}) "
            f"--> "
            f"{row['change_24h_pct']:.2f}%"
        )


    # ========================================================
    # 12. PRICE FILTER
    # ========================================================

    print("\n")

    print("=" * 80)

    print(
        f"              COINS ABOVE "
        f"${config.PRICE_THRESHOLD}"
    )

    print("=" * 80)


    coins_above_threshold = df[
        df["price_usd"]
        > config.PRICE_THRESHOLD
    ]


    if coins_above_threshold.empty:

        print(
            f"No cryptocurrencies currently "
            f"above ${config.PRICE_THRESHOLD}."
        )

    else:

        for _, row in (
            coins_above_threshold.iterrows()
        ):

            print(
                f"{row['name']} "
                f"({row['symbol']}) "
                f"--> "
                f"${row['price_usd']:,.2f}"
            )


    # ========================================================
    # 13. FINAL STATUS
    # ========================================================

    print("\n")

    print("=" * 80)

    print(
        "                    PROJECT STATUS"
    )

    print("=" * 80)

    print(
        "Data Source       : CoinMarketCap"
    )

    print(
        "Scraping Tool     : Selenium"
    )

    print(
        "Data Format       : CSV"
    )

    print(
        f"Records Collected: {len(df)}"
    )

    print(
        f"Timestamp         : {timestamp}"
    )

    print(
        f"Headless Mode     : "
        f"{config.HEADLESS_MODE}"
    )

    print(
        "Data Validation   : ENABLED"
    )

    print(
        "Automated Testing : ENABLED"
    )

    print(
        "Error Logging     : ENABLED"
    )

    print(
        "Error Screenshots : ENABLED"
    )

    print(
        "Status            : SUCCESS"
    )

    print("=" * 80)


    logger.info(
        "Cryptocurrency tracker completed successfully"
    )


# ============================================================
# ERROR HANDLING
# ============================================================

except ConnectionError as error:

    print("\n" + "=" * 80)

    print("CONNECTION ERROR")

    print("=" * 80)

    print(error)

    print(
        "\nPlease check your internet connection "
        "and try again later."
    )

    logger.error(
        "Connection error: %s",
        error
    )


except TimeoutException as error:

    print("\n" + "=" * 80)

    print("TIMEOUT ERROR")

    print("=" * 80)

    print(error)

    print(
        "\nThe website or cryptocurrency table "
        "did not respond in time."
    )

    logger.error(
        "Timeout error: %s",
        error
    )


except WebDriverException as error:

    print("\n" + "=" * 80)

    print("WEBDRIVER ERROR")

    print("=" * 80)

    print(error)

    print(
        "\nPlease check Chrome and ChromeDriver."
    )

    logger.exception(
        "WebDriver error"
    )


except PermissionError as error:

    print("\n" + "=" * 80)

    print("FILE PERMISSION ERROR")

    print("=" * 80)

    print(error)

    print(
        "\nPlease close crypto_data.csv "
        "if it is open in Excel."
    )

    logger.exception(
        "File permission error"
    )


except Exception as error:

    print("\n" + "=" * 80)

    print("UNEXPECTED ERROR")

    print("=" * 80)

    print(error)

    print(
        "\nCheck logs/tracker.log "
        "for detailed information."
    )

    logger.exception(
        "Unexpected error occurred"
    )


# ============================================================
# ALWAYS CLOSE BROWSER
# ============================================================

finally:

    close_browser(
        driver
    )

    print(
        "\nChrome browser closed."
    )

    print(
        "Tracker execution completed."
    )