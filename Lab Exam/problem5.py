x = { 'a' : 1, 'b' :  2, 'c': 3, 'd': 4}
d = {'!': 1, '@' : 2, '#': 3, '$' : 4, '%' : 5, '^' : 6}

x_list = []
d_list =[]

for key,value in x.items():
    x_list.append(key)
    x_list.append(value)

for key,value in d.items():
    d_list.append(key)
    d_list.append(value)

print(x_list)
print(d_list)