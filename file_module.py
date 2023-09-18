import os
import random
import string

def create_folder(folder_name):
    """Creates a folder with the given name. If the folder already exists, it does nothing."""
    try:
        os.makedirs(folder_name, exist_ok=True)
    except OSError as e:
        print(f"Error creating folder {folder_name}. Error: {e}")
        return False
    return True

def generate_random_filename():
    """Generates a random filename using lowercase letters with a length of 8."""
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for _ in range(8))
    return random_string
