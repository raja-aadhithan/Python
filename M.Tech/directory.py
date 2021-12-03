#directory

def update():
    name = 'obj_{}'.format(len(my_objects))
    nam = input("Enter Contacts Name: ")
    num =  input("Enter Contacts Mobile no: ")
    email = input("Enter Email: ")
    age = input("Enter Age: ")
    my_objects[name] = my_objects.get(name, person(nam, num, email, age))

def print_menu():
    print('\n\n\n\n Menu: \n')
    print('1. Print Details')
    print('2. Add a Contact')
    print('3. Remove a Contact ')
    print('4. Show all contacts ')
    print('5. Lookup a Phone Number')
    print('6. Update a Contact')
    print('To quit enter any other number')
    choice = input('Enter a Choice from 1 to 6: ')
    try:
        choice = int(choice)
        if(choice >= 1 and choice < 7):
            return(choice)
        else:
            print('Quitting')
    except:
        print('Invalid choice')
    

class person:
    def __init__(self, name, mobile_no, email, age):
        self.name = name 
        self.mobile_no = mobile_no
        self.email = email
        self.age = age
    def show(self):
        print('\t Contact :',self.name,'\n\t Mobile no:',self.mobile_no,'\n\t Email:',self.email,'\n\t Age:',self.age)

def call(chosen):
    state_machine(chosen)

def state_machine(chosen):
    if(chosen == 1):
        contact = input('Enter the name of the contact: ')
        for i in my_objects:
            if my_objects[i].name == contact:
                print('Contact Exists')
                no = input('Enter Details needed: \n\t 1. Mobile no \n\t 2. Email \n\t 3. Age \n\t 4. All \n')
                if (no == '1' or no == 'mobile_no' or no == 'Mobile_no'or no == 'Mobile'or no == 'mobile'):
                    print(my_objects[i].mobile_no)
                elif (no == '2' or no == 'email' or no == 'Email'or no == 'mail'):
                    print(my_objects[i].email)
                elif (no == '3' or no == 'age' or no == 'Age'):
                    print(my_objects[i].age)
                elif (no == '4' or no == 'all' or no == 'All'):
                    my_objects[i].show()
                else:
                    print('not a valid option')
        chosen = print_menu()
        call(chosen)


    elif(chosen == 2):
        update()
        chosen = print_menu()
        call(chosen)

    elif(chosen == 3):
        sample = input('Enter Contact name: ')
        for i in my_objects:
            if my_objects[i].name == sample:
                val = i;
        del my_objects[val]
        chosen = print_menu()
        call(chosen)

    elif(chosen == 4):
        for x in my_objects:
            print(my_objects[x].name)
        chosen = print_menu()
        call(chosen)
    
    elif(chosen == 5):
        sample = input('Enter phone number ')
        try: 
            sample = int(sample)
            for i in my_objects:
                if my_objects[i].mobile_no == sample:
                    print('Contact Name: ',my_objects[i].name)
        except:
            print('Enter valid number')
        chosen = print_menu()
        call(chosen)

    elif(chosen == 6):
        sample = input('Enter Contact name: ')
        for i in my_objects:
            if my_objects[i].name == sample:
                    opt = int(input('1. To update Mobile number \n2.To update Email \n3. To change age  '))
                    if(opt == 1):
                        my_objects[i].mobile_no = int(input('Enter New Number '))
                    if(opt == 2):
                        my_objects[i].email = input('Enter Mail ID ')
                    if(opt == 3):
                        my_objects[i].age = int(input('Enter Age '))
                        print(my_objects[i].age)
        chosen = print_menu()
        call(chosen)


my_objects = {}
name = 'obj_{}'.format(0)
my_objects[name] = my_objects.get(name, person("Aadhi",7639686939,"raja.aadhithan.t@gmail.com",22))
name = 'obj_{}'.format(1)
my_objects[name] = my_objects.get(name, person("Navi",9080637090,"transidharth@gmail.com",20))
name = 'obj_{}'.format(2)
my_objects[name] = my_objects.get(name, person("Peri",9393453452,"peri_start@gmail.com",34))
name = 'obj_{}'.format(3)
my_objects[name] = my_objects.get(name, person("hawkeye",9231220211,"hwkweye@gmail.com",15))


chosen = print_menu()
state_machine(chosen)
