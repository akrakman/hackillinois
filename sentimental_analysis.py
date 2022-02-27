from textblob import TextBlob

class ScaleUtilities:

    def get_sentiment_of(string):
        
        return TextBlob(string).sentiment.polarity * 5

    def get_subjectivity_of(string):
        return TextBlob(string).sentiment.subjectivity * 5