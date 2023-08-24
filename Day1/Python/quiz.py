my_number = 5
value = int(input("What number am I thinking of?"))

while(value != my_number):
    if value > my_number:
        print('Too high')
    else:
        print('Too low')
    
    value = int(input('Try again!'))
    
print('Yes!')