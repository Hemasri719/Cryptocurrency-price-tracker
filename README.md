# 🚀 Cryptocurrency Price Tracker

## Selenium-Based Real-Time Cryptocurrency Data Collection, Analysis and Visualization System

---

## 📌 1. Project Overview

The Cryptocurrency Price Tracker is a Python-based web automation and data analysis project developed to automatically collect real-time cryptocurrency market information from CoinMarketCap.

The project uses Selenium WebDriver with Google Chrome to automate browser interaction and extract dynamically loaded cryptocurrency data.

The system collects important information such as:

- Cryptocurrency Name
- Cryptocurrency Symbol
- Current Price in USD
- 24-Hour Percentage Change
- Market Capitalization
- Timestamp of data collection

The collected information is validated, processed using Pandas, displayed in the terminal, and stored in a CSV file for historical analysis.

The project has also been upgraded with additional features such as:

- Connection retry handling
- Page-load timeout handling
- Dynamic table waiting
- Data validation
- Error handling
- Application logging
- Centralized configuration
- Secure environment configuration
- Automated testing using Pytest
- Top-gainer analysis
- Price-threshold filtering
- Historical data storage
- Streamlit dashboard visualization

Therefore, the project is not limited to basic web scraping. It provides a complete workflow from data collection to validation, storage, analysis, testing, monitoring and visualization.

---

# 🎯 2. Project Objective

The main objective of this project is to automate cryptocurrency market-data collection and provide a simple system for monitoring and analyzing cryptocurrency information.

The project aims to:

1. Automatically open CoinMarketCap using Selenium.
2. Handle JavaScript-rendered web content.
3. Extract the top 10 cryptocurrency records.
4. Collect price, 24-hour change and market capitalization.
5. Validate the scraped information.
6. Store the data in CSV format.
7. Maintain timestamped historical records.
8. Identify top cryptocurrency gainers.
9. Filter cryptocurrencies based on price.
10. Record application activities using logs.
11. Test important functionality automatically.
12. Display the collected information through a dashboard.

---

# 💡 3. Problem Statement

Cryptocurrency prices change continuously.

Manually checking and recording cryptocurrency prices is time-consuming and makes historical comparison difficult.

This project solves this problem by automating the data collection process.

Instead of manually opening a cryptocurrency website and recording the information, Selenium automatically opens the website, waits for the dynamically loaded data, extracts the required information, validates it and stores it for future analysis.

The historical data can then be used for:

- Price comparison
- Trend analysis
- Cryptocurrency monitoring
- Basic market analysis
- Dashboard visualization

---

# ⚙️ 4. How the Project Works

The complete workflow of the application is:

    User runs main.py
             ↓
    Load project configuration
             ↓
    Start Chrome WebDriver
             ↓
    Open CoinMarketCap
             ↓
    Handle connection attempts
             ↓
    Wait for cryptocurrency table
             ↓
    Extract cryptocurrency rows
             ↓
    Extract Name, Symbol, Price,
    24h Change and Market Cap
             ↓
    Validate collected data
             ↓
    Collect Top 10 valid records
             ↓
    Create Pandas DataFrame
             ↓
    Display data in terminal
             ↓
    Save data to crypto_data.csv
             ↓
    Identify Top Gainers
             ↓
    Apply Price Threshold Filter
             ↓
    Write execution logs
             ↓
    Run automated tests
             ↓
    Display data using Streamlit Dashboard

---

# 🌐 5. Data Source

The primary data source used by the project is:

**CoinMarketCap**

Website:

https://coinmarketcap.com/

The project uses Selenium WebDriver because the cryptocurrency table is dynamically rendered by the website.

The application does not depend on manually copying cryptocurrency information.

---

# 🧰 6. Technologies Used

## Programming Language

### Python

Python is used as the main programming language for:

- Web automation
- Data extraction
- Data validation
- Data processing
- CSV storage
- Logging
- Testing
- Dashboard development

---

## Web Automation

### Selenium WebDriver

Selenium is used to automate Google Chrome.

It performs tasks such as:

- Opening Chrome
- Navigating to CoinMarketCap
- Waiting for dynamic content
- Locating cryptocurrency table rows
- Extracting cryptocurrency information

---

## Browser

### Google Chrome

Google Chrome is used as the browser controlled by Selenium WebDriver.

---

## Driver Management

### webdriver-manager

