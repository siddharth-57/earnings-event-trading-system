# Earnings-Based Trading Bot

A modular Python trading system that analyzes historical stock price behavior around earnings announcements, generates trade signals, and executes trades using a broker API with basic risk controls.

---

## Overview

This project implements an earnings-based trading strategy for Indian equities.
It analyzes historical price movements around earnings dates, evaluates performance metrics, and places live bracket orders for qualifying trade setups.

The application is structured using industry-standard modular design, separating data ingestion, strategy logic, execution, and configuration.

---

## Features

- Fetches historical stock price and earnings data using yfinance
- Computes earnings-window returns and historical performance statistics
- Generates BUY trade signals based on positive earnings surprises
- Executes live bracket orders via Zerodha Kite Connect API
- Applies basic risk controls with fixed capital allocation per trade
- Saves processed trade data for further analysis

---

## How It Works

1. Fetches historical stock prices and earnings dates
2. Computes earnings-window returns for each stock
3. Filters stocks with consistent positive earnings performance
4. Generates BUY signals on positive earnings surprises
5. Places bracket orders with predefined target and stop-loss
6. Stores trade data for performance evaluation

---

## Tech Stack

- Python
- pandas
- yfinance
- Zerodha Kite Connect API

---

## How to Run

1. Install dependencies:
   pip install -r requirements.txt
2. Add your API credentials in config.py
3. Run the application:
   python src/main.py

---

## Disclaimer

This project is for educational purposes only.
Live trading involves financial risk.

---

## Future Improvements

- Paper trading mode
- Improved risk management and position sizing
- Logging and monitoring
- Support for additional strategies and markets
