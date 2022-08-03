import random

# Глобальные переменные
number = ""  # загаданное число
tries = 0  # кол-во попыток
count_digits = 3  # кол-во цифр в числе
amount_tries = 10 #кол-во попыток
i = 0
while i < count_digits:
    numerical = str(random.randint(0, 9))
    if numerical not in number:
        number += numerical
        i += 1
print(f'Я загадал {count_digits}-x значное число. Попробуй угадать.\n')
while tries < amount_tries:
    tries += 1

    guess = input(f"попытка {tries}: \n> ")
    
    if tries == amount_tries and len(guess) != count_digits:
        print(f"\nТы использовал {tries} попыток. Ты проиграл! \nЯ загадал число = {number}")
        break
        
    if len(guess) != count_digits:
        continue

    if guess == number:
        print('Ты выиграл')
        break

    answers = []  # массив подсказок
    index = 0  # индекс ячейки в строчке
    while index < count_digits:

        if guess[index] == number[index]:
            answers.append('fermi')
        elif guess[index] in number:
            answers.append('pico')

        index += 1

    answers.sort()
    if answers:
        print(' '.join(answers))
    else:
        print('bagels')
      
    if tries == amount_tries:
        print(f"\nТы использовал {tries} потыток. Ты проиграл! \nЯ загадал число = {number}")



input("\n\nнажмите Enter")


