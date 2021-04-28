# -*- coding:UTF-8 -*-

account = 10000000  # 帳戶資金
stock = "台積電"  # 標的
price = 590.5  # 成交價
amount = 5432  # 股數
tax_ratio = 1.425/1000
fee_ratio = 3/1000

# 買入成本
cost = price * amount * (1 + tax_ratio)
# 帳戶剩餘資金
account = account - cost
print("成本 \t\t", "帳戶餘額")
print("%.1f" %cost,"\t", "%.1f" %account)
print("成本", cost)  # 預設的sep=" ", end=".\n"
print("成本", cost, sep="=", end=".\n")
# %f(浮點數) %d(整數) %(字串)
print("成本: %.1f" %cost)
# 欲印出 買進 台積點 5432 股 花費成本 $ 3212166.8 帳戶餘額 $ 6787833.2
print("買進 %s %d 股, 花費成本 $ %.1f, 帳戶餘額 $ %.1f" %(stock, amount, cost, account))
print("買進 %s %d 股, 花費成本 $ %.1f, 帳戶餘額 $ %s" %(stock, amount, cost, format(account, ',')))
print("買進 %s %d 股, 花費成本 $ %s, 帳戶餘額 $ %s" %(stock, amount, format(int(cost*10)/10, ','), format(account, ',')))
print("帳戶餘額 $ %s" % format(int(cost*10)/10, ','))

# 不足補 0
rate1 = 2.32
rate2 = 32.123
rate3 = 641.567
print("%09.4f" % rate1)
print("%09.5f" % rate2)
print("%07.5f" % rate3)