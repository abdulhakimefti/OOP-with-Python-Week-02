def create_new_string(s,a):
    output=""
    broken_s = s.replace(", ", " ").split(" ")
    for i in a:
        for index_j ,j in enumerate(broken_s) :
            if i.lower()==j.lower():
                output+=broken_s[index_j+1]+" "
    with open('out.txt','w') as fileWrite:
        fileWrite.write(output)
        fileWrite.close()

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."

create_new_string(s,a)

