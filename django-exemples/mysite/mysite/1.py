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

lst1=[1,1,2,5,8,7,46,5]
lst2=[8,7]
print([x * y for x in lst1 for y in lst2])