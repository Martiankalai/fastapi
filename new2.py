def func():
    for i in range(5):
        yield i


for i in func():
    print(i)
