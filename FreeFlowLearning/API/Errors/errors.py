from colorama import Fore, Back


class Error:
    def __init__(self, msg, level):
        char = ''
        if level > 2:
            for i in range(level-2):
                char += Back.RED + Fore.BLACK + "!" + Fore.RESET + Back.RESET
        if level == 1:
            char += Fore.YELLOW
        if level >= 2:
            char += Fore.RED
        print(char, msg, Fore.RESET)
