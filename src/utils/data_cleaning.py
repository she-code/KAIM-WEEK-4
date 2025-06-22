def clean_and_structure_data(df):
    """
    Processes raw DataFrame into structured format
    """
    # Select and rename columns
    processed_df = df[['timestamp', 'sender', 'message']].copy()
    processed_df.columns = ['timestamp', 'sender', 'raw_message']
    
    # Convert timestamp to datetime
    processed_df['timestamp'] = pd.to_datetime(processed_df['timestamp'])
    
    # Text preprocessing
    processed_df['clean_text'] = processed_df['raw_message'].apply(preprocess_amharic_text)
    
    # Tokenization
    processed_df['tokens'] = processed_df['clean_text'].apply(tokenize_amharic)
    
    # Extract message length features
    processed_df['message_length'] = processed_df['clean_text'].apply(len)
    processed_df['word_count'] = processed_df['tokens'].apply(len)
    
    # Detect language (simple Amharic character ratio)
    processed_df['amharic_ratio'] = processed_df['clean_text'].apply(
        lambda x: len(re.findall(r'[\u1200-\u137F]', x)) / len(x) if len(x) > 0 else 0
    )
    
    return processed_df