`webdriver-manager` is used to automatically manage the ChromeDriver required by Selenium.

This reduces the need to manually download and configure ChromeDriver.

---

## Data Processing

### Pandas

Pandas is used to:

- Create DataFrames
- Process scraped data
- Sort cryptocurrencies
- Identify top gainers
- Filter records
- Export data to CSV

---

## Dashboard

### Streamlit

Streamlit is used to create an interactive web dashboard.

The dashboard provides a visual representation of the cryptocurrency data stored in the CSV file.

---

## Testing

### Pytest

Pytest is used to automatically test important parts of the project.

The current project contains five automated test cases.

---

## Configuration

### Python Configuration File

`config.py` is used to store configurable project settings such as:

- CoinMarketCap URL
- Page-load timeout
- Table wait timeout
- Number of cryptocurrencies
- Number of top gainers
- Price threshold
- Headless browser mode

---

## Environment Configuration

### python-dotenv / .env

Environment-based configuration can be used for sensitive values such as API keys.

Sensitive credentials should not be directly written inside the source code.

---

## Logging

### Python Logging Module

The built-in Python logging module is used to record:

- Application startup
- WebDriver startup
- Website connection attempts
- Data collection
- Validation errors
- CSV storage
- Application errors
- Application completion

---

# ✨ 7. Original Project Features

The project implements the features specified in the original project description.

---

## 7.1 Live Price Scraping

The system automatically collects live cryptocurrency information from CoinMarketCap.

The collected data includes:

- Cryptocurrency name
- Symbol
- Current price
- 24-hour change
- Market capitalization

---

## 7.2 Dynamic Page Handling

CoinMarketCap uses dynamically loaded web content.

Selenium waits for the cryptocurrency table to become available before extracting the data.

This allows the project to handle JavaScript-rendered content.

---

## 7.3 Top 10 Cryptocurrency Tracking

The application collects the top 10 valid cryptocurrency records.

The number of cryptocurrencies can be changed through `config.py`.

Example:

    TOP_COINS = 10

---

## 7.4 CSV Export

The collected data is stored in:

    crypto_data.csv

New records are appended to the existing CSV file.

This allows historical cryptocurrency data to be maintained.

---

## 7.5 Headless Browser

The project supports headless Chrome execution.

When enabled, Chrome runs without displaying the browser window.

This is useful for automated/background execution.

The setting can be controlled through:

    config.py

---

## 7.6 Historical Logging

Each record contains a timestamp.

Example:

    2026-10-01 21:24:59

Each execution adds new timestamped records to the CSV file.

This makes the dataset useful for historical analysis.

---

## 7.7 Cryptocurrency Filtering

The project can filter cryptocurrencies based on:

- Price threshold
- 24-hour percentage change

This provides additional analysis beyond simple data collection.

---

# 🚀 8. Additional Features Implemented

The project was upgraded beyond the basic requirements to improve reliability, maintainability, data quality and usability.

---

## 8.1 Connection Retry Mechanism

If CoinMarketCap temporarily fails to load, the application attempts the connection again.

Example:

    Connection attempt 1/3...
    Connection attempt 2/3...
    Connection attempt 3/3...

This improves reliability during temporary network problems.

---

## 8.2 Page Load Timeout

A page-load timeout is configured so that the application does not wait indefinitely for a website response.

Example:

    PAGE_LOAD_TIMEOUT = 30

The timeout value can be changed in `config.py`.

---

## 8.3 Explicit Waiting

The application waits for the cryptocurrency table before attempting to extract information.

This is important because the data is dynamically loaded.

The project uses Selenium's:

    WebDriverWait
    Expected Conditions

This reduces problems caused by attempting to read the page before the data is available.

---

## 8.4 Data Validation

The project validates the collected data before storing it.

### Price Validation

The price must be numeric and greater than zero.

Example:

    $84,070.34

is converted into a numeric value before storage.

### 24-Hour Change Validation

The 24-hour percentage change must contain a valid numeric value.

Example:

    -0.14%

### Market Capitalization Validation

The application checks whether market capitalization data is available.

### Name and Symbol Validation

Records without valid cryptocurrency name and symbol information are ignored.

### Record Count Validation

The application verifies that the expected number of cryptocurrency records has been collected.

For example:

    Expected: 10
    Collected: 10

---

# 🛡️ 9. Error Handling

The application contains error handling for possible runtime problems.

