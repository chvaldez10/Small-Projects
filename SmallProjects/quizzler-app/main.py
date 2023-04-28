from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizInterface
from data import *
import json

# question_bank = []
# for question in question_data:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)


# quiz = QuizBrain(question_bank)
# quiz_ui = QuizInterface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()

# print("You've completed the quiz")
# print(f"Your final score was: {quiz.score}/{quiz.question_number}")

################################################################
#
#          main function for quiz game
#
################################################################

parameters ={
    "amount": 10,
    "difficulty": "easy",
    "type": "boolean",
}

difficulty = ["Easy", "Medium", "Hard"]

def get_num_of_questions() -> int:
    try:
        num_of_questions = input("How many questions do you want?: ")
        if num_of_questions.lower() == "exit":
            exit()
        num_of_questions = int(num_of_questions)
        return num_of_questions
    except:
        print("That is not a valid number")
        return get_num_of_questions()

def get_difficulty() -> str:
    global difficulty

    diff = input("What difficulty do you want?: ")

    if diff.lower() == "exit":
        exit()
    elif diff.title() not in difficulty:
        print("Not a valid difficulty")
        return get_difficulty()
    
    return diff.lower()


def fill_parameters() -> None:
    global parameters

    parameters["amount"] = get_num_of_questions()
    parameters["difficulty"] = get_difficulty()

    paramas_pretty = json.dumps(parameters, indent=4)
    print(f"\nParameters chosen:\n\n{paramas_pretty}\n")

def play_quiz_game() -> None:
    global parameters

    question_data = get_data_from_api(parameters)

    question_bank = []
    for question in question_data:
        question_text = question["question"]
        question_answer = question["correct_answer"]
        new_question = Question(question_text, question_answer)
        question_bank.append(new_question)

    quiz = QuizBrain(question_bank)
    quiz_ui = QuizInterface(quiz)

fill_parameters()    
play_quiz_game()