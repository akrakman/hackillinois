from textblob import TextBlob

class ScaleUtilities:
    average = 0
    number = 0
    def get_sentiment_of(string):
        
        return TextBlob(string).sentiment.polarity * 5

    def get_subjectivity_of(string):
        polarity = TextBlob(string).sentiment.polarity * 5
        number += 1
        average += polarity
        return polarity

    def get_subjectivity_of(string):
        subjectivity = TextBlob(string).sentiment.subjectivity * 5
        return
