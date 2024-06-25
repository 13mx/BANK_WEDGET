from datetime import datetime


def get_data(date_string):
    # Преобразование строки в объект datetime
    date_obj = datetime.strptime(date_string, "%Y-%m-%dT%H:%M:%S.%f")
    # Возвращение строки с датой в формате dd.mm.yyyy
    return date_obj.strftime("%d.%m.%Y")


# Пример использования
print(get_data("2018-07-11T02:26:18.671407"))
