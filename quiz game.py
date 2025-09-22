questions = [
 {"question": "What is the capital of France?", "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) {"question": "Which language is used for web apps?", "options": ["A) Python", "B) JavaScript", "C) C {"question": "What is 5 + 7?", "options": ["A) 10", "B) 11", "C) 12", "D) 13"], "answer": "C"},
]
def play_quiz():
 score = 0
 print("=== Welcome to the Quiz Game ===")
 for q in questions:
 print("\n" + q["question"])
 for option in q["options"]:
 print(option)
 answer = input("Enter your answer (A/B/C/D): ").strip().upper()
 if answer == q["answer"]:
 print("Correct!")
 score += 1
 else:
 print(f"Wrong! The correct answer was {q['answer']}.")
 print(f"\nYour final score: {score}/{len(questions)}")
if __name__ == "__main__":
 play_quiz()