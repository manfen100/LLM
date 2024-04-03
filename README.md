# LLM Python API library

 
The LLM Python library provides convenient access to the OpenAI Gemini Kimi REST API from any Python 3.7+
application. The library includes type definitions for all request params and response fields,
 
## Installation

```sh
# install for openai
pip install openai
```

```sh
# install for gemini
pip install -q -U google-generativeai
```


```sh
# install for kimi
pip install kimi
```
pip install --upgrade 'openai>=1.0'
## Usage


```python
import os
from openai import OpenAI

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Say this is a test",
        }
    ],
    model="gpt-3.5-turbo",
)
```

```python
from openai import OpenAI
 
client = OpenAI(
    api_key="MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1",
)
 
completion = client.chat.completions.create(
  model="moonshot-v1-8k",
  messages=[
    {"role": "system", "content": "你是 Kimi，由 Moonshot AI 提供的人工智能助手，你更擅长中文和英文的对话。你会为用户提供安全，有帮助，准确的回答。同时，你会拒绝一切涉及恐怖主义，种族歧视，黄色暴力等问题的回答。Moonshot AI 为专有名词，不可翻译成其他语言。"},
    {"role": "user", "content": "你好，我叫李雷，1+1等于多少？"}
  ],
  temperature=0.3,
)
 
print(completion.choices[0].message)
```

```python
chat = chat_model.start_chat(
    # Optional parameters, such ase top_p, top_k, temperature, max_output_tokens,
    # aren't specified in this example
    context="My name is Ned. You are my personal assistant. My favorite movies are Lord of the Rings and Hobbit.",
    examples=[
        InputOutputTextPair(
            input_text="Who do you work for?",
            output_text="I work for Ned.",
        ),
        InputOutputTextPair(
            input_text="What do I like?",
            output_text="Ned likes watching movies.",
        ),
    ],
)

print(chat.send_message("Are my favorite movies based on a book series?"))
```

While you can provide an `api_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `OPENAI_API_KEY="My API Key"` to your `.env` file
so that your API Key is not stored in source control.


## Requirements

Python 3.7 or higher.
