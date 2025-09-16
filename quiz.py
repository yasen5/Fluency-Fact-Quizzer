import json
import sys
import os
import random  # Import random for shuffling

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
        print(question)
        
        if category.lower() == "when":
            correct_answer = facts[topic].get(category, 'N/A')
            for attempt in range(2):
                user_answer = input("Your answer (attempt {}/2): ".format(attempt + 1))
                if user_answer == str(correct_answer):
                    print("🎉 Correct!")
                    break
                else:
                    if (attempt == 1):
                        wrongQuestions.append([question, correct_answer])
                    print("❌ Incorrect.")
            else:
                print(f"✅ Correct answer: {correct_answer}")
        else:
            input("Your answer: ")  # user types but we don’t grade it automatically
            print(f"✅ Correct answer: {facts[topic].get(category, 'N/A')}")

        if (questionCounter >= 5):
            print("\n=================================\nTake this chance to correct what you got wrong!\n=================================")
            intRange = len(wrongQuestions)
            for i in range(intRange):
                question = wrongQuestions.pop(0)
                print(question[0])
                user_answer = input("Your answer: ")
                if user_answer == str(question[1]):
                    print("🎉 Correct!")
                else:
                    wrongQuestions.append(question)
                    print("❌ Incorrect.")
            questionCounter = 0
                

    print("\n🎉 You've completed all the questions!")

if __name__ == "__main__":
    if os.path.exists("ff.json"):
        facts = load_facts("ff.json")
        if (len(sys.argv) > 1):
            quiz(facts, [sys.argv[1]])
        quiz(facts)
    else:
        print("Error: 'ff.json' file not found.")