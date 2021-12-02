#directory

def print_menu():
    print('1. Print Phone Numbers')
    print('2. Add a Phone Number')
    print('3. Remove a Phone Number')
    print('4. Lookup a Phone Number')
    print('5. Quit')

numbers ={}
menu_choice = 0
print_menu()
while menu_choice != 5:
    menu_choice = int(input("Enter choice from 1 to 5"))
    if(menu_choice == 1):
        