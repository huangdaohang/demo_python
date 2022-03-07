class Fib:
    def __init__(self,num):
        self.num = num
        self.recorder = 0
        self.a,self.b = 0,1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        self.recorder += 1
        if self.recorder >= self.num:
            raise StopIteration()
        return self.a

it = Fib(10)
for j in it:
    print(j)
for i in it:
    print(i)
# for i in range(5):
#     print(next(it))

# for j in range(10):
#     print(next(it))
