#2 задание
numbers = list(range(1, 1000, 2)) # задаем список от 1 до n нечетных чисел
print(numbers)
list_2 = [] #создаем второй список в который будем записывать кубические числа
i = 0 #задаем порядковый номер 0
for i in numbers: #тоже что ниже только короче
    list_2.append(i ** 3)
# while i < len(numbers): #запускаем цикл пока переменная i меньше длинны списка (количества элементов)
    # number = numbers[i] ** 3 #присваиваем переменной number кубические значение текущего элемента 1го списка
    # list_2.append(number)  # записываем полученное число в новый список
    # i += 1 #идем к след переменной
print(list_2)
list_3 = [] #создаем третий список
i = 0 #обнуляем счетчик
while i < len(list_2): #запускаем цикл пока переменная i меньше длинны списка (количества элементов)
    number = list_2[i] #присваиваем переменной number значение текущего элемента 2го списка
    result = 0 #присваиваем переменно result (сумма цифр числа) значение 0
    x = number #присваиваем переменной x значение текущего числа из списка
    while x > 0: #цикл по условию
        digit = x % 10 #получаем цифру от деления x с остатком на 10
        result = result + digit #суммируем результат с полученной цифрой
        x = x // 10 #получаем новое число для дальнейшего цикла
    if result % 7 == 0: #условие если результат делится нацело на 7
        list_3.append(number) #записываем число по которому в данный момент идет цикл в новый список
    i += 1
print(list_3)
print(sum(list_3)) #суммируем элементы списка 3
list_4 = [] #Создаем 4ый список для значений 2го увеличенных на 17
for i in list_2:  #цикл приплюсовки 17 к значениям элемента 2го списка
    list_4.append(i+17)
print(list_4)
list_5 = [] #Создаем 5ый список для перебора значений сумма цифр которых делится на 7
i = 0 #обнуляем счетчик
while i < len(list_4): #запускаем цикл пока переменная i меньше длинны списка (количества элементов)
    number = list_4[i] #присваиваем переменной number значение текущего элемента 4го списка
    # print(number)
    result = 0 #присваиваем переменно result (сумма цифр числа) значение 0
    x = number #присваиваем переменной x значение текущего числа из списка
    while x > 0: #цикл по условию
        digit = x % 10 #получаем цифру от деления x с остатком на 10
        result = result + digit #суммируем результат с полученной цифрой
        x = x // 10 #получаем новое число для дальнейшего цикла
    if result % 7 == 0: #условие если результат делится нацело на 7
        list_5.append(number) #записываем число по которому в данный момент идет цикл в новый список
    i += 1
print(list_5)
print(sum(list_5)) #суммируем элементы списка 5




