from random import sample


def lucky_numbers():
    """
    Checks the players numbers - checks type int, range between 1-50 or if the number isn't duplicated
    :return: list of 6 sorted from the smallest to the biggest numbers
    """
    numbers_list = []
    while len(numbers_list) < 6:
        try:
            choosen_number = int(input("Wybierz liczbę od 1-49:"))
            if choosen_number not in range(1, 50):
                print("Wartość musi znajdować się w przedziale 1-49!")
            elif choosen_number in numbers_list:
                print("Wartość nie może się powtórzyć!")
            else:
                numbers_list.append(choosen_number)
        except ValueError:
            print("Wartość niepoprawna!")
    return sorted(numbers_list)


def winning_numbers():
    """
    Get's numbers from lucky_numbers() funtion and comparing them with winning numbers.
    :return: str information of how many numbers the player had guessed
    """
    winning_list = sample(range(1, 50), 6)
    choosen_numbers = lucky_numbers()
    print(winning_list)
    print(choosen_numbers)
    result = len((set(winning_list)) & (set(choosen_numbers)))
    return f"You have guessed {result} numbers!"


if __name__ == '__main__':
    print(winning_numbers())
