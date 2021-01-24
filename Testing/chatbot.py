'''
There are 2 basic tyoes of chatbots

Rule-Based: a bot is progrmammed according to logical rules
 - answers simple questions, the ability to answer complex queries
 contingent on the set of rules programmed
 - Example:
    - nltk.chat.util: utility available in NLTK (Natural Language Tool Kit)
    for simple chatbot w/o ML
      https://www.kdnuggets.com/2019/05/build-chatbot-python-nltk.html

    - Simple chatbot using google search for user queries and webscraping
    to return web results:
      https://towardsdatascience.com/build-a-simple-chatbot-with-python-and-google-search-c000aa3f73f0

Self-Learning: programed using ML, particularly NLP
 - more efficient vs rule-based, can handle more complex queries
 - Some Python Libraries: chatterbot: https://pypi.org/project/ChatterBot/
 - A DL example:
     https://towardsdatascience.com/how-to-create-a-chatbot-with-python-deep-learning-in-less-than-an-hour-56a063bdfc44
'''

# import libraries
import time
import random


sec = 0.5

name = input("Hi, what is your name? ")
time.sleep(sec)
print("Hi " + name)

feeling = input("How are you today? ")
if "good" in feeling.lower():
    print("I'm feeling good too!")
elif "awesome" in feeling.lower():
    print("I'm feeling awesome too!")
else:
    print("I'm sorry to hear that!")

time.sleep(sec)

favfood = input("What's your favorite food? ")
foods = ["Italian", "Thai", "Ethiopian", "Mexican"]

time.sleep(sec)
print("My favorite food is " + random.choice(foods))
