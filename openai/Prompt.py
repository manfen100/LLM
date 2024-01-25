from openai import OpenAI
client =OpenAI(
    
)

response = client.completions.create(
    model ="text-davinci-003",
    prompt="Say this is a test",
)