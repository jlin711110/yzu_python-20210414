# -*- coding:UTF-8 -*-

h=1.73
w=90
BMI=w/(h*h)
bmi=w/(h**2)
print("H=",h,"; \nW=",w,"; \nBMI=",BMI, ";\nbmi= %.2f" %bmi)

print(5/2)
print(5//2)  # 整除
print(5%2)  # 餘數


num = 1234567
if num%2 == 0:
    print("偶數")
else:
    print("奇數")