import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

print('A enviar ficheiro para a Google...')
log_file = client.files.upload(file="servidor.txt") #fazer upload do ficheiro para a Files API

print('Upload concluido com sucesso')
print(f'Nome interno: {log_file.name}')
print(f'MIME type detetado {log_file.mime_type}')
print(f'URI: {log_file.uri}')

response = client.models.generate_content(
    model='gemini-3.5-flash-lite',
    contents=[
        log_file,
        "Analisa estes logs de servidor. Identifica a causa raiz do problema e lista o que falhou de forma cronológica e concisa."
    ],
)

print('Resposta')
print(response.text)

print('\nA eliminar o ficheiro dos servidores da Google...')
client.files.delete(name=log_file.name)
print(f'Ficheiro {log_file.name} eliminado com sucesso')