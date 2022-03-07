class Student:
    __slots__ = ("name", "age")

s = Student()
s.name = "张三"
s.age = 18
# s.score = 90

from types import MethodType

def set_score(self,score):
    self.score = score

Student.set_score = set_score
print(Student.__dict__)