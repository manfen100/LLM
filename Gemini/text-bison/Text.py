from vertexai.language_models import ChatModel, InputOutputTextPair

chat_model = ChatModel.from_pretrained("chat-bison@002")

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