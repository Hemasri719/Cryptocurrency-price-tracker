import os
import pandas as pd


def test_csv_file_exists():

    file_path = "crypto_data.csv"

    assert os.path.exists(file_path), \
        "crypto_data.csv file does not exist"


def test_csv_has_required_columns():

    df = pd.read_csv("crypto_data.csv")

    required_columns = [
        "timestamp",
        "name",
        "symbol",
        "price_usd",
        "change_24h_pct",
        "market_cap_usd"
    ]

    for column in required_columns:

        assert column in df.columns, \
            f"Missing column: {column}"


def test_price_values_are_valid():

    df = pd.read_csv("crypto_data.csv")

    assert (
        pd.to_numeric(
            df["price_usd"],
            errors="coerce"
        ).notna().all()
    ), "Invalid price value found"


def test_coin_names_are_not_empty():

    df = pd.read_csv("crypto_data.csv")

    assert (
        df["name"]
        .astype(str)
        .str.strip()
        .ne("")
        .all()
    ), "Empty cryptocurrency name found"


def test_timestamp_exists():

    df = pd.read_csv("crypto_data.csv")

    assert (
        df["timestamp"]
        .notna()
        .all()
    ), "Missing timestamp found"