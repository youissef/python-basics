
visit = int(input("enter the number of visitors: "))
request = int(input("enter the number of request: "))
def func(visit,request):
    persent = (visit / request)
    print(persent)
    if persent > 0.6:
        print("the client is fidele")
    else:
        print("the client is not fidele")  

func(visit,request)
