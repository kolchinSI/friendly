def bread(func):
     def wrapper():
         print("Булочка")
         func()
         print("<\Булочка/>")
     return wrapper

def ingredients(func):
    def wrapper():
        print("#помидоры#")
        func()
        print("~салат~")
    return wrapper

def sandwich(food="--ветчина--"):
    print(food)

@bread
@ingredients
def sandwich(food="--ветчина--"):
     print(food)

sandwich()


def incrementer():
    i = '1'
    while True :
        yield i
        i=i+'e'

inc = incrementer()
print(next(inc))
print(next(inc))
print(next(inc))