Examples include:

- Website connection timeout
- Page loading failure
- Invalid price
- Invalid percentage change
- Missing market capitalization
- Missing cryptocurrency name
- Missing cryptocurrency symbol
- Insufficient records
- WebDriver errors
- Unexpected runtime errors

When an error occurs:

1. The error is displayed in the terminal.
2. The error is written to the log file.
3. The browser is closed safely.

---

# 📋 10. Application Logging

The project creates a log directory:

    logs/

The main log file is:

    logs/tracker.log

The log contains information about application execution.

Example:

    INFO | Cryptocurrency tracking started
    INFO | Chrome WebDriver started successfully
    INFO | Opening CoinMarketCap
    INFO | Connection attempt 1/3
    INFO | CoinMarketCap opened successfully
    INFO | Successfully collected 10 cryptocurrencies
    INFO | Data saved successfully

Logging is useful for:

- Debugging
- Error investigation
- Monitoring
- Understanding application execution

---

# ⚙️ 11. Centralized Configuration

The project uses:

    config.py

to store important configuration values.

Typical settings include:

    COINMARKETCAP_URL
    PAGE_LOAD_TIMEOUT
    TABLE_WAIT_TIMEOUT
    TOP_COINS
    TOP_GAINERS
    PRICE_THRESHOLD
    HEADLESS_MODE

This makes the project easier to maintain.

For example, instead of modifying the main program to change the number of cryptocurrencies, the value can be changed in `config.py`.

---

# 🔐 12. Security Practices

Basic security practices have been included in the upgraded project.

## Environment Variables

Sensitive values such as API keys can be stored in `.env`.

Example:

    CMC_API_KEY=YOUR_API_KEY

The actual secret value should not be publicly exposed.

## Git Ignore

The `.gitignore` file prevents sensitive and unnecessary files from being committed.

Important entries include:

    .env
    venv/
    __pycache__/
    *.pyc

## Data Validation

Scraped information is validated before being stored.

## Error Handling

Runtime errors are handled instead of allowing the application to crash without information.

---

# 🧪 13. Automated Testing

The project includes automated tests using Pytest.

Test file:

    tests/test_tracker.py

The tests verify important data conditions such as:

- Required CSV columns
- Valid price values
- Non-empty cryptocurrency names
- Timestamp availability
- CSV data integrity

---

## Running Tests

Use:

    pytest

Expected successful result:

    collected 5 items

    tests/test_tracker.py .....

    5 passed

A result such as:

    5 passed

means all five implemented test cases passed successfully.

---

# 📊 14. Data Stored in CSV

The main data file is:

    crypto_data.csv

The CSV contains:

| Column | Description |
|---|---|
| timestamp | Date and time when data was collected |
| name | Cryptocurrency name |
| symbol | Cryptocurrency symbol |
| price_usd | Current price in USD |
| change_24h_pct | 24-hour percentage change |
| market_cap_usd | Market capitalization |

Example:

    timestamp,name,symbol,price_usd,change_24h_pct,market_cap_usd

    2026-10-01 21:24:59,Bitcoin,BTC,84070.34,-0.14,...

    2026-10-01 21:24:59,Ethereum,ETH,2682.30,-0.09,...

---

# 📈 15. Top Gainers Analysis

The project identifies cryptocurrencies with the highest 24-hour percentage change.

Example:

    ================================================================
                         TOP 3 GAINERS
    ================================================================

    Bitcoin (BTC) --> 2.50%
    Ethereum (ETH) --> 1.80%
    Solana (SOL) --> 1.25%

The number of top gainers is configurable.

This feature converts raw scraped information into useful basic market analysis.

---

# 💰 16. Price Threshold Filter

The project can identify cryptocurrencies whose current price is above a configured threshold.

Example:

    ================================================================
                       COINS ABOVE $100
    ================================================================

    Bitcoin (BTC) --> $84,070.34
    Ethereum (ETH) --> $2,682.30

The threshold can be configured using:

    PRICE_THRESHOLD

---

# 📊 17. Streamlit Dashboard

An interactive dashboard has been added as an additional upgrade.

The dashboard reads the collected CSV data and presents the information in a visual format.

Run the dashboard using:

    streamlit run dashboard.py

The dashboard is normally available at:

    http://localhost:8501

---

# 🖥️ 18. Dashboard Output

The dashboard can display:

### Summary Information

