class Foo(object):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print('Call wrapped')
            return func(*args, **kwargs)
        return wrapper

    @decorator
    def bar(self):
        print('Call bar')

Foo().bar()
