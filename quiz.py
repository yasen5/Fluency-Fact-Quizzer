import random
import json
import sys
import os

def load_facts(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

def quiz(facts):
    topics = list(facts.keys())
    categories = ["Who", "What", "Where", "When", "Why", "Significance"]
    
    while True:
        # Pick a random topic and category
        topic = random.choice(topics)
        category = random.choice(categories)
        
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

if __name__ == "__main__":
    if os.path.exists("ff.json"):
        json_file = "ff.json"
    else:
        if len(sys.argv) != 2:
            print("Usage: python quiz.py fluency_facts.json")
            sys.exit(1)
        
        json_file = sys.argv[1]

    facts = load_facts(json_file)
    quiz(facts)
