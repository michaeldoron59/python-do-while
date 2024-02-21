# python-do-while
A do while implementation for python

Usage:

In [1]: from do_while import DoWhile

In [2]: with DoWhile(lambda : x>2) as dw:
    ...:     x = 1
    ...:     while dw():
    ...:         x += 1
    ...: 

In [3]: x
Out[3]: 2
