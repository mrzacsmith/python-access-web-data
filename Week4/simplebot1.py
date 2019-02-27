

responses = {
    "what's your name?" : "my name is Echobot",
    "what's the weather today?" : "it is sunny"
}

def respond(message):
    if message in responses:
        print(responses[message])

respond("what's your name?")