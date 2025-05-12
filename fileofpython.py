import random

questions = [
    {
        "question": "What is the next number in the sequence: 2, 4, 8, 16, ?",
        "options": ["18", "20", "32", "24"],
        "answer": "32"
    },
    {
        "question": "Which shape has the most sides?",
        "options": ["Triangle", "Hexagon", "Pentagon", "Square"],
        "answer": "Hexagon"
    },
    {
        "question": "If all Bloops are Razzies and all Razzies are Lazzies, are all Bloops definitely Lazzies?",
        "options": ["Yes", "No", "Maybe", "Cannot say"],
        "answer": "Yes"
    },
    {
        "question": "What is the odd one out: Apple, Banana, Carrot, Grape?",
        "options": ["Apple", "Banana", "Carrot", "Grape"],
        "answer": "Carrot"
    },
    {
        "question": "If you rearrange the letters 'CIFAIPC', you get the name of a:",
        "options": ["City", "Animal", "Ocean", "Country"],
        "answer": "Ocean"
    }
]

def play_quiz():
    score = 0
    random.shuffle(questions)
    for q in questions:
        print("\n" + q["question"])
        for idx, opt in enumerate(q["options"], 1):
            print(f"{idx}. {opt}")
        try:
            choice = int(input("Your answer (1-4): "))
            if q["options"][choice - 1] == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is: {q['answer']}")
        except (ValueError, IndexError):
            print("Invalid input. Skipping question.")
    print(f"\nQuiz finished! Your score: {score}/{len(questions)}")

if __name__ == "__main__":
    play_quiz()