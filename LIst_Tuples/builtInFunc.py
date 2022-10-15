numbers = [12,13,1,15,165,18,19,2,4];
print(max(numbers))
print(min(numbers))
print(len(numbers))
# print(ord(numbers))
st = 'kfjsafjdjfsk'
for i in st:
    print(ord(i))
print(list(reversed(numbers)))
print(list(sorted(numbers)))
print(list(sorted(numbers,reverse=True)))

actor = [{'name': 'sakib', 'age': 34},
         {'name': 'shabana', 'age': 64},
         {'name': 'banna', 'age': 100},
         {'name': 'riyaz', 'age': 44},
         {'name': 'jhankar', 'age': 37} ]

print(list(sorted(actor,key=lambda actor : actor ['age'])))
print(list(sorted(actor,key = lambda actor : actor ['name'])))