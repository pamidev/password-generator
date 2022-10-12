import secrets
import string


def password_generator(pass_lenght:int = 8):
    characters_set = (string.ascii_letters +
                      string.digits +
                      string.punctuation)
    while True:
        gen_pass = ''
        for l in range(pass_lenght):
            gen_pass += ''.join(secrets.choice(characters_set))
        if (any(char in string.punctuation for char in gen_pass) and
            sum(char in string.digits for char in gen_pass) >= 2 and
            sum(char in string.ascii_lowercase for char in gen_pass) >= 2 and
            sum(char in string.ascii_uppercase for char in gen_pass) >= 2):
            break
    return gen_pass

try:
    lenght = int(input("Enter password lenght (at least 8): "))
    if lenght >= 8:
        pwd = password_generator(lenght)
        print(f"Your strong password is: {pwd}")
    else:
        print("Check password lenght. Must be at least 8.")
except ValueError:
    print("Entered bad data. Try again.")
