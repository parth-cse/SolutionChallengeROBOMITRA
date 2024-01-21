from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a chatbot instance
chatbot = ChatBot(
    'Happiness Delivery Bot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch'
    ],
    input_adapter='chatterbot.input.TerminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database_uri='sqlite:///database.db'
)

# Train the chatbot with AIML data
trainer = ListTrainer(chatbot)
trainer.train([
    'Hello! How can I help you today?',
    'I am here to spread happiness and assist you in any way I can.',
    'I can answer questions, provide information, and even engage in friendly conversation.',
    'Feel free to ask me anything!',
    # Add more AIML patterns and responses here
])

# Continuously engage in conversation
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot:", response)
