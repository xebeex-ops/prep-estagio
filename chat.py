import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv("Gemini_API_KEY"))

config = types.GenerateContentConfig(
    system_instruction="Es um assistente senior de DevOps. responde de forma concisa e tecnica",
    temperature=0.3,
)

chat = client.chats.create(
    model='gemini-3.5-flash-lite',
    config=config,
)

resposta_1 = chat.send_message('Ola, tenho uma base de dados PostgreSQL que esta a consumir toda a memoria RAM')

print(f'Assistente:\n{resposta_1.text}\n')
print('*' * 50)

historico = chat.get_history()
print(f'Total de turnos guardados: {len(historico)}')
for msg in historico:
    print(f'Papel: {msg.role}')