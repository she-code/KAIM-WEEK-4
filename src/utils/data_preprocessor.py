import re
import pandas as pd
from nltk.tokenize import word_tokenize
import emoji

import unicodedata
from nltk import download
download('punkt')  # Download tokenizer data

def preprocess_amharic_text(text):
    """
    Comprehensive Amharic text preprocessing
    """
    if not isinstance(text, str):
        return ""
    
    # Normalization
    text = unicodedata.normalize('NFC', text)  # Normalize character encoding
    text = text.lower()  # Convert to lowercase
    
    # Remove unwanted elements
    text = re.sub(r'http\S+|www\S+|https\S+', '', text)  # URLs
    text = re.sub(r'@\w+|#\w+', '', text)  # Mentions and hashtags
    text = re.sub(r'[^\w\s\u1200-\u137F]', ' ', text)  # Keep Amharic chars + basic punctuation
    
    # Handle emojis and special symbols
    text = emoji.demojize(text, delimiters=(" ", " "))
    
    # Normalize whitespace
    text = ' '.join(text.split())
    
    return text

def tokenize_amharic(text):
    """Custom tokenizer for Amharic text"""
    # First do word tokenization
    tokens = word_tokenize(text)
    
    # Handle common Amharic constructs
    processed_tokens = []
    for token in tokens:
        # Split attached postpositions
        if token.endswith(('ን', 'ም', 'ህ', 'ሽ', 'ው', 'ዎ', 'ዋ', 'አችሁ')):
            stem = token[:-1]
            postpos = token[-1]
            if stem:
                processed_tokens.append(stem)
            processed_tokens.append(postpos)
        else:
            processed_tokens.append(token)
    
    return processed_tokens