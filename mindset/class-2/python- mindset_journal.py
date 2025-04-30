import random
import datetime

affirmations = [
    "You are capable of achieving great things!",
    "Your mind is powerful. Think positive!",
    "Every day is a new opportunity to grow.",
    "You are in control of your own happiness.",
    "You are strong, smart, and capable.",
    "Believe in yourself and all that you are."
]

mindfulness_tips = [
    "Take deep breaths and focus on the present moment.",
    "Write down three things you’re grateful for.",
    "Take a short walk and clear your mind.",
    "Practice meditation for at least 5 minutes.",
    "Avoid negative self-talk and be kind to yourself.",
    "Limit screen time and spend time in nature."
]

def get_daily_affirmation():
    return random.choice(affirmations)

def get_mindfulness_tip():
    return random.choice(mindfulness_tips)

def journal_entry():
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = input("\nWrite your thoughts for today: ")
    
    with open("mindset_journal.txt", "a") as file:
        file.write(f"\n[{date}] {entry}\n")
    
    print("\nYour entry has been saved! Keep going! 💪")

def main():
    print("\n💡 Welcome to Your Positive Mindset Journal! 💡\n")
    print(f"🌟 Daily Affirmation: {get_daily_affirmation()}\n")
    print(f"🧘 Mindfulness Tip: {get_mindfulness_tip()}\n")
    
    choice = input("Would you like to write in your journal? (yes/no): ").lower()
    if choice == "yes":
        journal_entry()
    else:
        print("\nNo worries! Stay positive and keep smiling! 😊")

if __name__ == "__main__":
    main()
