from google import genai
import os
from google.genai import types
from dotenv import load_dotenv
load_dotenv()
client = genai.Client(api_key=os.getenv('GEMINI_API_KEY'))

config = types.GenerateContentConfig(
    temperature =0.1,
    max_output_tokens=300,
    system_instruction=(
        "És um arquiteto de software sénior focado em backend. "
        "Responde sempre de forma estritamente técnica, em tópicos diretos e sem saudações."
    ),

)

prompt = "Sugere 3 nomes para um serviço de backend que processa pedidos de IA em lote."

response = client.models.generate_content(
    model = 'gemini-flash-lite-latest',
    contents =prompt,
    config=config,


)

print(response.text)
print("-" * 30)
print(f"Finish Reason: {response.candidates[0].finish_reason}")