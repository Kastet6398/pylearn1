from transformers import Conversation, pipeline
conversation = Conversation([
    {'role': 'user', 'content': 'Hello!'},
    {'role': 'assistant', 'content': 'Hi there! How can I assist you today?'}
])
chat_pipeline = pipeline('text-generation')
user_input = "What's the weather like today?"
conversation.add_user_input(user_input)

assistant_response = chat_pipeline(conversation)
print(assistant_response)

