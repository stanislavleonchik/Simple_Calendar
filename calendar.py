# Используя классы написать календарь,
# в котором будут отмечены праздничные дни.
# На выходе программы должен быть консольный
# вывод запрошенного месяца,в котором отмечены
# все праздники (дата и название)
from time import sleep


class Date:
    def __init__(self, y, m, d):
        self.year = y
        self.mon = m
        self.day = d
    def __repr__(self):
        return f"{self.day}.{self.mon}.{self.year}"
class Calendar():
    def __init__(self):
        self.holiday_list = {}
    def init_holiday(self):
        name = input("Введите название праздника\n")
        try:
            raw_date = [int(item) for item in input("Введите дату\n").split()]
            if raw_date[0] not in range(1,32) or raw_date[1] not in range(1,13) or raw_date[2] not in range(1,2031):
                raise
            date = Date(raw_date[0], raw_date[1], raw_date[2])
            self.holiday_list[date] = name
        except Exception:
            print("Неверный формат.")
    def is_holiday_in_month(self):
        try:
            month = int(input("Введите месяц\n"))
            if month not in range(1,13):
                raise
            for key in self.holiday_list.keys():
                if int(str(key).split('.')[1]) == month:
                    print(f"Праздник: {self.holiday_list[key]}\n"
                          f"Дата: {key}")
        except:
            print("Неверный формат")
    def menu(self):
        print('┌', " Меню ".center(51, '—'), '┐', sep='')
        print("│ •1 Добавить праздник в календарь                  │")
        print("│ •2 Вывести все праздники за месяц                 │")
        print("│ •3 Вывести все праздники                          │")
        print("│ •9 Вывести меню                                   │")
        print("│ •0 Выход                                          │")
        print('└', '—' * 51, '┘', sep='')
    def wtopa(self):
        self.menu()
        while True:
            try:
                try:
                    p = int(input('Введите номер пункта: '))
                except ValueError:
                    print("Введите цифру")
                    continue
                if p == 1:
                    self.init_holiday()
                elif p == 2:
                    self.is_holiday_in_month()
                elif p == 3:
                    for key, value in self.holiday_list.items():
                        print(f"Праздник: {value}\n"
                          f"Дата: {key}")
                elif p == 9:
                    # вывести меню;
                    self.menu()
                elif p == 0:
                    # выйти из программы;
                    print("Выход из программы", end='')
                    sleep(0.3)
                    for j in range(3):
                        print('.', end='')
                        sleep(0.25)
                    return
                else:
                    print("Нет такого пункта меню!\n")
                    sleep(1)
            except Exception as e:
                print('Ошибка: ', e)
Calendar = Calendar()
Calendar.wtopa()