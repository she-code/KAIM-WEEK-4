
import pandas as pd

import re
import pandas as pd
from nltk.tokenize import word_tokenize
import emoji
import unicodedata
from nltk import download
download('punkt')  # Download tokenizer data
import os

def clean_and_structure_telegram_data(df):
    """
    Load, clean, and structure Telegram data into metadata and message components.

    Parameters:
        filepath (str): Path to the CSV or Excel file.

    Returns:
        tuple: (metadata_df, messages_df)
    """
  
    # Drop duplicates
    df.drop_duplicates(inplace=True)

    # Drop rows with missing Message or Date
    df.dropna(subset=["Date","Message","Media Path"], inplace=True)

    # Convert Date column to datetime
    df["Date"] = pd.to_datetime(df["Date"], errors='coerce')

    # Remove rows where Date conversion failed
    df.dropna(subset=["Date"], inplace=True)
    # Reset index
    df.reset_index(drop=True, inplace=True)

    # Split into metadata and message
    metadata_cols = ['Channel Title', 'Channel Username', 'ID', 'Date', 'Media Path']
    metadata_df = df[metadata_cols].copy()
    messages_df = df[['Message']].copy()

    return metadata_df, messages_df



def preprocess_amharic_text(text):
    """
    Comprehensive Amharic text preprocessing
    """
    if not isinstance(text, str):
        return ""
    
    # Normalization
    text = unicodedata.normalize('NFC', text)  # Normalize character encoding
    
    # Remove unwanted elements
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # URLs
    text = re.sub(r'@\w+|#\w+', '', text)  # Mentions and hashtags
    text = re.sub(r'[^\w\s\u1200-\u137F.,!?]', ' ', text)  # Keep Amharic + basic punctuation
    
    # Handle emojis and special symbols
    text = emoji.demojize(text, delimiters=(" ", " "))
    
    # Normalize whitespace
    text = ' '.join(text.split())
    
    return text

def clean_data(df):
    """
    Processes raw DataFrame into structured format
    """
    # Create clean copy
    processed_df = df.copy()

    # Drop duplicates
    processed_df.drop_duplicates(inplace=True)

    # Drop rows with missing Message or Date
    processed_df.dropna(subset=["Message", "Date","Media Path"], inplace=True)

    # Convert Date column to datetime
    processed_df["Date"] = pd.to_datetime(processed_df["Date"], errors='coerce')

    # Remove rows where Date conversion failed
    processed_df.dropna(subset=["Date"], inplace=True)

    # Reset index
    processed_df.reset_index(drop=True, inplace=True)
    
    return processed_df

