# 📦 Amharic E-commerce Data Extractor for EthioMart

## 📌 Project Overview

This project aims to transform messy Telegram posts from Ethiopian e-commerce channels into a smart FinTech engine that identifies top vendors suitable for loans. EthioMart wants to centralize fragmented Telegram e-commerce data into one unified platform by extracting structured business entities such as product names, prices, and locations from unstructured Amharic text, images, and documents.

---


## 🔑 Key Objectives

- Develop a repeatable pipeline: data ingestion → preprocessing → labeling → structured data output.
- Fine-tune transformer-based models (e.g., XLM-Roberta, mBERT) for Amharic Named Entity Recognition (NER) to extract Product, Price, and Location entities with high accuracy (F1-score).
- Compare multiple NER approaches and interpret model predictions using SHAP and LIME.
- Deliver actionable recommendations on the best model aligned to EthioMart’s business needs.

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

### ✅ Task 2: Label a Subset of Dataset in CoNLL Format
Manually labeled a subset of tokenized Amharic e-commerce messages using the CoNLL format for NER training

Used a dropdown-based Jupyter interface to assign entity tags like B-Product, I-PRICE, and B-LOC per token

Ensured proper structure by separating each message with a blank line and storing labeled tokens in plain text

Created a high-quality, human-annotated dataset to fine-tune transformer-based Amharic NER models


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
