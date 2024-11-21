import time

# Welcome feature
def Welcome():
    print("Welcome to Voting Education Assistant.")
    print("This program will test your knowledge about the electoral process.")
    print("If you get enough score, you will be able to vote. If not, you will receive recommendations to improve.")
    print("¡Let's start!\n")
    time.sleep(2)  # Causes the program to pause for two seconds before continuing

# Function to display a simulated progress bar
def progress_bar(progress, total):
    percentage = (progress / total) * 100
    bar = f"[{'#' * int(percentage // 5)}{'-' * (20 - int(percentage // 5))}]"
    print(f"\rProgress: {bar} {int(percentage)}%", end="", flush=True)

# Quiz feature
def quiz():  # Modify questions and answers
    questions = [
        {
            "question": "Why is it important to participate in elections?",
            "options": ["a) Because all votes count", "b) Because voting is a right and a duty", "c) Because voting influences future decisions", "d) All of the above"],
            "answer": "d",
            "weighting": 2
        },
        {
            "question": "What does it mean to vote informedly?",
            "options": ["a) Learn about each candidate's proposals", "b) Research each candidate's background", "c) Understand how the proposed policies will affect the community", "d) All of the above"],
            "answer": "d",
            "weighting": 2
        },
        {
            "question": "Is it okay to vote based on unverified information or rumors?",
            "options": ["a) Yes", "b) No"],
            "answer": "b",
            "weighting": 1
        },
        {
            "question": "Is your vote anonymous and protected by law in democratic elections?",
            "options": ["a) Yes", "b) No"],
            "answer": "a",
            "weighting": 1
        },
        {
            "question": "Select one benefit of democracy:",
            "options": ["a) Freedom of expression", "b) Equality before the law", "c) Opportunity to elect leaders", "d) All of the above"],
            "answer": "d",
            "weighting": 3
        },
        {
            "question": "Complete: In a democracy, power resides in ____.",
            "options": ["a) the government", "b) the citizens", "c) the media", "d) the political parties"],
            "answer": "b",
            "weighting": 2
        }
    ]

    # Performance counters
    correct = 0
    total_score = sum(question['weighting'] for question in questions)  # Calculate total score
    score_obtained = 0

    print("The questionnaire consists of 6 questions. Read carefully and answer.")
    time.sleep(2)

    for i, question in enumerate(questions):
        print(f"\nQuestion {i + 1}: {question['question']}")
        for option in question["options"]:
            print(option)

        response_start = time.time()  # Capture the start of the response
        response = input("Enter the letter of your response: ").strip().lower()
        response_time = time.time() - response_start  # Time it took to respond

        if response == question["answer"]:  # Corrected from 'answer'
            print(f"Correct! (+{question['weighting']} points)")
            correct += 1
            score_obtained += question["weighting"]
        else:
            print(f"Incorrect. The correct answer was: {question['answer'].upper()}. (+0 points)")

        print(f"Time taken: {response_time:.2f} seconds.")
        time.sleep(1)

        # Show progress bar
        progress_bar(i + 1, len(questions))

    print("\n\nEvaluation completed.")
    time.sleep(1)

    # Display results
    print(f"Correct answers: {correct}/{len(questions)}")
    print(f"Score obtained: {score_obtained}/{total_score}")

    # Performance-based feedback
    if score_obtained >= (0.7 * total_score):  # 70% or more to pass
        print("\nCongratulations! You have the knowledge to vote.")
    else:
        print("\nYou did not reach the necessary score to vote.")
        print("We recommend reviewing information about the electoral process and the importance of informed voting.")
        print("Visit trusted websites or consult with civic education specialists.")

# Function to close the program
def farewell():
    print("\nThank you for using the Educational Voting Assistant.")
    print("Remember that an informed vote is a powerful vote.")
    print("See you next time!")
    time.sleep(2)

# Main function
def main():
    Welcome()
    quiz()
    farewell()

# Ejecución del programa
if __name__ == "__main__":
    main()
