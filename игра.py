import os
import random

clear = lambda: os.system('cls')

print('Привет! Я загадал слово, твоя задача - угадать его по буквам')
input('*Нажмите enter чтобы продолжить*')
clear()
print('Поехали!')

words = ['пирожок', 'чебурек', 'огурец', 'сосиска', 'котик', 'квокка', 'корабль', 'самолет', 'автомобиль', 'дирижабль']
word = random.choice(words)

letters = []
isWin = True
hp = 10

while hp > 0:
    isWin = True
    print(letters)
    for symb in word:
        if symb in letters:
            print(symb, end=' ')
        else:
            print('*', end=' ')
            isWin = False
    print()

    if isWin:
        print('Ты угадал! Молодец!')
        break

    letter = input('Введите букву: ')
    letters.append(letter)
    clear()

    if letter not in word:
        hp -= 1
        print(f'Осталось попыток {hp}')

if hp == 0:
    print('Ты проиграл!')
