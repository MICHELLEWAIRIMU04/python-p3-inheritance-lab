#!/usr/bin/env python

from user import User

import random

knowledge = [
        "str is a data type in Python",
        "programming is hard, but it's worth it",
        "JavaScript async web request",
        "Python function call definition",
        "object-oriented teacher instance",
        "programming computers hacking learning terminal",
        "pipenv install pipenv shell",
        "pytest -x flag to fail fast",
    ]
class Teacher(User):
    def __init__(self, first_name, last_name, knowledge):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge

    def teach(self):
        index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[index]
    
    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"

teacher = Teacher("Michelle", "Wairimu", knowledge)
print(teacher)
print(teacher.teach())