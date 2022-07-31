
import random
from colorama import Fore, Style
from request_handler import to_polish, CAPITALS

OPTIONS = str(CAPITALS.keys())[10:-1]

CATEGORIES_MSG = f"Witaj w quizie stolic. Podaj kategorie, których chcesz się uczyć {OPTIONS}:\n"
EMPTY_POOL_ERROR_MSG = "Pula pytań pusta."
QUESTION_NUMBER_ERROR_MSG = "Liczba pytań większa od liczby możliwości!"

def generate_question_pool(categories_choice: str) -> list:
    pool = []
    for category in CAPITALS.keys():
        if category in categories_choice:
            pool.extend(CAPITALS[category].items())
            print(Fore.GREEN + load_success_msg(category))
    print(Style.RESET_ALL, end = '')

    if len(pool) == 0:
        print(Fore.RED + "Nie znaleziono żadnej kategorii." + Style.RESET_ALL)
        raise Exception(EMPTY_POOL_ERROR_MSG)

    return pool

def load_success_msg(category: str) -> str:
    return f"Załadowano kategorię {category}."

def ask(country: str, capital: str) -> bool:
    answer = input(f"{country}: ")
    if answer.lower() == capital.lower():
        print(Fore.GREEN + "Poprawnie!" + Style.RESET_ALL)
        return 1
    print(Fore.RED + "Niepoprawnie! Prawidłowa odwpowiedź to:" + Fore.YELLOW, capital + Style.RESET_ALL)
    return 0

def run():
    categories_choice = input(CATEGORIES_MSG)
    question_pool = generate_question_pool(categories_choice)
    
    random.shuffle(question_pool)

    question_number = int(input(f"Podaj liczbę pytań [max {len(question_pool)}]: "))

    if question_number > len(question_pool):
        raise Exception(QUESTION_NUMBER_ERROR_MSG)

    # These lines can be separated in the funcion 'play'
    points = 0

    for i in range(question_number):
        country, capital = question_pool.pop()
        correct = ask(to_polish(country), to_polish(capital))
        if correct:
            points += 1
    #


    print(Fore.YELLOW + f"Uzyskałeś {points}/{question_number} punkty/ów")

if __name__ == "__main__":
    run()