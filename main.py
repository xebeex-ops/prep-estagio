from google import genai
import os
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

response = client.models.generate_content_stream(
    model = 'gemini-flash-lite-latest',
    contents = 'Como as celulas fazem energia'


)

for stream in response:
    print(stream.text)