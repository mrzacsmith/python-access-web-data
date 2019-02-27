import random

responses = {
    "what's your name?" : [
      "my name is Echobot",
      "they call be Mr. Echobot",
      "the names Bot, Echobot"
      ]

    # "what's the weather today?" : "it's {} today"
}

weather_today = "cloudy"

def respond(message):
    if message in responses:
        print(random.choice(responses[message]))

# respond("what's the weather today?")
respond("what's your name?")
