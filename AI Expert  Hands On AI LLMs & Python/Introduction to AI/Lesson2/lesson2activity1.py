# 1. Importing Libraries
import colorama
from colorama import Fore, Style
from textblob import TextBlob

# 2. Initializing Colorama
colorama.init()

# 3. Greeting with Emojis and Colored Text
print(f"{Fore.CYAN}👋🕵️‍♂️ Welcome to Sentiment Spy! 📝️{Style.RESET_ALL}")

# 4. Asking for User's Name
user_name = input(f"{Fore.MAGENTA}Please enter your name: {Style.RESET_ALL} ").strip()
if not user_name:
    user_name = "MR. Secret Agent"

# 5. Conversation History Storage
conversation_history = []

# 6. Welcoming the User
print(f"\n{Fore.CYAN}Hello, Agent {user_name}!")
print(f"Type a Sentence and I will analyze your sentences with TextBlob and show you the sentiment. 🤖")
print(f"Type {Fore.YELLOW}'reset'{Fore.CYAN}, {Fore.YELLOW}'history'{Fore.CYAN}, or {Fore.YELLOW}'exit'{Fore.CYAN} to quit.{Style.RESET_ALL}\n")

# 7. The Main Loop
while True:
    user_input = input(f"{Fore.GREEN}>> {Style.RESET_ALL}").strip()
    
    if not user_input:
        print(f"{Fore.RED}Please enter some text or a valid command.{Style.RESET_ALL}")
        continue

    # 8. Command Handling
    if user_input.lower() == "exit":
        print(f"\n{Fore.BLUE}👋 Exiting Sentiment Spy. Farewell, Agent {user_name}! 🕵️‍♂️{Style.RESET_ALL}")
        break
    elif user_input.lower() == "reset":
        conversation_history.clear()
        print(f"{Fore.CYAN}🧹 All conversation history cleared!{Style.RESET_ALL}")
        continue
    elif user_input.lower() == "history":
        if not conversation_history:
            print(f"{Fore.YELLOW}No conversation history yet.{Style.RESET_ALL}")
        else:
            print(f"{Fore.CYAN}📜 Conversation History:{Style.RESET_ALL}")
            for idx, (text, polarity, sentiment_type) in enumerate(conversation_history, start=1):
                if sentiment_type == "Positive":
                    color = Fore.GREEN
                    emoji = "😊"
                elif sentiment_type == "Negative":
                    color = Fore.RED
                    emoji = "😞"
                else:
                    color = Fore.YELLOW
                    emoji = "😐"
                print(f"{idx}. {color}{emoji} {text} (Polarity: {polarity:.2f}, {sentiment_type}){Style.RESET_ALL}")
        continue

    # 9. Sentiment Analysis
    polarity = TextBlob(user_input).sentiment.polarity
    if polarity > 0.25:
        sentiment_type = "Positive"
        color = Fore.GREEN
        emoji = "😊"
    elif polarity < -0.25:
        sentiment_type = "Negative"
        color = Fore.RED
        emoji = "😞"
    else:
        sentiment_type = "Neutral"
        color = Fore.YELLOW
        emoji = "😐"

    # Storing and Displaying the Result
    conversation_history.append((user_input, polarity, sentiment_type))

    # Print result with color, emojis and polarity
    print(f"{color}{emoji} {sentiment_type} sentiment detected! (Polarity: {polarity:.2f}){Style.RESET_ALL}")
