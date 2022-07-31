import random

number = str(random.randint(100, 1000))
n = 0
k = 0
fermi = []
pico = []
bagels = []
print('''\n\t\t\t\t Это игра "Bagels"\
        \n\t\tПравила:\
        \n\t\t необходимо по подсказкам угадать число из трех цифр.\
        \n\t\t В ответ на ваши попытки игра выдает одну из трех подсказок:\
        \n\t\t Pico - если вы угадали правильную цифру на неправильном месте,\
        \n\t\t Fermi - если вы угадали число на правильном месте, Bagels - если вы не угадали цифру.\
        \n\t\t На все вам дается 10 попыток!\
        \n\t\t\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
        ''')

while k <= 3:
    if k == 3 and n <= 10:
        print(f"\nТы победил! Отгадал моё число {number}")
        break;
    elif k < 3 and n <= 10:
        while n <= 10:
            guess = input(f"\n\tУ тебя осталось {10 - n} попыток.\n\t Отгадай {k + 1}-ю цифру числа: ")
            if n <= 10:
                if guess == number[k]:
                    k += 1
                    fermi += guess
                    print("\nFermi")
                    print(f"\nFermi - {fermi} || Pico - {pico} || Bagels - {bagels}")
                    break;
                elif guess == number[k - 1] or guess == number[k - 2]:
                    n += 1
                    pico += guess
                    print("\nPico")
                else:
                    n += 1
                    bagels += guess
                    print("\nBagels")
                print(f"\nFermi - {fermi} || Pico - {pico} || Bagels - {bagels}")
            else:
                print("\nТы проиграл!")
    else:
        print("\nТы проиграл!!!!")
        break;


input("\n\nДля выхода нажмите Enter")