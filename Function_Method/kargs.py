def fullName (fName,lName):
    name = f'{fName} {lName}'
    return name

name = fullName('Abdul','Hakim')
print(name)

def longName(**kargs):
    print(kargs)

longName(first='Engr. ',last='Abdul ',lastAgain='Hakim')


def longNameOfMine(podobi,*arg,**kargs):
    print(podobi)
    print(arg)
    print(kargs)
    for key,valu in kargs.items():
        print(key,valu)
    
longNameOfMine('Engr. ','Abdul','Hakim','Efty',Undergred='BSC in CSE',greduation='MSC in CSE',PHd ='AI')