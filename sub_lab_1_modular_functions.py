def greet_user():
    print("Hello welcome to this survey")

def ask_question():
    import random
    questions = [
        "How satisfied are you with our product?",
        "Would you recommend us to a friend?",
        "What can we improve?"
    ]

    return random.choice(questions)

def record_responses(question, response):
    return{
        "question": question,
        "response": response
    }
    

try:
    greet_user()

    question = ask_question()
    print(question)

    res = input("input your answer here ")

    record = record_responses(question, res)
    print(record)


except Exception as e:
    print("something went wrong ", e)
