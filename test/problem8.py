def make_upper(st):
    output = ""
    for i in st:
        if ord(i) >= 97 and ord(i)<=120:
            output+=chr(ord(i)-32)
    return output

def make_lower(st):
    output = ""
    for i in st:
        if ord(i) >= 65 and ord(i)<=90 :
            output+=chr(ord(i)+32)
    return output
def make_capital(st):
    output = ""
    if ord(st[0])>=97 and ord(st[0])<=120:
        letter = ord(st[0])-32
        output=chr(letter)+st[1:]
    return output


