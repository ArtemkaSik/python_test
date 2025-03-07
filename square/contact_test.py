from contact import Contact

# Создаём экземпляр класса Contact
mike = Contact('Михаил Булгаков', 1891, False)

# Заготавливаем строку, которую по ожиданию должен вернуть метод show_contact():
expected_string = 'Михаил Булгаков, категория: Старейшина, статус: Нормальный'

# Пишем утверждение: 
# "вызов метода show_contact объекта mike вернёт строку, сохранённую в expected_string"
assert mike.show_contact() == expected_string, 'Метод show_contact работает некорректно!'