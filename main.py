from openai import OpenAI
from config.api_key import API_KEY

client = OpenAI(api_key=API_KEY)

# Make the completion request
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
    ]
)

# Print the generated completion
print(completion.choices[0].message)
