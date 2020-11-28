import colorama
from colorama import Fore
colorama.init()

class Colors():
    _all = [Fore.BLUE, Fore.GREEN, Fore.CYAN, Fore.YELLOW, Fore.RED]

class Strings():
    _all = ["[LOG]", "[WARN]", "[INFO]", "[ERROR]", "[SUCCESS]"]

class PYLog():
    _m = "[LOG]"
    _c = Fore.YELLOW


    def mode(mode):
        allcolor = Colors._all
        allstring = Strings._all

        if mode == "info":
            PYLog._c = allcolor[2]
            PYLog._m = allstring[2]
        elif mode == "error":
            PYLog._c = allcolor[4]
            PYLog._m = allstring[3]
        elif mode == "warn":
            PYLog._c = allcolor[0]
            PYLog._m = allstring[1]
        elif mode == "success":
            PYLog._c = allcolor[1]
            PYLog._m = allstring[4]
        else:
            PYLog._c = allcolor[3]
            PYLog._m = allstring[0]
        return PYLog._c, PYLog._m
        
    def log(m, text):
        mod = m # PYLog.mode(m)
        string = mod[1]
        color = mod[0]
        c = Fore.YELLOW
        return print(f"{color}{string} {c}{text}")

    def info(text):
        mod = PYLog.mode("info")
        string = mod[1]
        color = mod[0]
        c = Fore.YELLOW
        return print(f"{color}{string} {c}{text}")

    def error(text):
        mod = PYLog.mode("error")
        string = mod[1]
        color = mod[0]
        c = Fore.YELLOW
        return print(f"{color}{string} {c}{text}")

    def warn(text):
        mod = PYLog.mode("warn")
        string = mod[1]
        color = mod[0]
        c = Fore.YELLOW
        return print(f"{color}{string} {c}{text}")

    def success(text):
        mod = PYLog.mode("success")
        string = mod[1]
        color = mod[0]
        c = Fore.YELLOW
        return print(f"{color}{string} {c}{text}")

    def generic(text):
        mod = PYLog.mode("protogen")
        string = mod[1]
        color = mod[0]
        c = Fore.YELLOW
        return print(f"{color}{string} {c}{text}")
