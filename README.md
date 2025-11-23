## 📈 US Markets EDA 📊
**Exploratory Data Analysis (EDA) on US Markets**

This repository contains Jupyter notebooks and Python scripts for analyzing key US market indicators, including:
- **US Indexes** (S&P 500, Nasdaq, Dow Jones)
- **Interest Rates** (Federal Funds Rate, Treasury Yields)
- **Jobs & Unemployment** (Non-Farm Payrolls, Unemployment Rate)
- **CPI/PCE & Inflation**
- **Macroeconomic Trends**

---

## Repository Structure

## Repository Structure (Table Format)

| Path                          | Description                                   |
|------------------------------|-----------------------------------------------|
| `us-markets-eda/`            | Project root directory                        |
| ├── `data/`                  | Raw and processed datasets                    |
| │   ├── `sp500_2025.csv`     | S&P 500 dataset                               |
| │   ├── `interest_rates.csv` | Interest rate history                         |
| │   └── `...`                | Additional dataset files                      |
| ├── `notebooks/`             | Jupyter notebooks for EDA                     |
| │   ├── `sp500_analysis.ipynb` | S&P 500 exploratory analysis               |
| │   ├── `inflation_trends.ipynb` | Inflation time-series analysis           |
| │   └── `...`                | Other notebooks                               |
| ├── `scripts/`               | Python scripts for data processing            |
| │   ├── `data_cleaning.py`   | Data transformation and preprocessing         |
| │   └── `...`                | Other automation or utility scripts           |
| ├── `README.md`              | Project overview and documentation            |
| └── `requirements.txt`       | Python dependency list                        |

---

## Getting Started
### Prerequisites
- Python 3.8+
- Jupyter Notebook/Lab
- Required libraries (install via `pip install -r requirements.txt`):
- pandas
- numpy
- matplotlib
- seaborn
- yfinance

### Installation
1. Clone the repository:
 ```bash
 git clone https://github.com/your-username/us-markets-eda.git
```

### Navigate to the project directory:


```
cd us-markets-eda
```

### Install dependencies:

```
pip install -r requirements.txt
```

>Alpha Vantage (Free API):
Sign up for a free API key and fetch S&P 500 data.

### Usage

Place your datasets in the data/ directory.
Open a Jupyter notebook (e.g., sp500_analysis.ipynb) and run the cells to perform EDA.
Use the scripts/ directory for reusable Python functions.

### Contributing
Contributions are welcome! Open an issue or submit a pull request for:

New datasets
Improved visualizations
Bug fixes

License
This project is licensed under the MIT License.
