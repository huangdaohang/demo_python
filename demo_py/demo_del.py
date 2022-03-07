# class CLanguage:
#     def __init__(self):
#         print("调用构造函数")

#     def __del__(self):
#         print("调用析构函数")

# clangs = CLanguage()
# # cl = clangs
# del clangs
# print("*********")
# # del cl
# # print("---------")

class Base:
    def __init__(self):
        self.name = "张三"
        self.age = 20
        print("调用父类初始化方法")

    def __del__(self):
        print("调用父类清理方法")
    
class Son(Base):
    def __del__(self):
        # super().__del__()
        print("调用子类清理方法")

s = Son()
del s
# print(s.name)