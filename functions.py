def greet():
    print("Hello")

greet()

def add(a,b):
    sum = a+b
    diff = a-b
    return sum,diff


r,d = add(80,80)

print(r,d)

def update(x):
    x = 90
    print(x)

update(32)

f=67
update(f)   #
print(f)



#Variable length argument
def Total(a,*b):

    c=a

    for i in b:
        c= c+i

    print(c)

Total(80,80,80,80)


def person(name, **data):
    print()
    print(name)
    print(data)

    #for i in data:
     #   print()
      #  print(i, ':', data[i])

    for i,j in data.items():
        print(i,j)


person('Tarun', Age=28, City = 'London', Mob=91835)

