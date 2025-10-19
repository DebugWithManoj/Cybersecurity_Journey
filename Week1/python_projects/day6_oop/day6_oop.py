class Student:
    
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def total(self):
        return sum(self.marks)
    def average(self):
        return self.total() / len(self.marks)
    
    def __str__(self):
        return (f"Student Name: {self.name}\n"
                f"Roll Number: {self.roll}\n"
                f"Marks: {self.marks}\n"
                f"Total Marks: {self.total()}\n"
                f"Average Marks: {self.average():.2f}\n"
                )

student1 = Student("Manoj", 101, [ 85, 90, 78 ])
student2 = Student("Amit", 102, [ 92, 88, 79 ])
print(student1)
print(student2)
