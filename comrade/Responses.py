
from queue import Empty


def user_responses(input_text):
    user_message = str(input_text).lower()
    
    if user_message is Empty:
        return "Please provide valid info"
    