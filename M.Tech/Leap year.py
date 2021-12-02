x = input('Enter year  ')
try :
    x = int(x)
    if x%4 == 0 and x%100 != 0:
        print('Its a Leap year')
    elif x%400 == 0:
        print('Its a Leap year')
    else:
        print('Its not a Leap year') 
except:
    print('Year entered is invalid')