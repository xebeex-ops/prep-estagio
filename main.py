from google import genai
import os
from google.genai import types
from dotenv import load_dotenv
import time
load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

config = types.GenerateContentConfig(
    temperature =0.2,
    max_output_tokens=300,
    system_instruction=(
        "És um arquiteto de software sénior focado em backend. "
        "Responde sempre de forma estritamente técnica, em tópicos diretos e sem saudações."
    ),

)

prompt = "Sugere 3 nomes para um serviço de backend que processa pedidos de IA em lote."

response = client.models.generate_content_stream(
    model = 'gemini-flash-lite-latest',
    contents =prompt,
    config=config,


)
ttft = None
start_time = time.time()

for chunk in response:
    if ttft is None:
        ttft = time.time() - start_time
    print(chunk.text, end='', flush=True)
    
total_time = time.time() - start_time

print("\n" + "=" * 50)
print(f"Time to First Token (TTFT) : {ttft:.3f} segundos")
print(f"Tempo Total de Resposta    : {total_time:.3f} segundos")