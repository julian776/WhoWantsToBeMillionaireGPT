
from questions.question import Question
import json
import os
from openai import OpenAI

api_key = os.environ.get("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

class QuestionsRepository:
    def __init__(self) -> None:
        pass
    
    def get_questionLLM(self) -> Question:
        """
        load_questionLLM get one
        question requesting one AI LLM
        """
        
        prompt = """Give me a random question. Just answer me a JSON with what I just explained to you. Don't greet me, don't thank me, don't say anything extra. Answer in Spanish.
Example: {
  "question": "What is the capital of France?",
  "answer": "b",
  "options": {
    "a": "London",
    "b": "Paris",
    "c": "Berlin",
    "d": "Madrid"
  }
}"""  
        completion = client.chat.completions.create(
          model="gpt-3.5-turbo",
          messages=[
            {
              "role": "user",
             	"content": prompt
            },
            ],
          )
        questionText = completion.choices[0].message.content

        x = json.loads(questionText)
        return Question(
            x["question"], 
            x["answer"],
            x["options"],
            )