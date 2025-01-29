#!/usr/bin/env python

from user import User

class Student(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = []

    def learn(self, new_knowledge):
        self.knowledge.append(new_knowledge)

    def __str__(self):
        return f"Student: my {self.first_name} {self.last_name}, knowledge: {', '.join(self.knowledge)}"

student = Student("ann", "kinyanjui")
#print(student)
student.learn("Python function call definition")
print(student)
        