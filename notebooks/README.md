# Notebooks

This folder contains Jupyter notebooks illustrating the process of data ingestion, cleaning, and initial exploration of Telegram e-commerce data.

### task1.py
- Connecting to and scraping messages, images, and documents from multiple Ethiopian Telegram channels

- Normalizing Amharic text and handling language-specific punctuation and emojis

- Tokenizing and removing stopwords from messages

- Cleaning the dataset by removing duplicates and handling missing values

- Structuring raw messages with separate metadata columns (sender, timestamp, channel)

- Basic statistical summaries of message counts, media presence, and channel activity

- Initial exploratory data analysis with visualizations on message frequency, text length, and media usage

- Highlighting linguistic features and data quality issues to prepare for NER labeling and modeling

### task2.py
# task_2_ner_labeling_conll.py

- Loaded a preprocessed and tokenized subset of messages for manual labeling

- Used a Jupyter-based dropdown widget interface for intuitive token-by-token labeling

- Assigned entity tags following the CoNLL format: B-Product, I-Product, B-PRICE, I-PRICE, B-LOC, I-LOC, and O

- Allowed real-time selection of entity labels for each token with visual feedback

- Automatically saved labeled messages to a `.txt` file in CoNLL format after each submission

- Ensured each message was separated by a blank line for proper formatting

- Prepared the dataset for supervised fine-tuning of Amharic NER models using Hugging Face tools

- Enabled reproducibility and consistency by structuring labels in a widely accepted standard (CoNLL)

