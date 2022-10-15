with open('massage.txt','a') as filewrite:
    filewrite.write('Hello from python')

with open('massage.txt','r') as fileread:
    text = fileread.read()
    print(text)

# def display_person(*args):
#     for i in args:
#         print(i)

# display_person(name="Rahat", age="25")
def foo():
    try:
        return 1
    finally:
        return 2
k = foo()
print(k)