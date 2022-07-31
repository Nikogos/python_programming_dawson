import random

number = ""
i = 0

while i < 3:
    numerical = str(random.randint(0,9))
    if numerical not in number:
        number += numerical
        i += 1


print(number)
input("\n\nнажмите Enter")