numbers = [i ** 3 for i in range(1, 1000, 2)] #Задание сразу списка из кубов
list_2 = [] #создаем третий список
i = 0 #обнуляем счетчик
while i < len(numbers): #запускаем цикл пока переменная i меньше длинны списка (количества элементов)
    number = numbers[i] #присваиваем переменной number значение текущего элемента 2го списка
    result = 0 #присваиваем переменно result (сумма цифр числа) значение 0
    x = number #присваиваем переменной x значение текущего числа из списка
    while x > 0: #цикл по условию
        digit = x % 10 #получаем цифру от деления x с остатком на 10
        result = result + digit #суммируем результат с полученной цифрой
        x = x // 10 #получаем новое число для дальнейшего цикла
    if result % 7 == 0: #условие если результат делится нацело на 7
        list_2.append(number) #записываем число по которому в данный момент идет цикл в новый список
    i += 1
print(sum(list_2)) #суммируем элементы списка 3
list_3 = [] #Создаем 4ый список для значений 2го увеличенных на 17
for i in numbers:  #цикл приплюсовки 17 к значениям элемента 2го списка
    list_3.append(i+17)
list_4 = [] #Создаем 5ый список для перебора значений сумма цифр которых делится на 7
i = 0 #обнуляем счетчик
while i < len(list_3): #запускаем цикл пока переменная i меньше длинны списка (количества элементов)
    number = list_3[i] #присваиваем переменной number значение текущего элемента 4го списка
    result = 0 #присваиваем переменно result (сумма цифр числа) значение 0
    x = number #присваиваем переменной x значение текущего числа из списка
    while x > 0: #цикл по условию
        digit = x % 10 #получаем цифру от деления x с остатком на 10
        result = result + digit #суммируем результат с полученной цифрой
        x = x // 10 #получаем новое число для дальнейшего цикла
    if result % 7 == 0: #условие если результат делится нацело на 7
        list_4.append(number) #записываем число по которому в данный момент идет цикл в новый список
    i += 1
print(sum(list_4)) #суммируем элементы списка 5




