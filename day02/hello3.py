# -*- coding:UTF-8 -*-

# 隨機亂數
import random
n = random.randrange(0, 5)  # 0 <= n <5
print(n)
r = random.randint(0, 5)  # 0 <= n <=5
print(r)
f = random.randint(10, 200)  # 0 <= n <=5
print(f/100)

# 四星彩電腦選號
n1 = random.randint(0, 9)
n2 = random.randint(0, 9)
n3 = random.randint(0, 9)
n4 = random.randint(0, 9)
print(n1, n2, n3, n4, "\n")

# 跳脫字元
print("小明,\n明天\t要跟\"小英\"結婚了")
# 想要印出: 小明,\n明天\t要跟\"小英\"結婚了
print("小明,\\n明天\\t要跟\\\"小英\\\"結婚了")
print(n1 + n2 \
       + n3 + n4,)
