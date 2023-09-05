
from questions.question import Question
import os
import openai
import json

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")

class QuestionsRepository:
    def __init__(self) -> None:
        pass
    
    def get_questionChatGPT(self) -> Question:
        """
        load_questionChatGPT get one
        question requesting one AI LLM
        """
        
        propmt = """Vas a ser el presentador de ¿Quién cree ser millonario? Dame una pregunta aleatoria con la respuesta, cuatro opciones de respuesta, y la respuesta correcta. Solamente respóndeme un JSON con lo que te acabo de explicar. No me saludes, no me agradezcas, no digas nada extra. Responde en español.
Ejemplo: {
  "question": "¿Cuál es el capital de Francia?",
  "answer": "b",
  "options": {
    "a": "Londres",
    "b": "París",
    "c": "Berlín",
    "d": "Madrid"
  }
}"""
        # messages = [
        #         {"role": "user", "content": prompt }
        #     ]

        # chat_completion = openai.ChatCompletion.create(
        #     model="gpt-3.5-turbo",
        #     messages=messages
        #     )
        
        # x = json.loads(chat_completion["choices"][0]["message"]["content"])

        x = json.loads('{\"question\": \"¿Cuál es el capital de Francia?\",\"answer\": \"b\",\"options\": {\"a\": \"Londres\",\"b\": \"París\",\"c\": \"Berlín\",\"d\": \"Madrid\"}}')
        print("fdhd", x["options"])
        return Question(
            x["question"], 
            x["answer"],
            x["options"],
            )