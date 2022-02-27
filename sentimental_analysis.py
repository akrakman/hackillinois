from numpy import average, number
from textblob import TextBlob

class ScaleUtilities:
    average = 0
    number = 0

    def __init__(self, string, number):
        self.string = string

    def get_subjectivity_of(string):
        polarity = TextBlob(string).sentiment.polarity * 5
        number += 1
        average += polarity
        return polarity

    def average_opinion():
        if (number == 0):
            print("You idiot")
            exit(1)
        return average / number
