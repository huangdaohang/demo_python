from types import MethodType
# 定义一个空类
class Student:
    pass

# 实例化一个对象
s = Student()
# 用动态绑定的方式向对象s中赋值
s.name = "张三"
print(s.name)
# 查看对象的成员
print(s.__dict__)

# 定义一个成员函数
def set_age(self,age):
    self.age = age

# 将函数set_age绑定给对象s，注意：仅仅是绑定给对象s而不是类Student
s.set_age = MethodType(set_age,s)

s.set_age(25)
print(s.age)
# print(s.__dict__)

s2 = Student()
# s2.set_age(25)  # 报错，set_age函数没有绑定给s2，所以s2中没有这个函数
# print(s2.age)

def set_score(self,score):
    self.score = score

# 将函数set_score赋值给类Student，这样所有的对象都可以使用
Student.set_score = set_score
# print(Student.__dict__)

s.set_score(99)
s2.set_score(100)
print(s.score)
print(s2.score)
