import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask(query):
   chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": query,
        }
    ],
    model="llama-3.1-8b-instant",
    )

   print(chat_completion.choices[0].message.content)
