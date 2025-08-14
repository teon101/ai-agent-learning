import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simple_chat():
    """
    Simple chatbot that takes user input and responds using OpenAI GPT
    """
    print("🤖 Simple AI Chatbot")
    print("Type 'quit' to exit\n")
    
    while True:
        # Get user input
        user_message = input("You: ")
        
        if user_message.lower() == 'quit':
            print("👋 Goodbye!")
            break
            
        try:
            # Make API call to OpenAI
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
                messages=[
                    {
                        "role": "system", 
                        "content": "You are a helpful and friendly AI assistant. Keep responses concise and helpful."
                    },
                    {
                        "role": "user", 
                        "content": user_message
                    }
                ],
                temperature=0.7,  # Balanced creativity
                max_tokens=150    # Keep responses short for demo
            )
            
            # Extract and display the response
            ai_response = response.choices[0].message.content
            print(f"🤖 AI: {ai_response}\n")
            
        except Exception as e:
            print(f"❌ Error: {e}\n")
            print("💡 Make sure you have:")
            print("1. Set your OPENAI_API_KEY in .env file")
            print("2. Installed required packages: pip install openai python-dotenv\n")

def prompt_examples():
    """
    Show different prompt techniques and their effects
    """
    print("\n🧪 Prompt Engineering Examples")
    print("=" * 40)
    
    # Example prompts to test
    prompts = [
        {
            "name": "Basic Question",
            "system": "You are an AI assistant.",
            "user": "What is Python?"
        },
        {
            "name": "Role-Playing",
            "system": "You are a friendly coding teacher who explains things simply.",
            "user": "What is Python?"
        },
        {
            "name": "Structured Response",
            "system": "You are a helpful assistant. Always structure your responses with bullet points.",
            "user": "What is Python?"
        }
    ]
    
    for i, prompt in enumerate(prompts, 1):
        print(f"\n{i}. {prompt['name']}")
        print(f"System: {prompt['system']}")
        print(f"User: {prompt['user']}")
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": prompt['system']},
                    {"role": "user", "content": prompt['user']}
                ],
                temperature=0.5,
                max_tokens=100
            )
            
            ai_response = response.choices[0].message.content
            print(f"Response: {ai_response}")
            print("-" * 40)
            
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Simple Chat")
    print("2. Prompt Examples")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == "1":
        simple_chat()
    elif choice == "2":
        prompt_examples()
    else:
        print("Invalid choice. Running simple chat...")
        simple_chat()
