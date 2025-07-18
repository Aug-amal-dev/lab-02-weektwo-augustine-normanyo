def greet_user():
    print("Hello welcome to this survey")


def ask_question():
    import random

    question = [
        "How would you rate our product from 1 to 5?",
        "Would you recommend us to a friend? (yes/no)",
        "What feature would you like to see next?",
    ]

    selected_question = random.choice(question)
    valid_choice = None  # Initialize first!
    quest_type = None    # Good practice for clarity

    if selected_question == question[0]:
        valid_choice = ['1', '2', '3', '4', '5']
        quest_type = 'random'
    elif selected_question == question[1]:
        valid_choice = ['yes', 'no']
        quest_type = 'option'
    elif selected_question == question[2]:
        quest_type = 'normal'
        valid_choice = []  # Or another sensible default

    return valid_choice, quest_type, selected_question


def validate_response(question, valid_choice, question_type):
    while True:
        print(question)

        response = input(f"input your answer based on this '{question_type}': ").strip()

        if not response:
            print("Response cannot be empty.")
            continue

        if question_type == 'random':
            if response in valid_choice:
                return response
            print(f"{response} not in {valid_choice} or out of range")
            continue

        if question_type == 'option':
            if response.lower() in valid_choice:
                return response
            print(f"{response} not in {valid_choice} invalid input")
            continue

        if question_type == 'normal':
            return response
        

def print_response(question, response):
    import datetime
    
    return{
        "question": question,
        "response": response,
        "timestamp": datetime.datetime.now()
    }


try:
    greet_user()

    valid_choice, quest_type, selected_question = ask_question()

    response = validate_response(selected_question, valid_choice, quest_type)

    finale_response = print_response(selected_question, response)

    print(finale_response)

except Exception as e:
    print(e)

                


