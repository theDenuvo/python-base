# Задача-3: Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

#dist
number = input("Enter month number: ")
season = {
    "1": "winter",
    "2": "winter",
    "3": "spring",
    "4": "spring",
    "5": "spring",
    "6": "summer",
    "7": "summer",
    "8": "summer",
    "9": "autumn",
    "10": "autumn",
    "11": "autumn",
    "12": "winter",
}
print(season.get(number))

#list
season_list = ('winter', 'winter', 'spring', 'spring', 'spring', "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter",)
print(season_list[int(number) - 1])
