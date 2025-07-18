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