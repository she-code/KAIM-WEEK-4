import re
import pandas as pd
from nltk.tokenize import word_tokenize

from nltk import download
download('punkt')  # Download tokenizer data
import re
import os
import json

# Function to clean and structure Telegram data

# Basic Amharic stopword list (extendable)
amharic_stopwords = set([
    'እንደ', 'ነው', 'ይህ', 'ያም', 'ለማን', 'ናቸው', 'ነበር', 'ስለ', 'እዚህ',
    'እየ', 'ነኝ', 'በሚል', 'አይደለም', 'የሆነ', 'ያለ', 'እንጂ', 'እኔ'
])

# Emoji & symbol regex
emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"  # emoticons
    u"\U0001F300-\U0001F5FF"  # symbols
    u"\U0001F680-\U0001F6FF"  # transport
    u"\U0001F1E0-\U0001F1FF"  # flags
    u"\u2600-\u26FF\u2700-\u27BF"  # miscellaneous
"]+", flags=re.UNICODE)

def normalize_amharic_text(text):
    text = str(text)
    text = emoji_pattern.sub('', text)              # Remove emojis
    text = re.sub(r'[^\w\s፡።፣፤፥፦፧]', '', text)    # Remove punctuation except Amharic delimiters
    text = re.sub(r'\s+', ' ', text).strip()        # Normalize spaces
    return text

def tokenize(text):
    return re.findall(r'\w+', text)

def remove_stopwords(tokens):
    return [word for word in tokens if word not in amharic_stopwords]

def preprocess_amharic_messages(messages_df):
    clean_texts = []
    token_lists = []
    processed_tokens = []

    for msg in messages_df['Message']:
        norm = normalize_amharic_text(msg)         # Normalized string
        tokens = tokenize(norm)                    # Token list
        filtered = remove_stopwords(tokens)        # Stopword removal

        clean_texts.append(norm)
        token_lists.append(tokens)
        processed_tokens.append(filtered)

    # Add each stage as a separate column
    messages_df = messages_df.copy()
    messages_df['Clean_Text'] = clean_texts
    messages_df['Tokens'] = token_lists
    messages_df['Processed'] = processed_tokens

    return messages_df

def process_media_path(path):
    """Extract media type from path"""
    if not isinstance(path, str) or not path:
        return None
    ext = os.path.splitext(path)[1].lower()
    if ext in ['.jpg', '.jpeg', '.png']:
        return 'image'
    elif ext in ['.pdf', '.doc', '.docx']:
        return 'document'
    return 'other'

def extract_metadata(df):
    """
    Extracts and structures metadata
    """
    metadata = pd.DataFrame({
        'message_id': df['ID'],
        'channel_name': df['Channel Title'],
        'channel_username': df['Channel Username'],
        'timestamp': df['Date'],
        'has_media': df['Media Path'].notna(),
        'media_type': df['media_type'],
        'message_length': df['message_length'],
        'word_count': df['word_count'],
        'amharic_ratio': df['amharic_ratio'],
        'hour_of_day': df['Date'].dt.hour,
        'day_of_week': df['Date'].dt.day_name()
    })
    
    return metadata


def store_processed_data(processed_df, metadata, output_dir='../data/processed'):
    """
    Stores processed data in structured format
    """
    os.makedirs(output_dir, exist_ok=True)
    
    # Save processed messages (without metadata columns)
    message_cols = ['ID', 'Clean_Text', 'Tokens','Processed','Message', 'Media Path']
    processed_df[message_cols].to_parquet(f'{output_dir}/messages.parquet')
    
    # Save metadata
    metadata.to_parquet(f'{output_dir}/metadata.parquet')
    
    # Save stats (convert numpy types to native Python types)
    stats = {
        'total_messages': int(len(processed_df)),
        'channels': int(processed_df['Channel Username'].nunique()),
        'with_media': int(processed_df['Media Path'].notna().sum()),
        'date_range': {
            'start': str(processed_df['Date'].min()),
            'end': str(processed_df['Date'].max())
        },
        'avg_message_length': float(processed_df['message_length'].mean()),
        'avg_amharic_ratio': float(processed_df['amharic_ratio'].mean())
    }
    
    with open(f'{output_dir}/stats.json', 'w') as f:
        json.dump(stats, f, indent=2)
    
    print(f"Data successfully stored in {output_dir}")
