class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def print_student(self):
        print(f"\n{self.name} is {self.age} years old, and is in the {self.grade} grade.")


class Staff:
    def __init__(self, name, department, role, salary):
        self.name = name
        self.department = department
        self.role = role
        self.salary = salary

class Teacher(Staff):
    def __init__(self, name, department, role, salary, age):
        super().__init__(name, department, role, salary)
        self.age = age

    def print_teacher(self):
        print(f"\n{self.name} is {self.age} years old, and has a {self.role} role in the {self.department} department, making ${self.salary} annually.")

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4

student1 = Student("bill", 42, 107)
student2 = Student("bob", 4, 107)
student1.print_student()
student2.print_student()

teacher1 = Teacher("billy", "accounting", "senior manager", 107000, 53)
teacher2 = Teacher("bobby", "cleaning", "temp", 54, 28)
teacher1.print_teacher()
teacher2.print_teacher()

square1 = Square(2)
print(f"\nThe area of square1 is {square1.area()}")
print(f"\nThe perimeter of square1 is {square1.perimeter()}")