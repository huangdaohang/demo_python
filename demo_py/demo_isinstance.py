class Person:
    def __init__(self,name):
        self.name = name
    
class Son(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age

s = Son("小明",20)
flag = isinstance(s,Person)
print(flag)
print(type(s))