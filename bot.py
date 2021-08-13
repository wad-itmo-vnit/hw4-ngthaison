# Import necessary 
import datetime
import random

# Answer based on predefined rules
def get_ans(req):
    req = req.lower()

    if 'hi' in req or 'hello' in req:
        return "Hello!"
    elif 'time' in req:
        now = datetime.datetime.now()
        return "It's %s:%s" % (now.hour, now.minute)
    elif 'date' in req:
        now = datetime.datetime.now()
        return "Today's %s/%s" % (now.day, now.month)
    elif 'how' in req and 'you' in req:
        return "I'm fine!"
    elif 'weather' in req:
        return "It's such a great sunny day!"
    elif 'temperature' in req:
        return "It's about 23 degrees."
    else:
        return "It's a pleasure to meet you!"

# List of arbitrary sentences
sentences = ["Can I help you?",
            "Good to see you!",
            "Ask me anything.",
            "Hello!"
            ]

# Get random sentence
def random_chat():
    return random.choice(sentences)