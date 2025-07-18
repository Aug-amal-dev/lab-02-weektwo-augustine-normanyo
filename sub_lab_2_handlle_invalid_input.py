def greet_user():
    print("Hello welcome to this survey")


def ask_question():
    question = "How would you rate as from 1 - 5"

    valid_choices = ['1', '2', '3', '4', '5']

    return question, valid_choices


def validat_response(question, choices):
    while True:
        print(question)
        response = input(f"choose from {choices}: " ).strip()

        if response in choices:
            return response
        elif len(response) == 0:
            print("Input must not be empty")
        else:
            print("Invalid input input out of range")


def record_response(response):
    if response:
        print(f"Response recorded: {response}")


try:
    greet_user()

    question, choices = ask_question()

    final_response = validat_response(question, choices)

    record_response(final_response)

except Exception as e:
    print(e)

