import os
from pathlib import Path

from energia import recomendacoes
from dotenv import load_dotenv
from google import genai
from google.genai import types

BASE_DIR = Path(__file__).resolve().parent.parent


load_dotenv(BASE_DIR / ".env")

API_KEY = os.getenv("CHAVE_GEMINI")
MODELO = "gemini-3.1-flash-lite"


def linha(texto:str)->str:
    print("-"*100)
    pergunta = input(texto)
    print("-"*100)
    return pergunta.strip()


def carregar_prompt():
    caminho_prompt = BASE_DIR / "data" / "system_prompt.txt"

    if not caminho_prompt.exists():
        raise FileNotFoundError("Arquivo system_prompt não encontrado.")

    return caminho_prompt.read_text(encoding="utf-8")


def criar_cliente():
    if not API_KEY:
        raise ValueError("CHAVE_GEMINI não foi configurada no .env")
    return genai.Client(api_key=API_KEY)


def criar_chat(cliente):
    configuracao = types.GenerateContentConfig(
        system_instruction=carregar_prompt(),
        tools=[
            recomendacoes.analisar_residencia,
            recomendacoes.simular_reducao_banho
        ],
        automatic_function_calling=(
            types.AutomaticFunctionCallingConfig(
                maximum_remote_calls=3
            )
        ),
        max_output_tokens=4096
    )
    
    return cliente.chats.create(
        model=MODELO,
        config=configuracao
    )


def enviar_mensagem(chat, mensagem):
    resposta = chat.send_message(mensagem)

    return resposta.text or "Não foi possível gerar uma resposta."
