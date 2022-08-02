import random

number = ""
i = 0
k = 0
while i < 3:
    numerical = str(random.randint(0, 9))
    if numerical not in number:
        number += numerical
        i += 1
print(number)
while k < 10:
    guess = " "
    answer = ["", "", ""]
    k += 1
    n = 0
    while len(guess) != 3:
        guess = input(f"попытка {k}: \n> ")
    while n < 3:
        for m in guess:
            if m == number[n]:
                answer[n] += "fermi"
                n += 1
            elif guess[n] == number[n - 1]: 
                answer[n] += "pico"
                n += 1
            elif guess[n] == number[n - 2]:
                answer[n] += "pico"
                n += 1
            else:
                answer[n] += "bagels"
                n += 1
    print(answer)
    if k == 10:
        print("Ты проиграл!")
    if answer[0] == answer[1] == answer[2] == "fermi":
        print("Ты победил!")
        k = 10

    
input("\n\nнажмите Enter")


