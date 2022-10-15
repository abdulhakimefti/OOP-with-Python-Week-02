l = ["This", "is", "very", "fantastic"]

def create_string(l):
    st = ""
    for i in l:
       st+=i+" " 
    return st

st = create_string(l)
print(st)
