def foo(a):
    print(a)

def bar(a, b):
    print(a, b)


func = foo
func(10)
func.__code__ = bar.__code__
func(10, 20)
