def posneg(number):
    number = input("enter a number:\n")
    try: 
        number = int(number)
        if number<0: print("number is negative")
        elif number>0:  print("number is positive \U0001f60D")
        elif number == 0 : print ("number is zero")
    except: print("this is not even a number \U0001f612 \U0001f612 \U0001f612 \U0001f612")
posneg("s")