from time import sleep as t;
from colorama import Fore
import os;

print(Fore.BLACK + 'BLACK')
print(Fore.BLUE + 'BLUE')
print(Fore.CYAN + 'CYAN')
print(Fore.GREEN + 'GREEN')
print(Fore.LIGHTBLACK_EX + 'LIGHTBLACK_EX')
print(Fore.LIGHTBLUE_EX + 'LIGHTBLUE_EX')
print(Fore.LIGHTCYAN_EX + 'LIGHTCYAN_EX')
print(Fore.LIGHTGREEN_EX + 'LIGHTGREEN_EX')
print(Fore.LIGHTMAGENTA_EX + 'LIGHTMAGENTA_EX')
print(Fore.LIGHTRED_EX + 'LIGHTRED_EX')
print(Fore.LIGHTWHITE_EX + 'LIGHTWHITE_EX')
print(Fore.LIGHTYELLOW_EX + 'LIGHTYELLOW_EX')
print(Fore.MAGENTA + 'MAGENTA')
print(Fore.RED + 'RED')
print(Fore.RESET + 'RESET')
print(Fore.YELLOW + 'YELLOW')
print(Fore.WHITE + 'WHITE')
print("")

I=0
z=0
x=0
y=0

while True:
    I+=1
    y+=1
    print(Fore.GREEN + str(I)+"   "+ Fore.MAGENTA +str(y))
    if I==10:
        I=0
        x+=1
    if x==10:
        z+=1
        x=0
        y=0
        os.system('cls')
        print(Fore.LIGHTRED_EX +str(z)+"\n")
    t(0.1)