- Number of cryptocurrencies tracked
- Total historical records
- Average 24-hour change
- Highest cryptocurrency price

### Latest Cryptocurrency Data

- Name
- Symbol
- Price
- 24-hour change
- Market capitalization

### Top Gainers

Shows cryptocurrencies with the highest 24-hour percentage change.

### Price Analysis

Provides visual comparison of cryptocurrency prices.

### 24-Hour Change Analysis

Provides visual comparison of cryptocurrency percentage changes.

### Historical Data

Displays previously collected timestamped cryptocurrency records.

---

# 🖥️ 19. Expected Dashboard Structure

The dashboard follows a structure similar to:

    =========================================================
             CRYPTOCURRENCY PRICE TRACKER
    =========================================================

    Coins Tracked       : 10
    Total Records       : 50+
    Average 24h Change  : ...
    Highest Price       : ...

    ---------------------------------------------------------
                    LATEST CRYPTOCURRENCY DATA
    ---------------------------------------------------------

    Name        Symbol      Price       24h Change
    Bitcoin     BTC         $84,070     -0.14%
    Ethereum    ETH         $2,682      -0.09%
    Solana      SOL         $117        -1.78%

    ---------------------------------------------------------
                         TOP GAINERS
    ---------------------------------------------------------

    ...

    ---------------------------------------------------------
                       PRICE ANALYSIS
    ---------------------------------------------------------

                     [Interactive Chart]

    ---------------------------------------------------------
                   24-HOUR CHANGE ANALYSIS
    ---------------------------------------------------------

                     [Interactive Chart]

    ---------------------------------------------------------
                       HISTORICAL DATA
    ---------------------------------------------------------

                     [Data Table]

The actual values change whenever new live cryptocurrency data is collected.

---

# 💻 20. Expected Terminal Output

When the main program executes successfully, the terminal output follows a structure similar to:

    ================================================================================
                 CRYPTOCURRENCY PRICE TRACKER
    ================================================================================

    Starting Chrome WebDriver...
    Chrome WebDriver started successfully!

    Opening CoinMarketCap...
    Connection attempt 1/3...
    CoinMarketCap opened successfully!

    Waiting for cryptocurrency data...
    Rows found on CoinMarketCap: ...

    ================================================================================

                     TOP 10 CRYPTOCURRENCIES

    ================================================================================

    Rank       : 1
    Name       : Bitcoin
    Symbol     : BTC
    Price      : $84,070.34
    24h Change : -0.14%
    Market Cap : ...

    Rank       : 2
    Name       : Ethereum
    Symbol     : ETH
    Price      : $2,682.30
    24h Change : -0.09%
    Market Cap : ...

    ...

    Total cryptocurrencies collected: 10

    ================================================================================

    Data saved successfully to: crypto_data.csv

    ================================================================================

                         TOP GAINERS

    ================================================================================

    Bitcoin (BTC) --> ...
    Ethereum (ETH) --> ...
    Solana (SOL) --> ...

    ================================================================================

                       COINS ABOVE PRICE THRESHOLD

    ================================================================================

    ...

    ================================================================================

                         PROJECT STATUS

    ================================================================================

    Data Source       : CoinMarketCap
    Scraping Tool     : Selenium
    Data Format       : CSV
    Records Collected : 10
    Timestamp         : 2026-10-01 21:24:59
    Headless Mode     : False
    Data Validation   : ENABLED
    Logging           : ENABLED
    Status            : SUCCESS

    ================================================================================

    Chrome browser closed.
    Tracker execution completed.

---

# 🗂️ 21. Project Structure

The project is organized as follows:

    Cryptocurrency-price-tracker/
    │
    ├── main.py
    ├── dashboard.py
    ├── config.py
    ├── requirements.txt
    ├── README.md
    ├── .gitignore
    ├── .env
    ├── crypto_data.csv
    │
    ├── logs/
    │   └── tracker.log
    │
    ├── tests/
    │   └── test_tracker.py
    │
    └── venv/

---

# 📁 22. File and Folder Explanation

## main.py

Main application file.

Responsible for:

- Starting Selenium
- Starting Chrome WebDriver
- Opening CoinMarketCap
- Handling retries
- Waiting for cryptocurrency data
- Scraping data
- Validating data
- Creating DataFrame
- Saving CSV
- Finding top gainers
- Applying price filter
- Displaying status
- Closing browser

---

