# Первое
lst = [92, 91, 49, 87, 74, 20, 94, 12, 64, 36, 97, 2, 96, 40, 97, 36, 32, 22, 80, 83, 49, 52, 62, 31,
55, 86, 84, 1, 22, 15, 52, 18, 78, 92, 21, 9, 85, 89, 54, 99, 80, 7, 4, 31, 30, 28, 59, 35, 72, 33]
dic=dict(enumerate(lst))
print(dic)

# Второе
import random

guess_number=0

number=random.randint(1, 20)

while guess_number<6:
    guess=int(input("Введите число:"))

    guess_number+=1
    if guess<number:
        print("Слишком мало!")

    if guess>number:
        print("Слишком много!")

    if guess == number:
        break
if guess == number:
    print("Класс! Вы угадали.")
elif guess > 5:
    print("Все, вы не выиграли.Игра завершилась")

# Третий
some_string="Adverts"
some=some_string[2:5]
print(some)

a="Adilet"
b="Aidana"

# Четвертый
c=a[0]+b[0]+b[1]+a[1]+b[2]+a[2]+b[3]+a[3]+b[4]+a[4]+b[5]+a[5]
print(c)
