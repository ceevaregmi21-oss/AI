from textblob import TextBlob
import colorama
from colorama import Fore
colorama.init()

positive_count = 0
negative_count = 0
neutral_count = 0

print("Sentiment Chatbot - type 'exit' to quit")

while True:
    text = input('Please enter your text here: ')

    if text == 'exit':
        print(Fore.WHITE, "Positive:", positive_count, "Negative:", negative_count, "Neutral:", neutral_count)
        break

    a = TextBlob(text)
    b = a.sentiment.polarity

    if (b > 0):
        print(Fore.GREEN, "sentence is positive", b)
        positive_count = positive_count + 1
    elif (b < 0):
        print(Fore.RED, "sentence is negative", b)
        negative_count = negative_count + 1
    else:
        print(Fore.YELLOW, "sentence is neutral", b)
        neutral_count = neutral_count + 1