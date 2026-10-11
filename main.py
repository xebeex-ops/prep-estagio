import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
from pydantic import BaseModel, Field

load_dotenv()

class AnaliseIncidente(BaseModel):
    servico: str = Field(description='Nome do servico afetado')
    gravidade: str = Field(description = 'Nivel: Baixo, Medio, Alto, Critico')
    cpu_percent: float = Field(description = 'Percentagem de CPU registada')
    memoria_mb: int = Field(description = 'Consumo de memoria em MB')
    diagnostico: str = Field(description = 'Causa tecnica do problema')

client = genai.Client(api_key=os.getenv('GEMINI_API_KEY')) #chamar api

config = types.GenerateContentConfig(  
    temperature = 0.1,  #mais rigor
    response_mime_type='application/json',
    response_schema=AnaliseIncidente #Passa a classe Pydabtic como contrato
)

log_bruto = """
[2026-10-11 16:05:22] CRITICAL cluster-auth-service: Out of memory killer invoked.
CPU consumption reached 96.8% during token verification process. 
Memory usage peaked at 8192MB before the container crashed.
"""

prompt = f"Analisa este log de servidor e extrai a informação necessária:\n{log_bruto}"

response = client.models.generate_content(
    model='gemini-3.8-flash',
    contents=prompt,
    config=config,
)

print("Texto bruto devolvido pela Google:")
print(response.text)