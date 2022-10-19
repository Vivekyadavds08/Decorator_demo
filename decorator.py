def decor(num):
    def inner():
        add = num()
        add = add + 5
        return add
    return inner
@decor

def num():
    return 10
print(num())
