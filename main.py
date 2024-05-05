import openai
from config.api_key import API_KEY

# Set OpenAI API key
openai.api_key = API_KEY

def chat_with_chatBot(prompt):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150
        )
        print(response.choices[0].message.content.strip())
        return response.choices[0].message.content.strip()
    
    except Exception as e:
        print("Error:", e)
        return "Sorry, something went wrong. Please try again later."


if __name__ == "__main__":
    print("Welcome to the Chatbot!")
    print("Type 'quit', 'exit', or 'bye' to end the conversation.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ["quit", "exit", "bye"]:
            print("Goodbye!")
            break
        
        if not user_input:
            print("Please provide a valid input.")
            continue
        
        response = chat_with_chatBot(user_input)
        print("Chatbot:", response)
