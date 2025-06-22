# 🚗 ACIS Insurance Claims Analysis

This project performs an end-to-end analysis of car insurance data from **AlphaCare Insurance Solutions (ACIS)**, covering the period from February 2014 to August 2015. The goal is to uncover insights, evaluate risk and pricing fairness, and build predictive models to support dynamic, risk-based pricing.

---

## Project Objectives

- Perform **exploratory data analysis (EDA)** to identify trends, anomalies, and key business insights.
- Set up a **reproducible and auditable data pipeline** using DVC.
- Conduct **A/B testing** to evaluate risk and margin differences across customer segments.
- Build and evaluate **predictive models** for:
  - Claim **severity** (for customers who made claims)
  - Claim **frequency** (likelihood of a customer making a claim)

---


## Project Structure
---
```
KAIM-WEEK-3/
├── .github/
│ └── workflows/ # GitHub Actions workflows
├── data/
│ ├── raw/ # Raw data (should never be modified)
│ └── processed/ # Processed/cleaned data (gitignored)
├── notebooks/
│ ├── task1.ipynb # data scraping, cleaning and processing
│ └── README.md # Documentation for notebooks
├── scripts/
│ └── README.md # Documentation for scripts
├── src/
│ └── utils/ # Utility functions
    │ ├── data_loader.py # Data loading utilities
    │ ├── data_cleaning.py # Data cleaning utilities
    │ ├── data_preprocessor.py # Data preprocessing utilities
│ └── README.md # Documentation for source code
├── tests/
│ └── README.md # Testing documentation
├── .gitattributes
├── .gitignore
├── README.md # Main project documentation
└── requirements.txt # Python dependencies
```
---

## ⚙️ Tech Stack

**Languages & Libraries:**  
Python

**Data Management & Reproducibility:**  
Git, GitHub

**Data Manipulation & File Handling:**
os, json, csv, pandas

**Text Processing & NLP:**
re, nltk (word_tokenize, download), emoji, unicodedata

**Environment & Configuration:**
dotenv (load_dotenv)

**Telegram API Client:**
telethon (TelegramClient)

---

## Key Tasks Completed

### ✅ Task 1: Data Ingestion & Preprocessing
Connected to multiple Ethiopian Telegram e-commerce channels and collected real-time messages, images, and documents

Normalized and tokenized Amharic text, handling language-specific features and removing noise

Structured raw data by separating message content from metadata such as sender and timestamps

Cleaned and formatted datasets to prepare for entity extraction and downstream modeling
---

---
## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/she-code/KAIM-WEEK-4.git
cd KAIM-WEEK-4
```

2. **Create and activate a virtual environment:**

```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
3. **Install dependencies:**

```bash
pip install -r requirements.txt

```

## Contributors
- Frehiwot Abebie
