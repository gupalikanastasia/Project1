class Human:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def introduce(self):
        print(f"Привіт, я {self.name}, мені {self.__age} років.")

class Student(Human):
    def __init__(self, name, age, course):
        super().__init__(name, age)
        self.course = course

    def introduce(self):
        print(f"Привіт, я {self.name}, я студент {self.course}-го курсу.")


person = Human("Олег", 40)
student = Student("Марія", 19, 2)

person.introduce()
student.introduce()

print(person.get_age())