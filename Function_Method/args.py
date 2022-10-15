def add (num1,num2):
    total = num1 + num2
    print(total)
    return total
result = add (num2=12,num1=14)

def multiple (num1,num2=2):
    total = num1*num2
    return total
result = multiple(10)
print(result)

def multiple2(*num):
    total = 1
    for n in num:
        total *=n
    return total;
print(multiple2(2,3,4,5))

def add (num1,num2,*number):
    print(num1,num2)
    print(number)
    total =1
    for n in number :
        total = n + total
    return total

print(add(5,4,6,7,32,63))