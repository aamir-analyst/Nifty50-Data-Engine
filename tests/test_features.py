import pandas as pd

from features.indicators import IndicatorEngine


def test_indicator_engine():

    df = pd.DataFrame(
        {
            "Date": pd.date_range("2024-01-01", periods=250),
            "Symbol": ["TEST"] * 250,
            "Open": range(250),
            "High": range(1, 251),
            "Low": range(250),
            "Close": range(250),
            "Adj Close": range(250),
            "Volume": [1000] * 250,
        }
    )

    result = IndicatorEngine(df).calculate()

    assert "SMA_20" in result.columns
    assert "EMA_20" in result.columns
    assert "RSI_14" in result.columns
    assert "MACD" in result.columns