import secrets
import string


def password_generator(pass_length: int = 12):
    characters_set = (string.ascii_letters +
                      string.digits +
                      string.punctuation)
    while True:
        gen_pass = ''
        for l in range(pass_length):
            gen_pass += ''.join(secrets.choice(characters_set))
        if (any(char in string.punctuation for char in gen_pass) and
                sum(char in string.digits for char in gen_pass) >= 2 and
                sum(char in string.ascii_lowercase for char in gen_pass) >= 2 and
                sum(char in string.ascii_uppercase for char in gen_pass) >= 2):
            break
    return gen_pass


try:
    length = int(input("Enter password length (at least 12 characters): "))
    if length >= 8:
        pwd = password_generator(length)
        print(f"Your strong password is: {pwd}")
    else:
        print("Check password length. Must be at least 12 characters.")
except ValueError:
    print("Entered bad data. Try again.")
