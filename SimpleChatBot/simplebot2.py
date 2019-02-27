import random

name = 'Fred'
weather = 'sunny'

responses = {
    "what's your name?" : "my name is {0}".format(name),
    "what's the weather today?" : "the weather today is {0}".format(weather),
    "default" : "default message"
}

def respond(message):
    if message in responses:
        bot_message = print(responses[message])
    else:
        bot_message = print(responses["default"])

respond( "what's your name?")