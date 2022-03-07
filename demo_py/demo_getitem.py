class DataTest:
    def __init__(self,num):
        self.num = num

    def __getitem__(self,index):
        if index < self.num:
            return f"这是索引{index}所指向的元素"
        else:
            raise StopIteration

data = DataTest(20)
for i in data:
    print(i)

print("遍历结束")
print("---------")
print(data[0])
# print(data[15])
# print(data[19])

for i in data:
    print(i)