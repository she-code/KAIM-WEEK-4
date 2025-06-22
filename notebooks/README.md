# Notebooks

This folder contains Jupyter notebooks illustrating the process of data ingestion, cleaning, and initial exploration of Telegram e-commerce data.

### task_1_data_ingestion_preprocessing.py
- Connecting to and scraping messages, images, and documents from multiple Ethiopian Telegram channels

- Normalizing Amharic text and handling language-specific punctuation and emojis

- Tokenizing and removing stopwords from messages

- Cleaning the dataset by removing duplicates and handling missing values

- Structuring raw messages with separate metadata columns (sender, timestamp, channel)

- Basic statistical summaries of message counts, media presence, and channel activity

- Initial exploratory data analysis with visualizations on message frequency, text length, and media usage

- Highlighting linguistic features and data quality issues to prepare for NER labeling and modeling