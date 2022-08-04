# """Local Scoope
# Value can be accusedinside the function only"""
# def fun():
#     x=7;y=8;z=9
#     print(x+z)
# fun()
# def fun():
#     a=2;b=7;c=23
#     print(a+b+c)
# fun()

# def fun():
#     x=23; y=55; z=65
#     print(x-y-z)
# fun()
# """ Global scope of a variable,can be accussed by anyone"""
# a=2
# def bm():
#     a=4
#     b=4;c=5
#     print(a)
#     print(b)
# print(a)
# bm()
# print(a)
# """global is the keyword,which is need to be specified if we want to use """
# """ the local variable as global variable.."""
# c=4 
# def fun1():
#     a=3
#     global c,b
#     b=8;c=9
#     print(b)
# print(c)
# fun1()
# print(c);print(b);print(c)
# """count the lenth of string without using built-in-function"""
# def fn(st):
#     c=0
#     for i in st:
#         c+=1
#     return 
# print(fn('python'))
""" A guy  having multiple names """
def sc():
    school='john'
    print(f'Name in school is {school}')
def cl():
    college='max'
    print(f'Name in college is {college}')
    wk()
def wk():
    work='peter'
    print(f'Name at work location is{work}')
    sc()
cl()