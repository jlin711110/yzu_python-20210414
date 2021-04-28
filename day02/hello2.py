# -*- coding:UTF-8 -*-

chinese = '100'  # str
english = "90"  # str
math = 80  # int
print(chinese, english, math)
print(type(chinese), type(english), type(math))
sum = int(chinese) + int(english) + math
stream = chinese + english + str(math)
print(sum)
print("總分:" + str(sum))
print("總分:", sum)
print(stream)