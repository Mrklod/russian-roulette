# Угадай число v1

import random

random_number = random.randint(1, 5)
user_number = input("Угадай число(от 1 до 5): ")

if int(user_number) == random_number:
    print("Поздравляю,вы угадали :)")
else:
   print ("Вы не угадали :( ")

print ("Было загадано:", random_number)