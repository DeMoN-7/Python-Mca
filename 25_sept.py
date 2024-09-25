# wap to estimate the runtime for all the function that u have used so far

import time as t
from calc import add
from email_generator import gen

x=t.time()
sapids = [123,234324,345345,4545]
gen(sapids)
x1=t.time()
print((x1-x)*1000000)
print("2")
x=t.time()
print(add(11,313131313))
x1=t.time()
print((x1-x)*1000000)


# make function to return run time of function