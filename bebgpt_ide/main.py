from bebgpt_core import BebGpt
import sys

def main():
    # ইউজার চাইলে এখানে এনভায়রনমেন্ট ভেরিয়েবল থেকে কি নিতে পারবে
    ai = BebGpt(claude_api_key="sk-dummy-key")
    
    print(f"--- {ai.name} এ আপনাকে স্বাগতম ---")
    print("এটি 'free-claude-code' এবং 'Replit' এর সমন্বয়ে তৈরি।")
    print("কমান্ডস: 'exit' (বন্ধ), '/provider [name]' (প্রোভাইডার পরিবর্তন)")
    
    while True:
        user_input = input(f"\n[Provider: {ai.provider}] আপনি: ")
        
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"{ai.name}: বিদায়! আবার দেখা হবে।")
            break
        
        if user_input.startswith("/provider"):
            try:
                new_p = user_input.split(" ")[1]
                print(f"{ai.name}: {ai.set_provider(new_p)}")
                continue
            except IndexError:
                print(f"{ai.name}: দয়া করে একটি নাম দিন (যেমন: google, groq, deepseek)")
                continue

        if "code" in user_input.lower() or "run" in user_input.lower():
            response = ai.execute_on_replit(user_input)
        else:
            response = ai.ask_ai(user_input)
            
        print(f"{ai.name}: {response}")

if __name__ == "__main__":
    main()
