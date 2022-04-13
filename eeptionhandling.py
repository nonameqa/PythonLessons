a = 5
b = 3

try:
    print(a/b)
    k = int(input("enter a num"))
    print(k)

except ValueError as e:
    print("Invalid")

except ZeroDivisionError as e:
    print("Can't",e)

except Exception as e:
    print("everything")

finally:
    print("always execute")