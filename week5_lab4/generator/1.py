
n = int(input("write number: "))
sq_numbers = (i*i for i in range(1,n))
print(sq_numbers)
for i in sq_numbers:
    print(i)