start = int(input("Write starting point: "))
end = int(input("Write ending point: "))
sq_numbers = [i*i for i in range(start,end)]

#test
for i in sq_numbers:
    for j in range(start,end):
        if i/2 == j:
            print(i)
