#1 задание
duration = int(input("Введите число для преобразования: ")) #Запрашиваем пользователя ввести инфо с клавы
if duration <= 60: #Самое простое - если число меньше 60 то просто выводим его
    print("до минуты:", duration ,"секунд")
elif duration > 60 and duration <= 3600: #Если число от 60 до 3600 вычисляем число минут и секунд и выводим
    duration_in_min = duration // 60
    duration_in_sec = duration - duration_in_min * 60
    print("до часа:", duration_in_min, "минут", duration_in_sec, "секунд")
elif duration > 3600 and duration <= 86400: #Если число от 3600 до 86400 вычисляем число часов, минут, секунд и выводим
    duration_in_hour = duration // 3600
    duration_in_min = (duration - duration_in_hour * 3600) // 60
    duration_in_sec = duration - duration_in_hour * 3600 - duration_in_min * 60
    print("до суток:", duration_in_hour, "часов", duration_in_min, "минут", duration_in_sec, "секунд")
else:#Для значений больше 86400 вычисляем все параметры
    duration_in_days = duration // 86400
    duration_in_hour = (duration - duration_in_days * 86400) // 3600
    duration_in_min = (duration - duration_in_days * 86400 - duration_in_hour * 3600) // 60
    duration_in_sec = duration - duration_in_days * 86400 - duration_in_hour * 3600 - duration_in_min * 60
    print("в остальных случаях:", duration_in_days, "дней", duration_in_hour, "часов", duration_in_min, "минут",
          duration_in_sec, "секунд")
