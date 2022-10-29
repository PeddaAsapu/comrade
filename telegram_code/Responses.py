
def user_responses(input_text):
    user_message = str(input_text).lower()
    
    if not user_message:
        return "Please provide valid info"
    