# lamda function
addition = lambda a, b: a + b
# print(addition(5, 6))
# first comma separated alphabet are the parameter for function and after colon is the operation to perform

# map function
a = [1, 2, 2, 3, 3, 4]
b = list(range(len(a), len(a + a)))
result = map(addition, a, b)
print(list(result))

# multiple arguments can be given using a comma in map function

# iter function : an list is an iterable as but the difference is when you call next function of
# the iterator than only the function is loader in the memmory
# this is useful when you have huge list of values
lst1 = iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

l = next(lst1)  # this loads next element in the memory

# for i in lst1:
#     print(i)

# Exception handling
# try except, else and finally
try:
    a = 1
    b = int(input("enter a number"))
    c = input("enter something or nothing")
    s = a / b
except ZeroDivisionError as ex:
    print("dividing by zero gives you infinity")
else:
    # this block is used because when we there is no error in the program then perform this task
    print(s)

finally:
    # this block is used to release the resourses
    print('In finally block')


# custom Exception
class MyError(Exception):
    pass


class NewMyError(MyError):
    pass


num = 12
try:
    if num < 10:
        pass
    else:
        raise NewMyError
except NewMyError:
    print('custom error')
