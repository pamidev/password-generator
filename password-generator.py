import random


print("""

* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
*  Program generuje hasła na podstawie wprowadzonych wytycznych.  *
*  Zanim go wygeneruje, musisz odpowiedzieć na kilka pytań,       *
*  podając odpowiedź jako T (tak) lub N (nie).                    *
*  Jeśli natomiast chcesz zakończyć program,                      * 
*  wpisz w dowolnym momencie q lub Q.                             *
* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *

""")

upper_list = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
upper_list = random.sample(upper_list, k=len(upper_list))
lower_list = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]
lower_list = random.sample(lower_list, k=len(lower_list))
special_list = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "}", "[", "]", "|", "\\", ":", ";", '"', "'", "<", ">", ",", ".", "?", "/"]
special_list = random.sample(special_list, k=len(special_list))
digit_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
digit_list = random.sample(digit_list, k=len(digit_list))
generate_list = upper_list + lower_list + special_list + digit_list
generate_from = []
counter = 0
password = ""


def decision_validator(decision_to_validate: str):
    if decision_to_validate.isalpha() and decision_to_validate == "t":
        return True
    elif decision_to_validate.isalpha() and decision_to_validate == "T":
        return True
    elif decision_to_validate.isalpha() and decision_to_validate == "n":
        return True
    elif decision_to_validate.isalpha() and decision_to_validate == "N":
        return True
    elif decision_to_validate.isalpha() and decision_to_validate == "q":
        return True
    elif decision_to_validate.isalpha() and decision_to_validate == "Q":
        return True
    else:
        return False
    

decision = input("Czy mam wygenerować dla Ciebie hasło (T/N)? ")
if decision.isalpha() and decision == "n" or decision == "N" or decision == "q" or decision == "Q":
    print("Koniec programu.")
else:
    while not decision_validator(decision):
        print("Nie wprowadzono prawidłowo decycji: T - tak, N - nie, Q - koniec programu. Spróbuj więc ponownie.")
        decision = input("Czy mam wygenerować dla Ciebie hasło (T/N)? ")
    else:
        how_long = input("1) Z ilu znaków ma składać się Twoje hasło (nie więcej niż 92)? ")
        while not how_long.isdigit() or int(how_long) > 92:
            print("Nie wprowadzono prawidłowo decycji: T - tak, N - nie, Q - koniec programu lub podano długość hasła powyżej 92 znaków. Spróbuj więc ponownie.")
            how_long = input("1) Z ilu znaków ma składać się Twoje hasło? ")
        else:
            how_long = int(how_long)
            is_upper = input("2) Czy hasło ma obligatoryjnie zawierać wielkie litery (T/N)? ")
            while not decision_validator(is_upper):
                print("Nie wprowadzono prawidłowo decycji: T - tak, N - nie, Q - koniec programu. Spróbuj więc ponownie.")
                is_upper = input("2) Czy hasło ma obligatoryjnie zawierać wielkie litery (T/N)? ")
            else:
                if is_upper == "q" or is_upper == "Q":
                    print("Koniec programu.")
                else:
                    if is_upper == "t" or is_upper == "T":
                        generate_from += random.sample(upper_list, k=1)  # zmienić logikę dodawania losowych znaków do listy
                        counter += 1
                    # else:
                    #     generate_list = [lower_list + special_list + digit_list]
                    is_lower = input("3) Czy hasło ma obligatoryjnie zawierać małe litery (T/N)? ")
                    while not decision_validator(is_lower):
                        print("Nie wprowadzono prawidłowo decycji: T - tak, N - nie, Q - koniec programu. Spróbuj więc ponownie.")
                        is_lower = input("3) Czy hasło ma obligatoryjnie zawierać małe litery (T/N)? ")
                    else:
                        if is_lower == "q" or is_lower == "Q":
                            print("Koniec programu.")
                        else:
                            if is_lower == "t" or is_lower == "T":
                                generate_from += random.sample(lower_list, k=1)  # zmienić logikę dodawania losowych znaków do listy
                                counter += 1
                            # else:
                            #     generate_list = [special_list + digit_list]
                            is_special = input("4) Czy hasło ma obligatoryjnie zawierać znaki specjalne (T/N)? ")
                            while not decision_validator(is_special):
                                print("Nie wprowadzono prawidłowo decycji: T - tak, N - nie, Q - koniec programu. Spróbuj więc ponownie.")
                                is_special = input("4) Czy hasło ma obligatoryjnie zawierać znaki specjalne (T/N)? ")
                            else:
                                if is_special == "q" or is_special == "Q":
                                    print("Koniec programu.")
                                else:
                                    if is_special == "t" or is_special == "T":
                                        generate_from += random.sample(special_list, k=1)  # zmienić logikę dodawania losowych znaków do listy
                                        counter += 1
                                    # else:
                                    #     generate_list = [digit_list]
                                    is_digit = input("5) Czy hasło ma obligatoryjnie zawierać cyfry (T/N)? ")
                                    while not decision_validator(is_digit):
                                        print("Nie wprowadzono prawidłowo decycji: T - tak, N - nie, Q - koniec programu. Spróbuj więc ponownie.")
                                        is_digit = input("5) Czy hasło ma obligatoryjnie zawierać cyfry (T/N)? ")
                                    else:
                                        if is_digit == "q" or is_digit == "Q":
                                            print("Koniec programu.")
                                        else:
                                            if is_digit == "t" or is_digit == "T":
                                                generate_from += random.sample(digit_list, k=1)   # zmienić logikę dodawania losowych znaków do listy
                                                counter += 1
                                            # else:
                                            #     generate_list = []
                                            if counter > how_long:
                                                print(f"Podana przez Ciebie ilość znaków hasła ({how_long}) nie spełni wszystkich wybranych warunków ({counter}).")
                                                new_decision = input(f"Czy zatem wygenerować dla Ciebie hasło o długości {counter} znaków? ")
                                                while not decision_validator(new_decision):
                                                    print("Nie wprowadzono prawidłowo decycji: T - tak, N - nie, Q - koniec programu. Spróbuj więc ponownie.")
                                                    new_decision = input(f"Czy zatem wygenerować dla Ciebie hasło o długości {counter} znaków? ")
                                                else:
                                                    if new_decision == "q" or new_decision == "Q":
                                                        print("Koniec programu.")
                                                    else:
                                                        if new_decision == "t" or new_decision == "T":
                                                            how_long = counter
                                                        else:
                                                            print("W takim razie nie mogę wygenerować hasła. Uruchom program ponownie, zmieniając swoje wybory.")
                                            generate_from += random.sample(generate_list, k=(how_long - counter))
                                            gen_password = random.sample(generate_from, k=(len(generate_from)))
                                            for char in range(len(gen_password)):
                                                password += gen_password[char]
                                            print()
                                            print(f"Twoje wygenerowane hasło to: {password}")
