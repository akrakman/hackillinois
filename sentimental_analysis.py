def get_sentiment_of(string):
    return TextBlob(string).sentiment.polarity

def get_subjectivity_of(string):
    return TextBlob(string).sentiment.subjectivity
