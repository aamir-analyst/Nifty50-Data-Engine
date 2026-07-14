<p align="center">
  <img src="images/banner.png" width="100%" alt="Nifty50 Data Engine Banner">
</p>

<h1 align="center">📈 Nifty50 Data Engine</h1>

<p align="center">
Production-Ready End-to-End <b>NIFTY50 Stock Market Data Engineering Pipeline</b>
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-2.x-green?style=for-the-badge&logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)
![Pytest](https://img.shields.io/badge/Pytest-Tested-success?style=for-the-badge&logo=pytest)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

</p>

---

# 🚀 Overview

Nifty50 Data Engine is a **production-ready stock market data pipeline** built with Python.

It automates the complete workflow of downloading, validating, cleaning, storing and transforming historical NIFTY50 stock data into **machine learning-ready datasets**.

The project follows a modular architecture inspired by real-world Data Engineering practices.

---

# 📊 Project Statistics

| Metric | Value |
|---------|------:|
| Stocks Covered | 50 |
| Historical Data | 2000 – Present |
| Dataset Size | 285,000+ Rows |
| Database | SQLite |
| Export Formats | CSV + Parquet |
| Technical Indicators | 10+ |
| Testing Framework | Pytest |
| CLI Support | ✅ |

---

# 🏗 Architecture

```text
                 Yahoo Finance
                       │
                       ▼
              Stock Downloader
                       │
                       ▼
               CSV File Generator
                       │
                       ▼
                  Data Merger
                       │
                       ▼
                SQLite Database
                       │
                       ▼
                 Data Validator
                       │
                       ▼
             Feature Engineering
                       │
          ┌────────────┴────────────┐
          ▼                         ▼

     features.csv          features.parquet
```

---

# ✨ Features

## 📥 Data Collection

- Download historical NIFTY50 stock data
- Automatic retry mechanism
- Progress tracking
- Multi-stock support

---

## 🧹 Data Processing

- Merge all stock datasets
- Duplicate detection
- Missing value validation
- Price validation
- Volume validation

---

## 💾 Storage

- SQLite Database
- CSV Export
- Parquet Export

---

## 📈 Feature Engineering

The pipeline automatically generates:

- SMA (20, 50, 100, 200)
- EMA (20, 50, 200)
- RSI (14)
- MACD
- Bollinger Bands
- ATR
- Daily Return
- Log Return

---

## 🧪 Software Engineering

- Modular Project Structure
- Command Line Interface (CLI)
- Logging
- Unit Testing (Pytest)
- GitHub Actions Ready
- Clean Code Architecture

---

# 📂 Project Structure

```text
Nifty50-Data-Engine/
│
├── .github/
│   └── workflows/
│
├── config/
├── scraper/
├── database_manager/
├── features/
├── ml/
├── tests/
├── utils/
│
├── data/
│   ├── metadata/
│   ├── raw/
│   └── processed/
│
├── images/
├── notebooks/
│
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
├── CHANGELOG.md
└── .gitignore
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/aamir-analyst/Nifty50-Data-Engine.git
```

Go into the project

```bash
cd Nifty50-Data-Engine
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

# ▶️ Usage

Run the complete pipeline

```bash
python main.py --all
```

Download data

```bash
python main.py --download
```

Merge datasets

```bash
python main.py --merge
```

Validate dataset

```bash
python main.py --validate
```

Generate features

```bash
python main.py --features
```

---

# 🧪 Run Tests

```bash
pytest
```

Coverage

```bash
pytest --cov=.
```

---

# 📈 Technical Indicators

| Indicator | Purpose |
|------------|----------|
| SMA | Trend Analysis |
| EMA | Short-Term Trend |
| RSI | Momentum |
| MACD | Trend + Momentum |
| Bollinger Bands | Volatility |
| ATR | Average True Range |
| Daily Return | Daily Performance |
| Log Return | Quantitative Finance |

---

# 🛠 Tech Stack

- Python
- Pandas
- NumPy
- yfinance
- SQLite
- TA
- PyArrow
- Rich
- Pytest

---

# 📌 Roadmap

## ✅ Version 2.0

- Historical Downloader
- Data Merger
- SQLite Database
- Data Validator

---

## ✅ Version 2.2

- Feature Engineering
- CLI
- CSV Export
- Parquet Export
- Unit Testing
- GitHub Repository

---

## 🚀 Version 2.3

- Docker Support
- HTML Reports
- Rich Terminal Dashboard

---

## 🚀 Version 3.0

- ML Dataset
- Random Forest
- XGBoost
- LightGBM
- LSTM
- Transformer Models

---

## 🚀 Version 4.0

- FastAPI
- Streamlit Dashboard
- Live Market Updates
- Portfolio Analytics

---

# 🤝 Contributing

Contributions are welcome.

If you find a bug or have an idea for improvement, feel free to open an Issue or submit a Pull Request.

---

# 📄 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

## Aamir

**B.Sc. Data Science & Artificial Intelligence**

GitHub:

https://github.com/aamir-analyst

---

<p align="center">

⭐ If you found this project useful, please consider giving it a Star.

</p>