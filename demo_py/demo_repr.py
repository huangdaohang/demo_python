class Person:
    def __init__(self,name):
        self.name = name

    # def __repr__(self):
    #     return f"我的名字叫{self.name}"

    def __str__(self):
        return f"我的名字叫{self.name}"

    __repr__ = __str__

p = Person("李四")
print(str(p))
print(repr(p))

strs = "hello word \n"
print(strs)
print(111111)
print(repr(strs))
print(11111)