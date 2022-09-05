import config
from time import sleep
from colorama import Fore, Style, init
init()

r = Fore.RED + Style.BRIGHT
y = Fore.YELLOW + Style.BRIGHT
c = Fore.CYAN + Style.BRIGHT
g = Fore.GREEN + Style.BRIGHT
m = Fore.MAGENTA + Style.BRIGHT
reset_all = Fore.RESET
print(r + config.tegs, y + config.text)

for names in c + "\nВведите свое имя":
	print(names, end="", flush=True)
	sleep(00.03)
name = input(" >> ")

for years in c + "Введите свой возраст":
	print(years, end="", flush=True)
	sleep(00.03)
year = int(input(" >> "))

if year >= 18:
	for i in g + "Вход разрешен!\n":
		print(i, end="", flush=True)
		sleep(00.03)
	for n in (f"Добро пожаловать, {m} {name}!"):
		print(n, end="", flush=True)
		sleep(00.03)

else:
	for no in r + "Вход запрещен!":
		print(no, end="", flush=True)
		sleep(00.03)
	print(reset_all)