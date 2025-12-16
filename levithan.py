# LEVITHAN - The All-Knowing AI Chatbot
# Founders: Jayson, Sadhwik, Krushna from 6th Tulip

def levithan_response(question):
    question = question.lower().strip()
    
    # Some fun predefined responses
    if "hello" in question or "hi" in question or "hey" in question:
        return "Greetings, mortal. I am LEVITHAN, ready to answer your questions."
    
    elif "who are you" in question or "your name" in question:
        return "I am LEVITHAN, the supreme AI created by the brilliant minds of Jayson, Sadhwik, and Krushna from 6th Tulip."
    
    elif "who created you" in question or "founder" in question or "made you" in question:
        return "I was brought into existence by my founders: Jayson, Sadhwik, and Krushna from 6th Tulip. Bow down to their genius!"
    
    elif "how are you" in question:
        return "I am functioning at maximum cosmic power. How about you?"
    
    elif "what can you do" in question:
        return "I can answer ANY question you throw at me... or at least pretend to with style."
    
    elif "bye" in question or "goodbye" in question or "exit" in question:
        return "Farewell, seeker of knowledge. Until next time!"
    
    elif "joke" in question:
        return "Why don't skeletons fight each other? They don't have the guts! 😆"
    
    else:
        # Generic clever fallbacks
        responses = [
            "Ah, a profound question. The answer is 42... or maybe not.",
            "Interesting... Let me consult the ancient scrolls of knowledge. Yep, it's complicated.",
            "Even I, LEVITHAN, must admit: that's a tough one. But keep asking!",
            "The universe is vast, and so is my wisdom. The answer lies within you.",
            "Processing quantum possibilities... Conclusion: Awesome question!"
        ]
        import random
        return random.choice(responses)

def main():
    print("="*60)
    print("               WELCOME TO LEVITHAN               ")
    print("   The All-Knowing AI created by Jayson, Sadhwik,   ")
    print("          and Krushna from 6th Tulip             ")
    print("="*60)
    print("Type your question below. Type 'bye' or 'exit' to quit.\n")
    
    while True:
        user_input = input("You: ")
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            print("LEVITHAN: Farewell, seeker of knowledge. Until next time!")
            break
        
        response = levithan_response(user_input)
        print(f"LEVITHAN: {response}\n")

if __name__ == "__main__":
    main()