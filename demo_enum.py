from enum import Enum

class Color(Enum):
    red = 1
    green = 2
    blue = 3

# print(Color.red)
# print(Color["red"])
# print(Color(1))

# print(Color.red.value)
# print(Color.red.name)

for name,member in Color.__members__.items():
    print(name,member)

# for color in Color:
#     print(color)

Gender = Enum("Gender",("MALE","FEMALE","OTHER"))
# print(Gender.FEMALE)
# print(Gender.MALE.name)
# print(Gender.FEMALE.value)
# print(Gender(1))
# for sex in Gender:
#     print(sex)
for name,member in Gender.__members__.items():
    print(name,member)