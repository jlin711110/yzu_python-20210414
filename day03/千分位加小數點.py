# 千分位 + 小數點
# -*- coding:UTF-8 -*-

n = 123 * 99 * 1234 * 1.2121212
print(n)
print("{:,}".format(n))
print("%.2f" % n)
print("{:,}".format(float("%.2f" % n)))
print(format(float("%.2f" % n), ","))