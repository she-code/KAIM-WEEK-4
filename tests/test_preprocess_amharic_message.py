import pandas as pd
import pytest
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from utils.data_preprocessor import preprocess_amharic_messages

# Assuming the functions below are imported or defined in the same test file:
# - preprocess_amharic_messages
# - normalize_amharic_text
# - tokenize
# - remove_stopwords

def test_preprocess_amharic_messages():
    # Sample input data
    data = {
        'Message': [
            "ሰላም ልዑል! 😊 እንደምን ነህ?",
            "ይህ ሙከራ ጽሑፍ ነው። 150 ብር ዋጋ አለው።"
        ]
    }
    df = pd.DataFrame(data)
    
    # Run preprocessing
    processed_df = preprocess_amharic_messages(df)
    
    # Check that new columns exist
    assert 'Clean_Text' in processed_df.columns
    assert 'Tokens' in processed_df.columns
    assert 'Processed' in processed_df.columns
    
    # Check Clean_Text is a string without emojis or unwanted punctuation
    for original, clean in zip(df['Message'], processed_df['Clean_Text']):
        assert isinstance(clean, str)
        assert '😊' not in clean  # Emoji removed
    
    # Check Tokens column contains list of strings
    for tokens in processed_df['Tokens']:
        assert isinstance(tokens, list)
        assert all(isinstance(t, str) for t in tokens)
    
    # Check Processed column tokens have stopwords removed
    # Example: If stopwords are known, check none present in processed tokens
    # Here you might want to test that processed tokens list is a subset of tokens list
    for tokens, processed in zip(processed_df['Tokens'], processed_df['Processed']):
        assert set(processed).issubset(set(tokens))
        # Additionally, processed tokens should be fewer or equal in count
        assert len(processed) <= len(tokens)
