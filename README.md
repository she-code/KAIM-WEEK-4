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
├── model # contains models
│ ├── fine_tuned_amharic_ner_mofel/ #ner model
├── notebooks/
│ ├── task1.ipynb # data scraping, cleaning and processing
│ ├── task2.ipynb # conll data extracted
│ ├── task3.ipynb # fine tune ner model
│ ├── task4_model_comparison.ipynb model comparison
│ ├── task5.ipynb # model interpretability
│ ├── task6.ipynb # vendor scorecard
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

### ✅ Task 3: Fine-Tune Amharic NER Model
Fine-tuned a transformer model (e.g., AfriBERTa) on the labeled CoNLL-format dataset using Hugging Face tools

Aligned token-label pairs for subword tokens and trained with Trainer API

Evaluated performance using precision, recall, and F1 metrics via seqeval

Saved the best model and tokenizer for downstream NER tasks on Amharic Telegram data

### ✅ Task 4: Compare & Select Best NER Model
Converted .txt file to .conll file

Compared multiple multilingual transformer models (XLM-R, DistilBERT, mBERT) for Amharic NER using the same labeled dataset

Aligned tokens and labels, fine-tuned each model with consistent settings using Hugging Face’s Trainer API

Evaluated performance using seqeval metrics (F1, precision, recall, accuracy)

Selected xlm-roberta-base as the best model based on F1 score and saved its configuration for production use

### ✅ Task 5:  Model Interpretability

Loaded saved pretrained model 

Implemented SHAP and LIME interpretability tools to explain model predictions

Visualized predicted entities with color coding and performed error analysis against ground truth

Tested models on sample Amharic sentences, revealing poor accuracy and common misclassification patterns (e.g., overuse of I-CONTACT)

Identified core issues in model learning, such as weak token-feature relationships and data complexity

✅ Task 6: Vendor Scorecard for Micro-Lending

Created NER dataset by extracting product-related entities (product_category, price, location, contact_info) from the messages column

Loaded Telegram metadata and NER-extracted product data

Merged metadata with extracted entities to build a vendor-level dataset

Calculated vendor metrics: posting frequency, average views per post, and average product price

Identified each vendor's top-performing post based on views and price

Designed a custom Lending Score to rank vendors by business activity and engagement

Generated a Vendor Scorecard comparing all vendors across key metrics

Recommended micro-loan amounts based on vendor score and pricing strategy

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
