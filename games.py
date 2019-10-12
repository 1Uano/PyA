def ask_yes_no(question):
    """Задает вопрос с ответом (у/п)"""
    response = None
    while response not in ("y", "n"):
        response = input(question + ' (y/n)? ').lower()

def ask_number(question, low, high):
    """Просит ввести число из заданного диапазона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == '__main__':
    print("Вы запустили модуль games, а не импортирован его (import games).")
    input("\n\nНажмите Enter, чтобы выйти")