print('     Welcome to')
print('╔╗──╔══╗╔══╗─────╔╗')
print('║║──║╔╗║║╔╗║────╔╝║')
print('║║──║╚╝║║╚╝╚╗───╚╗║')
print('║║──║╔╗║║╔═╗║────║║')
print('║╚═╗║║║║║╚═╝║────║║')
print('╚══╝╚╝╚╝╚═══╝────╚╝')
print(
    
)
print('---------------------------------')
task  = int(input('Write the task you want to choose\n     𝟙   𝟚   𝟛   𝟜   𝟝   𝟞\n---------------------------------\n'))


if(task == 1):
#T1 print and format
    print('---------------------------------')
    x = input("Write your name\n---------------------------------\n")
    print("\nHello {}\n".format(x))

if(task == 2):
#T2 numbers
    print('---------------------------------')
    number = input("Write a number\n---------------------------------\n")
    print('---------------------------------')
    number_type = input("Write the type to translate\n   Float     Complex\n---------------------------------\n")
    if(number_type.lower() == "float"):
        print('\nNow your number is float type:',float(number))
    else:
        print('\nNow your number is complex type:',complex(number))

if(task == 3):
#T3 variable 
    x1 = ["apple", "banana", "kiwi"]
    print('---------------------------------')
    x = input("write a color to receive a gift\n   Red    Yellow    Green\n---------------------------------\n")
    if( 'red' == x.lower()):
        print('\nYou get:',x1[0])
    elif( 'yellow' == x.lower()):
        print('\nYou get:',x1[1])
    elif( 'green' == x.lower()):
        print('\nYou get:',x1[2])

if(task == 4):
#T4 True or not true
    print('---------------------------------')
    x = int(input("True or not True\nWrite  𝟘  or  𝟙\n---------------------------------\n"))
    print("\n",bool(x))

if(task == 5):
#T5 string 
    print('---------------------------------')
    x =  input("Write any word\n---------------------------------\n")
    print()
    for i in x:
        print(i.upper())
        print("-")
    print("Length of the word: {}".format(len(x)))

if(task == 6):
#T6 calculator
    print('---------------------------------\nSimple calculator\n---------------------------------')
    a = input("First number:\n")
    b = input("Second number:\n")
    print('---------------------------------')
    x =  input("Write the type of operation\nAddition  Subtraction  Multiplication\nDivision  Modulus      Exponentiation\n---------------------------------\n")
    if(x.lower() == "addition"):
        print("\nYour result:",int(a)+int(b))
    elif(x.lower() == "subtraction"):
        print("\nYour result:",int(a)-int(b))
    elif(x.lower() == "multiplication"):
        print("\nYour result:",int(a)*int(b))
    elif(x.lower() == "division"):
        print("\nYour result:",int(a)/int(b))
    elif(x.lower() == "modulus"):
        print("\nYour result:",int(a)%int(b))
    elif(x.lower() == "exponentiation"):
        print("\nYour result:",int(a)**int(b))
    