# 📈 Nifty50 Data Engine

> A production-ready end-to-end **NIFTY 50 Stock Market Data Engineering Pipeline** built with Python.

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

# 🚀 Project Overview

Nifty50 Data Engine is a complete stock market data pipeline that automatically:

- Downloads historical NIFTY50 stock data
- Cleans and validates data
- Stores data in SQLite
- Generates technical indicators
- Creates ML-ready datasets
- Exports CSV & Parquet files

---

# ✨ Features

✅ Historical Data Downloader (2000–2026)

✅ Automatic Data Merge

✅ SQLite Database

✅ Data Validation

✅ Technical Indicators

- SMA (20,50,100,200)
- EMA (20,50,200)
- RSI (14)
- MACD
- Bollinger Bands
- ATR
- Daily Return
- Log Return

✅ CSV Export

✅ Parquet Export

✅ Command Line Interface

---

# 📂 Project Structure

```text
Nifty50-Data-Engine/
│
├── config/
├── scraper/
├── database_manager/
├── features/
├── ml/
├── utils/
├── reports/
├── logs/
├── models/
├── tests/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── metadata/
│
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Nifty50-Data-Engine.git
```

Go to project

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

Install dependencies

```bash
python -m pip install -r requirements.txt
```

---

# ▶️ Usage

Run complete pipeline

```bash
python main.py --all
```

Download only

```bash
python main.py --download
```

Merge only

```bash
python main.py --merge
```

Validate only

```bash
python main.py --validate
```

Generate Features

```bash
python main.py --features
```

---

# 📊 Output

Generated files

```text
data/

raw/
merged/

processed/
features.csv
features.parquet

database/
nifty.db
```

---

# 📈 Feature Engineering

The project generates:

| Indicator | Description |
|------------|-------------|
| SMA | Trend |
| EMA | Fast Trend |
| RSI | Momentum |
| MACD | Trend + Momentum |
| Bollinger Bands | Volatility |
| ATR | Average True Range |
| Daily Return | Daily Change |
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

---

# 📌 Roadmap

### ✅ Version 2.0

- Downloader
- Merger
- SQLite
- Validator

### ✅ Version 2.2

- Feature Engineering
- CLI
- Parquet Export

### 🚀 Upcoming

- ML Pipeline
- XGBoost
- LightGBM
- Random Forest
- LSTM
- Transformer
- Streamlit Dashboard
- FastAPI
- Docker
- CI/CD

---

# 🤝 Contributing

Pull requests are welcome.

For major changes, please open an issue first.

---

# 📄 License

MIT License

---

# 👨‍💻 Author

**Aamir**

Data Science & AI Student

---

⭐ If you found this project useful, don't forget to star the repository.