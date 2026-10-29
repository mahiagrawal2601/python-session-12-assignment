from functools import reduce

order_amounts = [120, 340, 560, 80]

total = reduce(lambda a,b : a + b, order_amounts)

print("Total bill amount:", total)