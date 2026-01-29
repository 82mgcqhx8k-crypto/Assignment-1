import os
import random
import string
import time

list_words = [
    'apple', 'banana', 'cherry', 'date', 'elderberry', 'grape',
    'honeydew', 'kiwi', 'lemon', 'mango', 'orange' , 'papaya',
    'raspberry', 'strawberry', 'tangerine', 'watermelon'
]
def memorable_password(num_words):
    selected_words = random.sample(list_words, num_words)
    password_parts = []
    for word in selected_words:
        digit_random = str(random.randint(0, 9))
        password_parts.append(word + digit_random)
    password_memorable_file = "-".join(password_parts)
    save_password(password_memorable_file, 'Memorable Passwords')
    return password_memorable_file

def random_password(length=12, include_punctuation=True, exclude_character=''):

    chars = list(string.ascii_letters + string.digits)
    if include_punctuation:
        chars += list(string.punctuation)

    new_chars = []
    for c in chars:
        if c not in exclude_character:
            new_chars.append(c)
    chars = new_chars

    password_random_file = ''.join(random.choice(chars)
    for _ in range(length))
    save_password(password_random_file, 'Random Passwords')
    return password_random_file

def save_password(password, folder):

    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, 'Passwords.txt')

    password_made = time.ctime()

    # add password and timestamp of when it was created
    with open(filename, 'a') as f:
        f.write(f"{password} , Created at: {password_made}\n")

def generate_password():
    type_of_password = input("Enter your desired password type ('memorable' or 'random'): ").strip().lower()
    if type_of_password == 'memorable':
        num_words = int(input("How many words do you want to include in your memorable password?: "))
        print(" Here is your generated memorable password:", memorable_password(num_words))
    elif type_of_password == 'random':
        length = int(input("Enter password length: "))
        include_punct = input("Any punctuation in your password? (yes/no): ").strip().lower() == 'yes'
        exclude = input("Want to exclude any characters? (leave blank if no characters to exclude): ")
        print("Here is your random password:", random_password(length, include_punct, exclude))
    else:
        print("Invalid type. Please enter 'Memorable' or 'Random'.")

generate_password()

