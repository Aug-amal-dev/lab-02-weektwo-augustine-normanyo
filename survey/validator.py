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