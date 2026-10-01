# Cryptocurrency Price Tracker

A Python-based web scraping tool that uses Selenium and Chrome WebDriver to collect real-time cryptocurrency market data from CoinMarketCap.

The project extracts the top 10 cryptocurrencies and collects their name, symbol, current price, 24-hour price change, and market capitalization. The collected data is displayed in the terminal and stored in a CSV file with a timestamp for historical tracking and analysis.

---

## Project Description

The Cryptocurrency Price Tracker is a Selenium-powered web scraping project developed to demonstrate how dynamic, JavaScript-based websites can be accessed and processed using browser automation.

The application opens CoinMarketCap using Selenium WebDriver, waits for the cryptocurrency table to load, extracts the required market information from the webpage, and stores the results in a structured CSV file.

Each time the program is executed, a new timestamped set of cryptocurrency records is appended to the CSV file. This allows the collected data to be used for historical tracking and basic market analysis.

---

## Objectives

The main objectives of this project are:

- To understand web scraping using Selenium.
- To automate Google Chrome using Chrome WebDriver.
- To extract data from a dynamically rendered webpage.
- To collect the top 10 cryptocurrencies by market ranking.
- To store scraped data in CSV format.
- To maintain historical records using timestamps.
- To identify the top 3 cryptocurrencies based on 24-hour price change.
- To filter cryptocurrencies based on a price threshold.

---

## Features

### 1. Real-Time Cryptocurrency Scraping

The application retrieves current cryptocurrency market information directly from CoinMarketCap when the program is executed.

### 2. Selenium Web Scraping

Selenium WebDriver is used to automate Chrome and extract information from the dynamically rendered CoinMarketCap webpage.

### 3. Top 10 Cryptocurrency Data

The application collects data for the first 10 valid cryptocurrencies found on the CoinMarketCap market table.

The following information is collected:

- Cryptocurrency name
- Cryptocurrency symbol
- Current price in USD
- 24-hour price change
- Market capitalization

### 4. Timestamped Historical Logging

Every successful execution adds a timestamp to the collected records.

The data is appended to `crypto_data.csv` instead of replacing previous records.

This creates a historical dataset that can be used for future analysis.

### 5. CSV Export

The scraped data is stored in a structured CSV file named:

`crypto_data.csv`

### 6. Top 3 Gainers

The application sorts the collected cryptocurrencies according to their 24-hour percentage change and displays the top 3 gainers.

### 7. Price Threshold Filtering

The application identifies and displays all cryptocurrencies whose current price is greater than $100.

### 8. Error Handling

The application includes exception handling for problems that may occur while loading the website or scraping the data.

### 9. Connection Retry

The application attempts to reconnect to CoinMarketCap when a page-loading timeout occurs.

---

## Technologies Used

### Programming Language

- Python

### Libraries

- Selenium
- pandas
- webdriver-manager
- datetime
- os
- time

### Browser Automation

- Google Chrome
- ChromeDriver
- Selenium WebDriver

### Data Storage

- CSV

### Data Source

- CoinMarketCap

---

## How the Project Works

The project follows these steps:

1. The Python program starts.
2. Selenium starts Google Chrome using Chrome WebDriver.
3. The program opens CoinMarketCap.
4. Selenium waits for the cryptocurrency table to load.
5. The program identifies the cryptocurrency rows.
6. Non-cryptocurrency rows such as the CMC20 index are ignored.
7. The first 10 valid cryptocurrency records are extracted.
8. The program extracts:
   - Name
   - Symbol
   - Price
   - 24-hour change
   - Market cap
9. A timestamp is added to every record.
10. The data is converted into a pandas DataFrame.
11. The top 10 cryptocurrency details are displayed in the terminal.
12. The data is appended to `crypto_data.csv`.
13. The top 3 gainers are identified.
14. Cryptocurrencies priced above $100 are displayed.
15. A final project status is displayed.

---

## Project Structure

```text
Cryptocurrency-price-tracker/
│
├── driver/
│   └── chromedriver.exe
│
├── venv/
│
├── main.py
├── selenium_test.py
├── crypto_data.csv
├── README.md
├── requirements.txt
└── .gitignore