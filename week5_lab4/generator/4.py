def squares(a, b):
    for i in range(a, b):
        yield i ** 2


s = squares(int(input()), int(input()))

for i in s:
    print(i)  # i is yielded value
