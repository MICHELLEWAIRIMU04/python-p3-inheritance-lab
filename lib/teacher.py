#!/usr/bin/env python

from user import User

import random

KNOWLEDGE = [
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
    def __init__(self, first_name, last_name, knowledge=None):
        super().__init__(first_name, last_name)
        self.knowledge = knowledge if knowledge is not None else KNOWLEDGE.copy()
        

    def teach(self):
        index = random.randint(0, len(self.knowledge) - 1)
        return self.knowledge[index]
    
    def __str__(self):
        return f"Teacher: {self.first_name} {self.last_name}"

teacher = Teacher("Michelle", "Wairimu", KNOWLEDGE)
print(teacher)
print(teacher.teach())