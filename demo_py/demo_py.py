class Worker:
    work_time = 100

    def __init__(self,name):
        self.name = name
        self.__money = 2500
        self.hour = 0

    def doWork(self,hours):
        print(f"{self.name}已经加班{hours}小时")
        self.hour += hours
        Worker.work_time -= hours
        self.__money += hours * 10

    @property
    def myMoney(self):
        return self.__money

    @classmethod
    def add_work(cls,n):
        cls.work_time += n
        print(f"万恶的甲方又加了需求，现在还剩{Worker.work_time}小时才能完成")

    @staticmethod
    def func(num):
        print(f"这是一句没用的废话，{num}")
        print(Worker.work_time)

# if __name__ == "__main__":
#     w_dn = Worker("大牛")
#     # print(w_dn.__money)
#     # print(w_dn.name)
#     w_dn.doWork(10)
#     Worker.add_work(50)
#     Worker.func(5)

