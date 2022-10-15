import pyjokes

def tell_some_jokes() :
    print(pyjokes.get_joke())

isMore = True
while(isMore):
    print("\n")
    tell_some_jokes()
    print("\n")
    isMore = input("To More Joke Write 'True'\nTo stop Wirte 'False'\n\n")