## dashboard.py

Creates the Streamlit dashboard.

Responsible for displaying:

- Cryptocurrency information
- Summary metrics
- Top gainers
- Price analysis
- 24-hour change analysis
- Historical data

---

## config.py

Contains project configuration values.

This allows settings to be changed without modifying the main application logic.

---

## requirements.txt

Contains the Python packages required to run the project.

Main dependencies include:

    selenium
    webdriver-manager
    pandas
    streamlit
    pytest
    python-dotenv

---

## crypto_data.csv

Stores historical cryptocurrency market data.

New records are appended when the tracker runs successfully.

---

## logs/tracker.log

Stores application execution logs and errors.

---

## tests/test_tracker.py

Contains automated Pytest test cases.

---

## .env

Stores sensitive environment configuration when required.

The real `.env` file should not be uploaded publicly.

---

## .gitignore

Prevents sensitive and unnecessary files from being committed to Git.

---

## venv/

Python virtual environment containing project-specific packages.

---

# 🔄 23. Complete System Architecture

The project architecture can be represented as:

                         COINMARKETCAP
                                |
                                ↓
                       SELENIUM WEBDRIVER
                                |
                                ↓
                    DYNAMIC DATA EXTRACTION
                                |
                                ↓
                        DATA VALIDATION
                                |
                                ↓
                       PANDAS DATAFRAME
                         /           \
                        /             \
                       ↓               ↓
              CSV DATA STORAGE     DATA ANALYSIS
                                      /      \
                                     /        \
                                    ↓          ↓
                              TOP GAINERS   PRICE FILTER
                                    |
                                    ↓
                          STREAMLIT DASHBOARD


Additional monitoring:

    Application
        |
        └── logs/tracker.log


Automated testing:

    Project
        |
        └── Pytest
              |
              └── 5 Test Cases

---

# 🔧 24. Installation and Setup

## Step 1: Open the Project

Open the project folder in Visual Studio Code.

Example:

    Cryptocurrency-price-tracker

---

## Step 2: Create Virtual Environment

Run:

    python -m venv venv

---

## Step 3: Activate Virtual Environment

Windows PowerShell:

    venv\Scripts\activate

---

## Step 4: Install Required Packages

Run:

    pip install -r requirements.txt

---

## Step 5: Configure the Project

Check:

    config.py

Configure the required values such as:

    TOP_COINS
    TOP_GAINERS
    PRICE_THRESHOLD
    HEADLESS_MODE
    PAGE_LOAD_TIMEOUT

---

## Step 6: Configure Environment Variables

If required, create:

    .env

Store sensitive configuration values there.

Do not publish actual API keys.

---

# ▶️ 25. How to Run the Project

## Run Cryptocurrency Tracker

    python main.py

The program will start Chrome, access CoinMarketCap, collect the required information, validate the records, save the CSV data and display the analysis.

---

## Run Automated Tests

    pytest

Expected:

    5 passed

---

## Run Dashboard

    streamlit run dashboard.py

Then open:

    http://localhost:8501

---

# 🧪 26. Testing Status

The project has automated tests for important data conditions.

Current test coverage includes:

- CSV required columns
- Price validation
- Cryptocurrency name validation
- Timestamp validation
- CSV data integrity

Successful test result:

    5 passed

This indicates that all currently implemented automated test cases passed successfully.

---

# 🔒 27. Reliability and Security Improvements

The project was upgraded to make it more suitable for a real-world development environment.

### Reliability Improvements

- Connection retry mechanism
- Page-load timeout
- Explicit Selenium waits
- Data validation
- Record count validation
- Exception handling
- Automatic browser cleanup

### Security Improvements

- Environment-based configuration
- `.env` protection
- `.gitignore`
- Avoiding hard-coded sensitive credentials
- Input/data validation

### Maintainability Improvements

- Centralized configuration
- Structured project folders
- Logging
- Separate dashboard
- Separate test files

---

# 📌 28. Why This Project Was Upgraded

The basic version of the project focused mainly on scraping cryptocurrency information and saving it into a CSV file.

The project was upgraded to make it more complete and practical.

The upgrades were introduced for the following reasons:

### Reliability

Connection retries and timeout handling help the application deal with temporary connection problems.

### Data Quality

Validation prevents obviously invalid records from being stored.

### Maintainability

Centralized configuration makes the project easier to modify.

### Monitoring

Logging makes it