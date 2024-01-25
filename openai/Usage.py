import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(".env")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
client = OpenAI(
    api_key= os.environ.get(OPENAI_API_KEY),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role":"user",
            "content":"Say this is a test",
        }
    ],
    model ="gpt-3.5-turbo",
  
    # json format
    response_format={"type":"json_object"}
)
print(chat_completion.choices[0].message)


