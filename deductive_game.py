import random

number = str(random.randint(100, 1000))

print(number)

i = 0
n = 0
k = 0
pico = []
bagels = []
while i < 3:
    i += 1
    k += 1
    while n < 10:
        guess = input(f"отгадай {k}-ю цифру числа: ")
        n += 1
        if n < 10:
            if guess == number[k - 1] :
                print("\nFermi")
                break;
            elif guess == number[k] or guess == number[k + 1]:
                pico += guess
                print("\nPico")
            else:
                bagels += guess
                print("\nBagels")
            print(f"\nPico - {pico}, Bagels - {bagels}")
        else:
            print("\nТы проиграл!")
# print("\nТы победил!")
input("\n\nДля выхода нажмите Enter")