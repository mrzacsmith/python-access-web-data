

responses = {
    "what's your name?" : "my name is Echobot",
    "what's the weather today?" : "it's {} today"
}

weather_today = "cloudy"

def respond(message):
    if message in responses:
        print(responses[message].format(weather_today))

respond("what's the weather today?")
respond("what's your name?")