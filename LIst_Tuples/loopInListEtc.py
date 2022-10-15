marks={'eng':100,'bng':90,'math':87,'chem':90}
numbers = [12,11,16,27,28,11,12]
nums={12,11,14,15,11,16}
num = 12,13,14,11,12,13

total = 0;
for i in numbers:
    total+=i
print(total)

for i in nums :
    total+=i
print(total)

for i in num :
    total+=i
print(total)

for mark in marks:
    print(mark)

for mark in marks:
    print(marks[mark])

for key,value in marks.items():
    print(key,value)

for i ,j in enumerate(numbers):
    print(i,j)