from openai import OpenAI # Import the OpenAI client

# Set your API key during the instantiation of the OpenAI client
client = OpenAI(api_key='YOUR API KEY') # Replace with your API key
## I recommend storing your API key in a separate file and importing it here or use environment variables
## Dont ever store your API key in a public repository

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a very skilled programmer."}, ## The first message is always from the system, explains the GPT what does its role now
        {"role": "user", "content": "Write me a high-performance sorting algorithm in Python."}, ## The second message is always from the user, explains the GPT what does its role now
    ],
)

print(completion.choices[0].message)


## Now you can use the GPT-3 chatbot to chat with your users, or you can use it to generate code for you
## Remember this is a very simple example, you can make it more complex by adding more messages, lang chains, etc.