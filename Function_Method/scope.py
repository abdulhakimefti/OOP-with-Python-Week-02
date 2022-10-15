
balance = 100
def totalCost(price,quantity):
    global balance
    cost = price * quantity
    balance = balance-cost
    return cost

pay = totalCost(10,15);
print(f'Please pay {pay},Now balance is {balance}')
#We can't access cost in here
