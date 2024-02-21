# python-do-while
A do while implementation for python

Usage:
```ipython
In [1]: from do_while import DoWhile
In [2]: with DoWhile(lambda : x!=1) as dw:
   ...:     while dw():
   ...:         x = 1
In [3]: x
Out[3]: 1
```
