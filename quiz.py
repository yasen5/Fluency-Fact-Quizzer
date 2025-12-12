import json
import re
import sys
import os
import random

def sanitize(s: str) -> str:
    s = re.sub(r'[^0-9-]', '', str(s))  # keep digits and hyphens
    return s[:9]  # first 9 characters

def ask_question(question, answer: str, wrongQuestions):
    print(question)
    response = input("Your answer: ")
    if sanitize(answer) == str(response).replace("s", ""):
        print("🎉 Correct!")
    elif str(response) in answer:
        print("Please remember to add an end date")
        ask_question(question, answer, wrongQuestions)
    else:
        wrongQuestions.append([question, answer])
        print("❌ Incorrect.")
        print(f"✅ Correct answer: {answer}")

def load_facts(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        return json.load(f)

def quiz(facts, categories = ["Who", "What", "Where", "When", "Why", "Significance"]):
    questionCounter = 0
    wrongQuestions = []
    topics = list(facts.keys())
    
    # Generate all possible questions (topic, category pairs)
    questions = [(topic, category) for topic in topics for category in categories]
    random.shuffle(questions)  # Shuffle the questions to randomize the order
    
    for topic, category in questions:
        questionCounter += 1
        question = f"\n📘 {topic} — {category}:"

        category = category[0].upper() + category[1:]
        
        if category.lower() == "when":
            correct_answer = facts[topic].get(category, "Couldn't find for topic " + topic)
            ask_question(question, correct_answer, wrongQuestions)
            
        else:
            print(question)
            input("Press 'Enter' to see the description: ")  # user types but we don’t grade it automatically
            print(f"{facts[topic].get(category, 'N/A')}")

        if (questionCounter >= 5):
            intRange = len(wrongQuestions)
            if (intRange > 0):
                print("\n=================================\nTake this chance to correct what you got wrong!\n=================================")
                for i in range(intRange):
                    question = wrongQuestions.pop(0)
                    ask_question(question[0], question[1], wrongQuestions)
            questionCounter = 0
                

    print("\n🎉 You've completed all the questions!")
    exit(0)

if __name__ == "__main__":
    if os.path.exists("ff.json"):
        facts = load_facts("ff.json")
        if (len(sys.argv) > 1):
            quiz(facts, [sys.argv[1]])
        else:
            quiz(facts)
    else:
        print("Error: 'ff.json' file not found.")