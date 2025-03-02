import nltk 
from nltk.chat.util import Chat, reflections

nltk.download('punkt')


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot created by you. You can call me ChatBot.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm great, thanks for asking!",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no worries.", "No problem, don't worry about it.",]
    ],
    [
        r"quit",
        ["Bye-bye! Take care.", "It was nice talking to you. Goodbye!",]
    ],
    [
        r"(.*) (good|great|fine|well)",
        ["That's good to hear!", "Awesome!",]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi!",]
    ],
    [
        r"(.*) (age|old) ?",
        ["I'm just a program, so I don't have an age.",]
    ],
    [
        r"what (.*) want ?",
        ["I'm here to assist you with any questions or tasks you have.",]
    ],
    [
        r"(.*) created you ?",
        ["I was created by you using Python and NLTK.",]
    ],
    [
        r"(.*) (location|city) ?",
        ["I exist in the digital world, so I don't have a physical location.",]
    ],
    [
        r"how (.*) health (.*)",
        ["I'm just a program, so I don't have health, but thanks for asking!",]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not connected to the internet, so I can't check the weather for you.",]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that.", "Could you please rephrase that?",]
    ]
]


chatbot = Chat(pairs, reflections)


print("Hi, I'm ChatBot. How can I assist you today?")
while True:
    user_input = input("> ")
    if user_input.lower() == "quit":
        print("ChatBot: Bye-bye! Take care.")
        break
    response = chatbot.respond(user_input)
    print("ChatBot:", response)
