# Lambda Function
# "Anonymous function, small, only
# one expersion"

def myfunc(x):
  return lambda y : y * x

myanswer = myfunc(5)

print(myanswer(10))
