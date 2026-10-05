from google import genai
import os
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

chat = client.chats.create(model='gemini-flash-lite-latest')


while True:
    message = input('> ')
    if message == 'exit':
        break
    res = chat.send_message(message)
    print(res.text)