def print_response(question, response):
    import datetime
    
    return{
        "question": question,
        "response": response,
        "timestamp": datetime.datetime.now()
    }
