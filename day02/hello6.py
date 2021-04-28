# -*- coding:UTF-8 -*-

import math

print(math.pow(2, 3))  # 2**3
print(math.sqrt(4))  # 平方根

x1, y1 = 10, 20
x2, y2 = 15, 45

# 求兩點間的距離
X= math.pow((x2-x1),2)
Y= math.pow((y2-y1),2)
print(math.sqrt(X + Y))
x3= x2-x1
y3= y2-y1
print(math.sqrt(math.pow(x3, 2) + math.pow(y3, 2)))

