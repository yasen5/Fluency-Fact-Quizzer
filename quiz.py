import json
import sys
import os
import random  # Import random for shuffling

def load_facts(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

def quiz(facts):
    topics = list(facts.keys())
    categories = ["Who", "What", "Where", "When", "Why", "Significance"]
    
    # Generate all possible questions (topic, category pairs)
    questions = [(topic, category) for topic in topics for category in categories]
    random.shuffle(questions)  # Shuffle the questions to randomize the order
    
    for topic, category in questions:
        print(f"\n📘 {topic} — {category}:")
        
        if category.lower() == "when":
            correct_answer = facts[topic].get(category, 'N/A')
            for attempt in range(2):
                user_answer = input("Your answer (attempt {}/2): ".format(attempt + 1))
                if user_answer == str(correct_answer):
                    print("🎉 Correct!")
                    break
                else:
                    print("❌ Incorrect.")
            else:
                print(f"✅ Correct answer: {correct_answer}")
        else:
            input("Your answer: ")  # user types but we don’t grade it automatically
            print(f"✅ Correct answer: {facts[topic].get(category, 'N/A')}")

    print("\n🎉 You've completed all the questions!")

if __name__ == "__main__":
    if os.path.exists("ff.json"):
        facts = load_facts("ff.json")
        quiz(facts)
    else:
        print("Error: 'ff.json' file not found.")