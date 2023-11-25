# Import the 'random' module to shuffle questions and choices.
import random

# Define a class representing a question in the quiz.
class Question:
    def __init__(self, text, choices, correct_answer):
        # Initialize the question with its text, choices, and correct answer.
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer

    # Define a method to check if the provided answer is correct.
    def is_correct(self, answer):
        return answer.lower() == self.correct_answer.lower()

# Define a class representing a section of the quiz.
class QuizSection:
    def __init__(self, name, questions):
        # Initialize the section with a name and a list of questions.
        self.name = name
        self.questions = questions
        self.score = 0

    # Define a method to run the quiz section.
    def run(self):
        print(f"--- {self.name} Section ---")
        # Iterate through each question in the section.
        for i, question in enumerate(self.questions, start=1):
            # Print the question text and choices.
            print(f"\nQuestion {i}: {question.text}")
            print('\n'.join(question.choices))

            # Get the user's answer and convert it to uppercase.
            answer = input("Your answer (enter the letter): ").upper()

            # Check if the answer is correct and provide feedback.
            if question.is_correct(answer):
                print("Correct!")
                self.score += 1
            else:
                print("Incorrect.")

        # Print the user's score at the end of the section.
        print(f"\n--- Your Score in {self.name} Section: {self.score} out of {len(self.questions)} ---")
        return self.score

# Define a function to read questions from a file and create Question objects.
def read_questions_from_file(file_path):
    # Open the file in read mode and read lines.
    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Initialize variables to store questions and choices.
    questions = []
    current_question = None

    # Iterate through each line in the file.
    for line in lines:
        line = line.strip()
        # Check if the line starts with "Question" to identify a new question.
        if line.startswith("Question"):
            # If a question is already in progress, add it to the list.
            if current_question:
                questions.append(current_question)
            # Extract the text of the new question.
            text = line.split(": ", 1)[1]
            # Initialize an empty list to store choices.
            choices = []
        # Check if the line starts with "Correct Answer" to identify the correct answer.
        elif line.startswith("Correct Answer:"):
            # Extract the correct answer and create a Question object.
            correct_answer = line.split(": ", 1)[1]
            current_question = Question(text, choices, correct_answer)
        else:
            # Add choices to the list.
            choices.append(line)

    # Add the last question to the list.
    if current_question:
        questions.append(current_question)

    return questions

# Define a function to generate a quiz with shuffled questions.
def generate_quiz(file_path, num_questions):
    # Read questions from the file.
    all_questions = read_questions_from_file(file_path)
    # Shuffle all questions and select a subset for the quiz.
    random.shuffle(all_questions)
    selected_questions = all_questions[:num_questions]
    return selected_questions

# Define the main function that orchestrates the quiz.
def main():
    # Define the path to the file containing quiz questions.
    questions_file_path = 'computer_literacy_questions.txt'
    # Define the number of questions to include in the quiz.
    num_questions = 5

    # Start an infinite loop for repeated quizzes.
    while True:
        # Generate a new quiz with shuffled questions.
        questions = generate_quiz(questions_file_path, num_questions)
        # Create a QuizSection object for the Computer Literacy section.
        section = QuizSection("Computer Literacy", questions)
        # Run the quiz section.
        section.run()

        # Ask the user if they want to check corrections or retake the quiz.
        check_corrections = input("Do you want to check the corrections? (yes/no/retake): ").lower()
        if check_corrections == "yes":
            # Print corrections if the user chooses to check them.
            print("\n--- Corrections for Computer Literacy Section ---")
            for i, question in enumerate(questions, start=1):
                print(f"\nQuestion {i}: {question.text}")
                print(f"Correct Answer: {question.correct_answer}")
        elif check_corrections == "retake":
            # Restart the loop to retake the quiz.
            print("\n--- Retake quiz ---")
        else:
            # Exit the loop and end the program if the user chooses to exit.
            print("\nExiting the quiz!")
            print("\nThank you for taking the quiz!")
            break

# Check if the script is being run directly (not imported).
if __name__ == "__main__":
    # Call the main function to start the quiz.
    main()
