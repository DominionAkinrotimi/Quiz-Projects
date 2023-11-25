# Define a class to represent a single question in the quiz
class Question:
    def __init__(self, text, choices, correct_answer):
        # Initialize question attributes
        self.text = text
        self.choices = choices
        self.correct_answer = correct_answer.upper()  # Store correct answer in uppercase

    # Check if the provided answer is correct
    def is_correct(self, answer):
        return answer.upper() == self.correct_answer


# Define a class to represent a section of the quiz, containing multiple questions
class QuizSection:
    def __init__(self, name, questions):
        # Initialize quiz section attributes
        self.name = name
        self.questions = questions
        self.score = 0  # Initialize score to 0

    # Run the quiz section
    def run(self):
        print(f"--- {self.name} Section ---")
        for i, question in enumerate(self.questions, start=1):
            print(f"\nQuestion {i}: {question.text}")
            for choice in question.choices:
                print(f"{choice}")
            answer = input("Your answer (enter the option): ").upper()  # Get user's answer in uppercase
            try:
                if question.is_correct(answer):
                    print("Correct!")  # Display correct message if the answer is right
                    self.score += 1  # Increment score for correct answers
                else:
                    print("Incorrect.")  # Display incorrect message for wrong answers
            except ValueError:
                print("Invalid input. Skipping question.")  # Handle invalid input

        print(f"\n--- Your Score in {self.name} Section: {self.score} out of {len(self.questions)} ---")
        return self.score  # Return the final score


# Main function to run the quiz
def main():
    # Sample questions for a section (Basic Physics)
    questions = [
        Question("What is the unit of electric current?", ["A. Watt", "B. Volt", "C. Ampere", "D. Newton"], "C"),
        Question("Which force holds the nucleus of an atom together?",
                 ["A. Gravitational force", "B. Strong nuclear force", "C. Electromagnetic force", "D. Weak nuclear force"], "B"),
        Question("What is the acceleration due to gravity on Earth?",
                 ["A. 9.8 m/s^2", "B. 5.67 x 10^-11 Nm^2/kg^2", "C. 3 x 10^8 m/s", "D. 6.63 x 10^-34 Js"], "A"),
        Question("What type of energy does a moving car have?",
                 ["A. Kinetic energy", "B. Potential energy", "C. Thermal energy", "D. Chemical energy"], "A"),
        Question("What is the chemical symbol for water?", ["A. O", "B. H2O", "C. CO2", "D. H2SO4"], "B"),
    ]

    physics_section = QuizSection("Basic Physics", questions)
    physics_score = physics_section.run()

    # After the quiz, offer to check corrections
    check_corrections = input("Do you want to check the corrections? (yes/no/retake): ").lower()
    if check_corrections == "yes":
        print("\n--- Corrections for Basic Physics Section ---")
        for i, question in enumerate(questions, start=1):
            print(f"\nQuestion {i}: {question.text}")
            print(f"Correct Answer: {question.correct_answer}")
    elif check_corrections == "retake":
        print("\n--- Take quiz again ---")
        physics_section = QuizSection("Basic Physics", questions)
        physics_score = physics_section.run()
    else:
        print("\nExiting the quiz!")
        print("\nThank you for taking the quiz!")


# Entry point of the program
if __name__ == "__main__":
    main()
