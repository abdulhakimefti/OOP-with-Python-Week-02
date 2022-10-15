numbers = [11, 12, 13, 15, 16, 18]
# def double_it (num):
#     return num*2


def double_it(num): return num*2


print(double_it(88))

number_d = list(map(double_it, numbers))
print(number_d)

filtered = list(filter(lambda x: x > 23, number_d))
print(filtered)


actor = [{'name': 'sakib', 'age': 34},
         {'name': 'shabana', 'age': 64},
         {'name': 'banna', 'age': 100},
         {'name': 'riyaz', 'age': 44},
         {'name': 'jhankar', 'age': 37} ]

print(actor)

actors_jr = list(filter(lambda actor : actor['age']<50,actor))
print(actors_jr)