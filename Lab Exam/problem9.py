def  replace_word(s,replace_with):
    result = ""
    broken_s = s.split(" ")
    for index_j,j in enumerate(replace_with):
        for index_i ,i in enumerate(broken_s):
            if i == j and index_j%2==0  :
                broken_s[index_i]=replace_with[index_j+1]

    for i in broken_s:
        result+=i+" "
    return result


replace_with = ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."

result = replace_word(s,replace_with)
print(result)
