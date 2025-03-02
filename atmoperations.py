from atmexcep import *
bal=500
def deposit():
    dep=int(input("enter how many amount you want to deposit"))
    if(dep<=0):
        raise depositError
    else:
        global bal
        bal=bal+dep
        print("your account is credited with {}".format(dep))
        print("now your account balance is {}".format(bal))
def withdraw():
    global bal

    wp=int(input("enter how many amount you want to withdraw"))
    if(wp<=0):
        raise withdrawError
    elif(bal<=0):
        raise insufficientfundError
    else:

        bal = bal-wp
        print("your account is debited with {}".format(wp))
        print("now your account balance is {}".format(bal))
def checkbal():
    print("your account balance is {}".format(bal))

