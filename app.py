class Student:

    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def show_info(self):
        print(f"Ім'я: {self.name}, Вік: {self.age}, Курс: {self.course}")

    def change_course(self, new_course):
        self.course = new_course

student1 = Student("Іван", 18, 1)
student2 = Student("Анна", 19, 2)

student1.show_info()
student2.show_info()

student1.change_course(2)
student1.show_info()

class Task:

    def __init__(self, title):
        self.title = title
        self.completed = False

    def mark_done(self):
        self.completed = True


tasks_list = [
    Task("Повторититеорію"),
    Task("Написати код"),
    Task("Здати роботу"),
]

for task in tasks_list:
    print(f"Завдання: {task.title}, Статус: {task.completed}")


class Event:

    def __init__(self, title, date):
        self.title = title
        self.date = date
        self.description = ""

    def show(self):
        print(f"Подія: {self.title}, Дата: {self.date}, Опис: {self.description}")

    def update_description(self, new_description):
        self.description = new_description


event1 = Event("Вебінар", "20.07.2026")
event1.update_description("Лекція про декоратори")
event1.show()