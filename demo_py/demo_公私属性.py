class PropertyTest:
    name = "张三"
    age = 20

    def func(self,s):
        # 此处相当于初始化了一个name的实例属性
        self.name = s

    def func2(self):
        # 不调用func()前直接访问self.name,获取到的是公共属性
        # 调用func()后再访问self.name,获取到的就是实例属性
        print(self.name)

p = PropertyTest()
# p.func("李四")
p.func2()

# print(PropertyTest.name)
# print(p.name)

# print(PropertyTest.__dict__)
# print(p.__dict__)