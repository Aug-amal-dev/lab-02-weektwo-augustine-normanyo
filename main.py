from survey.greeter import greet_user
from survey.question import ask_question
from survey.validator import validate_response
from survey.recorder import print_response

def main():
    try:
        greet_user()

        valid_choice, quest_type, selected_question = ask_question()

        response = validate_response(selected_question, valid_choice, quest_type)

        finale_response = print_response(selected_question, response)

        print(finale_response)

    except Exception as e:
        print(e)

main()