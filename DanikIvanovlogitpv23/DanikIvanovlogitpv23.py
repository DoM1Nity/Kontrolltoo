#Вариант 4
# задание 1


while True:
    try:
        n = int(input("Sisestage loomade arv (1 kuni 9):")) #спрашивает у пользавателя число от 1 до 9
        if 1 <=n<= 9: #проверяет, что введенное число находится в диапазоне от 1 до 9 
            break #завершает цикл, если введено корректное число.
        else: #если введенное число больше 9 выводит текст об ошибке
            print("Palun sisestage number 1 kuni 9")
    except ValueError: #выдает ошибку если человек вел вместо 1-9 , к примеру "10" или велл словами то выдаст ошибку и скажет "Palun sisestage õige number"
        print("Palun sisestage õige number")  


for i in range(n): #создает цикл, который выполняется n раз (у меня это от 1 до 9).
    print("  ^---^")
    print(" ( o o )")
    print("  ! = !/) ", end="") #выводит через пробел нового зверя
    # Печатаем пустой столбец после каждого зверька, кроме последнего
    if i < n - 1: #проверяет последний ли это зверь
        print() #просто пустая строчка для разрыва между ними 





##Задание 2
# Ввод числа n и показателя степени
try:
    n = int(input("Sisestage number n: ")) #n присвоеное число n (имеется ввиду которое впишет пользаватель)
    määr = int(input("Sisestage kraadi näitaja: ")) #Выполняет тоже самое действие что и прошлая строчка кода
except ValueError:
    print("Palun sisestage täisarvud.") 
   

for i in range(n * 100): #внутри цикла переменная i принимает значения от 1 до n * 10
    tulemus = i ** määr #tulemus это значение i в степени määr
    if tulemus > 100:  #если tulemus(результат) больше 100 то прервать цикл
        break 
    print(f"{i}^{määr} = {tulemus}")  # "f" используется для вставки значений переменных i, määr и tulemus внутрь строчки 







from random import randint

õppijate_arv = 15 #количество оценок
hinnang = []  #создаем пустой список оценок

for i in range(õppijate_arv):
    hinnang.append(randint(1, 12))  #добавляем оценки в список "append используется для добавления элемента в конец списка" подсмотрел в интернете

# Определение минимальной и максимальной оценок
minimaalne_hinnang = min(hinnang)  # нахождение минимальной оценки
maksimaalne_hinnang = max(hinnang)  # нахождение  максимальной оценки

# Вывод результатов
print(f"Õpilaste hinnangud: {hinnang}")  # Вывод списка оценок
print(f"minimaalne hinnang: {minimaalne_hinnang}")  #минимальная оценка
print(f"maksimaalne hinnang: {maksimaalne_hinnang}")  #максимальная оценка