# Notebooks

This folder contains Jupyter notebooks illustrating the process of data ingestion, cleaning, and initial exploration of Telegram e-commerce data.

### task1.ipynb
- Connecting to and scraping messages, images, and documents from multiple Ethiopian Telegram channels

- Normalizing Amharic text and handling language-specific punctuation and emojis

- Tokenizing and removing stopwords from messages

- Cleaning the dataset by removing duplicates and handling missing values

- Structuring raw messages with separate metadata columns (sender, timestamp, channel)

- Basic statistical summaries of message counts, media presence, and channel activity

- Initial exploratory data analysis with visualizations on message frequency, text length, and media usage

- Highlighting linguistic features and data quality issues to prepare for NER labeling and modeling

### task2.ipynb

- Loaded a preprocessed and tokenized subset of messages for manual labeling

- Used a Jupyter-based dropdown widget interface for intuitive token-by-token labeling

- Assigned entity tags following the CoNLL format: B-Product, I-Product, B-PRICE, I-PRICE, B-LOC, I-LOC, and O

- Allowed real-time selection of entity labels for each token with visual feedback

- Automatically saved labeled messages to a `.txt` file in CoNLL format after each submission

- Ensured each message was separated by a blank line for proper formatting

- Prepared the dataset for supervised fine-tuning of Amharic NER models using Hugging Face tools

- Enabled reproducibility and consistency by structuring labels in a widely accepted standard (CoNLL)

## task3.ipynb

- Loaded CoNLL-formatted Amharic dataset for training and validation

- Parsed token-label sequences and converted them into Hugging Face datasets format with proper alignment

- Tokenized input text using a pretrained Amharic transformer tokenizer (e.g., AfriBERTa, XLM-R)

- Applied label alignment to ensure correct mapping of entity tags to subword tokens

- Fine-tuned a transformer-based model using Hugging Face's Trainer API with sequence labeling objectives

- Monitored training with validation loss, precision, recall, and F1 score using seqeval metrics

- Evaluated the final model on held-out test data and generated classification reports per entity type

- Saved the best-performing model checkpoint and tokenizer for downstream inference

- Enabled reproducibility through fixed seeds, logged training arguments, and saved evaluation metrics

- Prepared the model for real-world Telegram NER use cases such as product name, price, and location extraction

## convert_to_conll.ipynb

- converts the txt file to .conll file

## task4_model_comparison.ipynb

- Implemented a full model comparison workflow for Amharic Named Entity Recognition using multiple multilingual transformer models

- Parsed CoNLL-formatted datasets containing token–label sequences and structured them into Hugging Face Dataset format

- Fine-tuned and evaluated three transformer models:

    - xlm-roberta-base

    - bert-base-multilingual-cased (mBERT)

    - Davlan/distilbert-base-multilingual-cased-ner-hrl

- Tokenized the Amharic text and aligned NER labels properly across subword tokens for each model

- Used Hugging Face's Trainer API with consistent training arguments across all models (e.g., batch size, epochs, weight decay)

- Evaluated all models on a validation split using the seqeval metric to compute precision, recall, and F1 score

- Logged training time and validation performance for each model to enable reproducible benchmarking

- Identified the best-performing model based on F1 score and evaluation loss for downstream deployment

- Saved the tokenizer and model checkpoint of the top performer for real-world usage in Amharic Telegram e-commerce entity      extraction

## task5.ipynb

- Loaded saved pretrained model 

- Implemented SHAP and LIME interpretability tools to explain model predictions

- Visualized predicted entities with color coding and performed error analysis against ground truth

- Tested models on sample Amharic sentences, revealing poor accuracy and common misclassification patterns (e.g., overuse of I-CONTACT)

- Identified core issues in model learning, such as weak token-feature relationships and data complexity

## ner_data_from_message.ipynb

- Extracts prodct details from message

## task6.ipynb

- Loaded Telegram metadata and NER-extracted product data

- Merged metadata with NER output to create a full vendor dataset

- Calculated key metrics per vendor: Posts/Week, Avg. Views/Post, Avg. Price

- Identified top-performing post per vendor based on views and price

- Designed and applied a custom Lending Score formula

- Generated a comparative Vendor Scorecard table

- Recommended micro-loan amounts based on vendor performance and price levels